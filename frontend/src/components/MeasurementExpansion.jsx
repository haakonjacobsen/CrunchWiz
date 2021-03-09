import React from 'react';
import './MeasurementExpansion.css';
import PropTypes from 'prop-types';
import {
  Line, LineChart,
  ResponsiveContainer,
  XAxis,
  YAxis,
  Tooltip,
} from 'recharts';

export default function MeasurmentExpansion({ name, graphData }) {
  return (
    <div className="Extended-info">
      <h3 className="Extended-title">
        {name}
      </h3>
      <div className="Extended-graph">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart
            width={500}
            height={200}
            data={graphData}
            margin={{
              top: 5, right: 20, bottom: 5, left: 0,
            }}
          >
            <XAxis dataKey="time" />
            <YAxis />
            <Line type="monotone" dataKey="number" />
            <Tooltip />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

MeasurmentExpansion.defaultProps = {
  name: 'Nothing is slected',
  graphData: { name: 'Nothing', number: 0, time: '00-00-00' },
};

MeasurmentExpansion.propTypes = {
  name: PropTypes.string,
  graphData: PropTypes.shape({ root: PropTypes.string.isRequired }),
};
