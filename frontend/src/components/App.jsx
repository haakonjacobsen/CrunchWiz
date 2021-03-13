import React from 'react';
import './App.css';
import Header from './Header';
import MainContent from './MainContent';

const App = () => (
  <div className="App">
    <Header />
    <div className="MainContentCentralizer">
      <MainContent />
    </div>
  </div>
);

export default App;
