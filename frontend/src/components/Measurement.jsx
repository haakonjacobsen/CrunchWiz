import React from 'react';
import './Measurement.css';
import PropTypes from 'prop-types';
import Indicator from './Indicator';
import Stickman from './Stickman';

export default function Measurment({ name, number, showExtended }) {
  if (name === 'most_used_joints') {
    return (
      <div className="Measurment Box" role="button" value={name} tabIndex={0} onClick={() => showExtended(name)} onKeyDown={() => showExtended}>
        <div className="Measurment-number-wrapper">
          <h3 className="Measurment-number" style={{ opacity: '100%' }}>{number}</h3>
        </div>
        <h3 className="Measurment-text">{name}</h3>
      </div>
    );
  } if (name === 'anticipation') {
    return (
      <div className="Measurment Box" role="button" value={name} tabIndex={0} onClick={() => showExtended(name)} onKeyDown={() => showExtended}>
        <div className="Measurment-number-wrapper">
          <h3 className="Measurment-number" style={{ opacity: '100%' }}>{number}</h3>
          <Stickman number={number} />
        </div>
        <h3 className="Measurment-text">{name}</h3>
      </div>
    );
  } if (name === 'emotions') {
    return (
      <div className="Measurment Box" role="button" value={name} tabIndex={0} onClick={() => showExtended(name)} onKeyDown={() => showExtended}>
        <div className="Measurment-number-wrapper">
          <h3 className="Measurment-number">{number}</h3>
          <Stickman number={number} />
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
  name: 'stuff',
  number: 0,
  showExtended: () => {},
};

Measurment.propTypes = {
  name: PropTypes.string,
  number: PropTypes.number,
  showExtended: PropTypes.func,
};
