/* eslint react/prop-types: 0 */
import React from 'react';
import './Stickman.css';

export default function Stickman({ name }) {
  return (
    <div className="Stickman Box">
      <div className="Stickman-header">
        <h2>{name}</h2>
      </div>
      <div className="Stickman-svg">
        <svg width="100%" height="100%" viewBox="0 0 220 498" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M86.3456 30.2465L99.2461 17.8068L109.382 30.7073M109.382 30.7073L119.058 17.8068L132.88 30.7073M109.382 30.7073V96.592M109.382 96.592H159.141L178.492 165.702L191.393 234.812M109.382 96.592H59.6231L40.2723 165.702L24.6074 234.812M109.382 96.592V234.812M109.382 234.812H141.633V336.173V442.602M109.382 234.812H74.3665V336.173V442.602M141.633 442.602L132.419 453.199M141.633 442.602L159.141 474.393L168.356 465.178M74.3665 442.602L84.0419 453.199M74.3665 442.602L59.6231 474.393L50.4084 468.864" stroke="black" strokeWidth="2" />
          <circle cx="99" cy="18" r={name === 'Right Eye' ? 10 : 5} fill={name === 'Right Eye' ? 'red' : 'black'} />
          <circle cx="85" cy="30.6392" r={name === 'Right Ear' ? 10 : 5} fill={name === 'Right Ear' ? 'red' : 'black'} />
          <circle cx="132.812" cy="30.6392" r={name === 'Left Ear' ? 10 : 5} fill={name === 'Left Ear' ? 'red' : 'black'} />
          <circle cx="119" cy="18" r={name === 'Left Eye' ? 10 : 5} fill={name === 'Left Eye' ? 'red' : 'black'} />
          <circle cx="109" cy="31" r={name === 'Nose' ? 10 : 5} fill={name === 'Nose' ? 'red' : 'black'} />
          <circle cx="109" cy="96.9847" r={name === 'Neck' ? 10 : 5} fill={name === 'Neck' ? 'red' : 'black'} />
          <circle cx="109" cy="235" r={name === 'MidHip' ? 10 : 5} fill={name === 'MidHip' ? 'red' : 'black'} />
          <circle cx="142.026" cy="235" r={name === 'Left Hip' ? 10 : 5} fill={name === 'Left Hip' ? 'red' : 'black'} />
          <circle cx="74.7588" cy="235" r={name === 'Right Hip' ? 10 : 5} fill={name === 'Right Hip' ? 'red' : 'black'} />
          <circle cx="75" cy="337" r={name === 'Right Knee' ? 10 : 5} fill={name === 'Right Knee' ? 'red' : 'black'} />
          <circle cx="142" cy="337" r={name === 'Left Knee' ? 10 : 5} fill={name === 'Left Knee' ? 'red' : 'black'} />
          <circle cx="142" cy="443" r={name === 'Left Ankle' ? 10 : 5} fill={name === 'Left Ankle' ? 'red' : 'black'} />
          <circle cx="132.812" cy="454" r={name === 'Left Heel' ? 10 : 5} fill={name === 'Left Heel' ? 'red' : 'black'} />
          <circle cx="83.9736" cy="453.592" r={name === 'Right Heel' ? 10 : 5} fill={name === 'Right Heel' ? 'red' : 'black'} />
          <circle cx="61" cy="475" r={name === 'Right BigToe' ? 10 : 5} fill={name === 'Right BigToe' ? 'red' : 'black'} />
          <circle cx="50.8018" cy="469.256" r={name === 'Right SmallToe' ? 10 : 5} fill={name === 'Right SmallToe' ? 'red' : 'black'} />
          <circle cx="168.749" cy="465.571" r={name === 'Left SmallToe' ? 10 : 5} fill={name === 'Left SmallToe' ? 'red' : 'black'} />
          <circle cx="159" cy="475" r={name === 'Left BigToe' ? 10 : 5} fill={name === 'Left BigToe' ? 'red' : 'black'} />
          <circle cx="74.7588" cy="443.455" r={name === 'Right Ankle' ? 10 : 5} fill={name === 'Right Ankle' ? 'red' : 'black'} />
          <circle cx="159.534" cy="97" r={name === 'Left Shoulder' ? 10 : 5} fill={name === 'Left Shoulder' ? 'red' : 'black'} />
          <circle cx="60.0156" cy="97" r={name === 'Right Shoulder' ? 10 : 5} fill={name === 'Right Shoulder' ? 'red' : 'black'} />
          <circle cx="40.665" cy="166.095" r={name === 'Right Elbow' ? 10 : 5} fill={name === 'Right Elbow' ? 'red' : 'black'} />
          <circle cx="178.885" cy="166" r={name === 'Left Elbow' ? 10 : 5} fill={name === 'Left Elbow' ? 'red' : 'black'} />
          <circle cx="191" cy="235" r={name === 'Left Wrist' ? 10 : 5} fill={name === 'Left Wrist' ? 'red' : 'black'} />
          <circle cx="25" cy="235" r={name === 'Right Wrist' ? 10 : 5} fill={name === 'Right Wrist' ? 'red' : 'black'} />
        </svg>
      </div>
    </div>
  );
}
