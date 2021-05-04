import React from 'react';
import './Header.css';
import CrunchWizLogo from './SVG/CrunchWizLogo';
import EmpaticaSVG from './SVG/EmpaticaSVG';
import OpenPoseSVG from './SVG/OpenPoseSVG';
import EyeSVG from './SVG/EyeSVG';

const Header = () => (
  <header className="App-header">
    <div className="Logo-wrapper">
      <CrunchWizLogo />
    </div>
    <div className="Device-status-nav">
      <div className="Device-status-wrapper">
        <div className="Device-logo">
          <EmpaticaSVG />
        </div>
        <h2 className="Device-title">Empatica E4</h2>
      </div>
      <div className="Device-status-wrapper">
        <div className="Device-logo">
          {/* Icon made by Freepik from www.flaticon.com */}
          <EyeSVG />
        </div>
        <h2 className="Device-title">Tobii</h2>
      </div>
      <div className="Device-status-wrapper">
        <div className="Device-logo">
          <OpenPoseSVG />
        </div>
        <h2 className="Device-title Device-active">openPose</h2>
      </div>
    </div>
  </header>
);

export default Header;
