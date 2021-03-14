import React from 'react';
import './Measurement.css';
import PropTypes from 'prop-types';

export default function Measurment({ name, number, showExtended }) {
  let circleColor = '#C4C4C4';
  if (number > 20) {
    circleColor = '#F45656';
  } else if (number > 10) {
    circleColor = '#F4B556';
  } else if (number > -10) {
    circleColor = '#C4C4C4';
  } else if (number > -20) {
    circleColor = '#B3D2A0';
  } else {
    circleColor = '#8BD45F';
  }
  return (
    <div className="Measurment" role="button" value={name} tabIndex={0} onClick={() => showExtended(name)} onKeyDown={() => showExtended}>
      <div className="Measurment-number-wrapper">
        <h3 className="Measurment-number">
          {number}
          {' '}
          %
        </h3>
        <svg className="MeasurementIndicator" height="100%" width="100%">
          <circle cx="50%" cy="50%" r="20%" fill={circleColor} />
        </svg>
      </div>
      <h3 className="Measurment-text">{name}</h3>
    </div>
  );
}

Measurment.defaultProps = {
  name: 'stuff',
  number: 0,
  showExtended: () => {},
};

Measurment.propTypes = {
  name: PropTypes.string,
  number: PropTypes.number,
  showExtended: PropTypes.func,
};
