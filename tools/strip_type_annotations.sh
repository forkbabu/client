#!/bin/bash
set -e

CODEMOD_DIRS="sdk sdk/internal sdk/interface sdk/backend sdk/lib sdk/verify sdk/integration_utils sdk/service"

CODEMOD_SRC_BASE="wandb"
CODEMOD_DEST_SUFFIX="_py27"
CODEMOD_DEST_SUFFIX_TMP="_tmp"

# Hack for check
CODEMOD_SDK_EXCLUDES="--exclude internal --exclude interface --exclude backend --exclude lib --exclude verify --exclude integration_utils --exclude sdk/launch --exclude service"

check=false
if [ "$1" == "--check" ]; then
  check=true
fi

for dir in $CODEMOD_DIRS; do
  src="$CODEMOD_SRC_BASE/${dir}/"

  dest=`echo $CODEMOD_SRC_BASE/$dir | sed 's:/sdk:/sdk_py27:'`
  dest_tmp="$dest${CODEMOD_DEST_SUFFIX_TMP}/"
  if $check; then
    dest_orig=$dest
    dest=$dest_tmp
  fi

  if [ "$dest" == "" -o "$dest" == "/" ]; then
    echo "SAFETY CHECK"
    exit 1
  fi

  mkdir -p $dest
  rm -f ${dest}/*.py

  cp -f $src/*.py $dest
  python3 -m libcst.tool codemod --no-format remove_types.RemoveTypesTransformer $dest/*.py

  for f in $dest/*.py; do
    sed -i.tmp 's/__COMMENT__/# /g; 1s/^#$/# File is generated by: tox -e codemod/' $f
    rm $f.tmp
    chmod -w $f
    b=`basename $f`
    cnt_src=`wc -l <$src/$b`
    cnt_dest=`wc -l <$dest/$b`
    if [ $cnt_src -ne $cnt_dest ]; then
      echo "ERROR: mismatch file length $b $cnt_src != $cnt_dest"
      exit 1
    fi
  done

  if $check; then
    #diff -q $DEST $DEST_TMP | egrep "[.]py$"
    set +e
    diff --exclude="*.pyc" --exclude="__pycache__" $CODEMOD_SDK_EXCLUDES -q $dest_orig $dest_tmp
    result="$?"
    set -e
    rm -f ${dest}*
    rmdir $dest
    if [ $result -ne 0 ]; then
      echo "ERROR: codemod check failed."
      exit 1
    fi
  fi
done
