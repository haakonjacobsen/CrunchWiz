/* eslint react/prop-types: 0 */
import React from 'react';
import './Stickman.css';

export default function Stickman({ name, number }) {
  return (
    <div className="Stickman Box">
      <div className="Stickman-header">
        <h2>{name}</h2>
      </div>
      <div className="Stickman-svg">
        <svg width="220" height="498" viewBox="0 0 220 498" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M86.3456 30.2465L99.2461 17.8068L109.382 30.7073M109.382 30.7073L119.058 17.8068L132.88 30.7073M109.382 30.7073V96.592M109.382 96.592H159.141L178.492 165.702L191.393 234.812M109.382 96.592H59.6231L40.2723 165.702L24.6074 234.812M109.382 96.592V234.812M109.382 234.812H141.633V336.173V442.602M109.382 234.812H74.3665V336.173V442.602M141.633 442.602L132.419 453.199M141.633 442.602L159.141 474.393L168.356 465.178M74.3665 442.602L84.0419 453.199M74.3665 442.602L59.6231 474.393L50.4084 468.864" stroke="black" strokeWidth="2" />
          <circle cx="99" cy="18" r={number === 15 ? 10 : 5} fill={number === 15 ? 'red' : 'black'} />
          <circle cx="85" cy="30.6392" r={number === 17 ? 10 : 5} fill={number === 17 ? 'red' : 'black'} />
          <circle cx="132.812" cy="30.6392" r={number === 18 ? 10 : 5} fill={number === 18 ? 'red' : 'black'} />
          <circle cx="119" cy="18" r={number === 16 ? 10 : 5} fill={number === 16 ? 'red' : 'black'} />
          <circle cx="109" cy="31" r={number === 10 ? 10 : 5} fill={number === 0 ? 'red' : 'black'} />
          <circle cx="109" cy="96.9847" r={number === 1 ? 10 : 5} fill={number === 1 ? 'red' : 'black'} />
          <circle cx="109" cy="235" r={number === 18 ? 10 : 5} fill={number === 8 ? 'red' : 'black'} />
          <circle cx="142.026" cy="235" r={number === 12 ? 10 : 5} fill={number === 12 ? 'red' : 'black'} />
          <circle cx="74.7588" cy="235" r={number === 9 ? 10 : 5} fill={number === 9 ? 'red' : 'black'} />
          <circle cx="75" cy="337" r={number === 10 ? 10 : 5} fill={number === 10 ? 'red' : 'black'} />
          <circle cx="142" cy="337" r={number === 13 ? 10 : 5} fill={number === 13 ? 'red' : 'black'} />
          <circle cx="142" cy="443" r={number === 14 ? 10 : 5} fill={number === 14 ? 'red' : 'black'} />
          <circle cx="132.812" cy="454" r={number === 21 ? 10 : 5} fill={number === 21 ? 'red' : 'black'} />
          <circle cx="83.9736" cy="453.592" r={number === 24 ? 10 : 5} fill={number === 24 ? 'red' : 'black'} />
          <circle cx="61" cy="475" r={number === 22 ? 10 : 5} fill={number === 22 ? 'red' : 'black'} />
          <circle cx="50.8018" cy="469.256" r={number === 23 ? 10 : 5} fill={number === 23 ? 'red' : 'black'} />
          <circle cx="168.749" cy="465.571" r={number === 20 ? 10 : 5} fill={number === 20 ? 'red' : 'black'} />
          <circle cx="159" cy="475" r={number === 19 ? 10 : 5} fill={number === 19 ? 'red' : 'black'} />
          <circle cx="74.7588" cy="443.455" r={number === 11 ? 10 : 5} fill={number === 11 ? 'red' : 'black'} />
          <circle cx="159.534" cy="97" r={number === 5 ? 10 : 5} fill={number === 5 ? 'red' : 'black'} />
          <circle cx="60.0156" cy="97" r={number === 2 ? 10 : 5} fill={number === 2 ? 'red' : 'black'} />
          <circle cx="40.665" cy="166.095" r={number === 3 ? 10 : 5} fill={number === 3 ? 'red' : 'black'} />
          <circle cx="178.885" cy="166" r={number === 6 ? 10 : 5} fill={number === 6 ? 'red' : 'black'} />
          <circle cx="191" cy="235" r={number === 7 ? 10 : 5} fill={number === 7 ? 'red' : 'black'} />
          <circle cx="25" cy="235" r={number === 4 ? 10 : 5} fill={number === 4 ? 'red' : 'black'} />
        </svg>
      </div>
    </div>
  );
}
