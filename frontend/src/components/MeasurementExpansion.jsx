import React from 'react';
import './MeasurementExpansion.css';
import PropTypes from 'prop-types';

export default function MeasurmentExpansion({ name }) {
  return (
    <div className="Extended-info">
      <h3 className="Extended-title">
        {name}
      </h3>
      <div className="Extended-graph"> </div>
    </div>
  );
}

MeasurmentExpansion.defaultProps = {
  name: 'Nothing is slected',
};

MeasurmentExpansion.propTypes = {
  name: PropTypes.string,
};
