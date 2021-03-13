import React from 'react';
import './Measurement.css';
import PropTypes from 'prop-types';

export default function Measurment({ name, number, showExtended }) {
  return (
    <div className="Measurment" role="button" value={name} tabIndex={0} onClick={() => showExtended(name)} onKeyDown={() => showExtended}>
      <div className="Measurment-number-wrapper">
        <h3 className="Measurment-number">{number}</h3>
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
