import React from 'react';
import './Measurement.css';
import PropTypes from 'prop-types';
import Indicator from './Indicator';

export default function Measurment({
  name, number, showExtended, specialMeasurements,
}) {
  if (specialMeasurements.includes(name)) {
    return (
      <div className="Measurment Box" role="button" value={name} tabIndex={0} onClick={() => showExtended(name)} onKeyDown={() => showExtended}>
        <div className="Measurment-number-wrapper">
          <h3 className="Measurment-number" style={{ opacity: '100%' }}>{number}</h3>
        </div>
        <h3 className="Measurment-text">{name}</h3>
      </div>
    );
  }
  return (
    <div className="Measurment Box" role="button" value={name} tabIndex={0} onClick={() => showExtended(name)} onKeyDown={() => showExtended}>
      <div className="Measurment-number-wrapper">
        <h3 className="Measurment-number">
          {number}
          {' '}
          %
        </h3>
        <Indicator number={number} />
      </div>
      <h3 className="Measurment-text">{name}</h3>
    </div>
  );
}

Measurment.defaultProps = {
  name: 'no_measurement',
  number: 0,
  showExtended: () => {},
  specialMeasurements: [],
};

Measurment.propTypes = {
  name: PropTypes.string,
  number: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
  showExtended: PropTypes.func,
  specialMeasurements: PropTypes.arrayOf(PropTypes.string),
};
