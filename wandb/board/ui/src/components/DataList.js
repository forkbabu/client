import React from 'react';
import {List, Input, Icon, Modal, Button, Grid} from 'semantic-ui-react';
import FixedLengthString from '../components/FixedLengthString';
import {flatten} from '../util/flatten';
import {Sparklines, SparklinesLine} from 'react-sparklines';
import {XYPlot, LineSeries, XAxis, YAxis, VerticalBarSeries} from 'react-vis';
import {
  displayValue,
  fuzzyMatch,
  fuzzyMatchHighlight,
  truncateString,
} from '../util/runhelpers';
import _ from 'lodash';

class DataList extends React.Component {
  state = {};
  constructor(props) {
    super(props);
    this.noData = this.noDataDefault;
    this.formatValue = this.formatValueDefault;
  }

  _setup(props) {
    if (props.noData) {
      this.noData = props.noData;
    }
    if (props.formatValue) {
      this.formatValue = props.formatValue;
    }

    if (props.data && Object.keys(props.data).length > 0) {
      this.flatData = flatten(props.data, {safe: true});
    }
  }

  componentWillMount() {
    this._setup(this.props);
  }

  componentWillReceiveProps(nextProps) {
    this._setup(nextProps);
  }

  isDict(v) {
    return (
      typeof v === 'object' &&
      v !== null &&
      !(v instanceof Array) &&
      !(v instanceof Date)
    );
  }

  prepDataDefault(data) {
    return data;
  }

  configItem(key, value, i, highlighted = false) {
    return (
      <List.Item key={'config ' + i}>
        <List.Content>
          <List.Header>
            {highlighted ? key : <FixedLengthString text={key} />}
          </List.Header>
          <List.Description style={{width: '100px'}}>
            {this.formatValue(value)}
          </List.Description>
        </List.Content>
      </List.Item>
    );
  }

  noDataDefault() {
    return <p>No data</p>;
  }

  formatValueDefault(value) {
    if (value._type && value._type === 'histogram') {
      let data = [];
      for (let i = 0; i < value.values.length; i++) {
        data.push({
          x0: value.bins[i],
          x: value.bins[i + 1],
          y: value.values[i],
        });
      }
      console.log(data);

      return (
        <XYPlot width={100} height={20}>
          <VerticalBarSeries data={data} />
        </XYPlot>
      );
    } else {
      return displayValue(value);
    }
  }

  rawMode = e => {
    this.setState({format: 'raw'});
  };

  jsonMode = e => {
    this.setState({format: 'json'});
  };

  renderLongList() {
    return (
      <div>
        <Grid style={{marginBottom: 0}}>
          <Grid.Column floated="left" width={10}>
            <Input
              onChange={(e, {value}) => this.setState({filter: value})}
              icon={{name: 'search', circular: true, link: true}}
              placeholder="Search..."
              size="mini"
              className="DataListSearchBox"
            />
          </Grid.Column>
          <Grid.Column floated="right" width={3}>
            <Modal
              trigger={<Button icon="expand" size="mini" floated="right" />}>
              <Modal.Header>
                {this.props.name}
                <Button.Group floated="right">
                  <Button
                    active={this.state.format !== 'json'}
                    onClick={this.rawMode}>
                    List
                  </Button>
                  <Button
                    active={this.state.format === 'json'}
                    onClick={this.jsonMode}>
                    Json
                  </Button>
                </Button.Group>
              </Modal.Header>
              <Modal.Content>
                {this.state.format === 'json' ? (
                  JSON.stringify(this.props.data, null, '\t')
                ) : (
                  <List>
                    {_.keys(this.flatData)
                      .sort()
                      .map((key, i) =>
                        this.configItem(
                          key,
                          this.formatValue(this.flatData[key]),
                          i
                        )
                      )}
                  </List>
                )}
              </Modal.Content>
            </Modal>
          </Grid.Column>
        </Grid>
        <div className="DataListWithSearch">
          <List divided>
            {this.state.filter
              ? fuzzyMatch(Object.keys(this.flatData), this.state.filter).map(
                  (key, i) =>
                    this.configItem(
                      fuzzyMatchHighlight(key, this.state.filter),
                      this.flatData[key],
                      i,
                      true
                    )
                )
              : _.keys(this.flatData)
                  .sort()
                  .map((key, i) =>
                    this.configItem(
                      key,
                      this.formatValue(this.flatData[key]),
                      i
                    )
                  )}
          </List>
        </div>
      </div>
    );
  }

  renderShortList() {
    return (
      <div className="DataList">
        <List divided>
          {_.keys(this.flatData)
            .sort()
            .map((key, i) => this.configItem(key, this.flatData[key], i))}
        </List>
      </div>
    );
  }

  renderNoData() {
    return <div className="DataList">{this.noData()}</div>;
  }

  render() {
    if (this.flatData && _.size(this.flatData) > 0) {
      if (_.size(this.flatData) > 10) {
        return this.renderLongList();
      } else {
        return this.renderShortList();
      }
    } else {
      return this.renderNoData();
    }
  }
}

export default DataList;
