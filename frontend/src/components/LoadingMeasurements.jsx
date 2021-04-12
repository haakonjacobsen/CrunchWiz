import React from 'react';
import './ConnectingPanel.css';
import './LoadingMeasurements.css';
import { css } from '@emotion/react';
import ClipLoader from 'react-spinners/ClipLoader';

// Can be a string as well. Need to ensure each key-value pair ends with ;
const override = css`
  display: block;
  margin: 0 auto;
  border-color: red;
`;

export default function LoadingMeasurements() {
  const loading = true;
  const color = '#ffffff';
  return (
    <div className="Connecting-panel">
      <h1 className="Connecting-panel-title">Calculating baseline</h1>
      <ClipLoader color={color} loading={loading} css={override} size={150} />
    </div>
  );
}
