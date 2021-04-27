/* eslint react/prop-types: 0 */
import React from 'react';
import './MeasurementStat.css';

export default function MeasurementStat({ name, value }) {
  const displayValue = typeof value === 'number'
    && !Number.isInteger(value) ? value.toFixed(2) : value;
  if (name === 'Name') {
    return (null);
  }
  return (
    <div className="Measurement-stat Box">
      <div className="Measurement-stat-header">
        <h2>{name}</h2>
      </div>
      <div className="Measurement-stat-content">
        <h1>{displayValue}</h1>
      </div>
    </div>
  );
}
