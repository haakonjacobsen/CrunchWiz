import React from 'react';

const LoadingSpinnerSVG = () => (
  <svg className="spinner" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
    <rect className="spinner__rect" x="0" y="0" width="100" height="100" fill="none" />
    <circle className="spinner__circle" cx="50" cy="50" r="40" stroke="#999999" fill="none" strokeWidth="6" strokeLinecap="round" />
  </svg>
);

export default LoadingSpinnerSVG;
