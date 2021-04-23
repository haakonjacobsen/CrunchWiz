/* eslint react/prop-types: 0 */
import React, { useState } from 'react';
import './MeasurementExpansion.css';
import Indicator from './Indicator';
import MeasurmentStat from './MeasurementStat';
import Stickman from './Stickman';
import LineChart from './LineGraph';
import BarGraph from './BarGraph';

export default function MeasurmentExpansion({
  name, graphData, dataStats, changeExtended, number,
}) {
  const [time, setTime] = useState(5);
  const [graph, setGraph] = useState('line');

  function formatStats(stats) {
    const result = Object.keys(stats).filter((key) => key !== 'most_used_joints').map((key) => {
      const res = stats[key];
      res.name = key;
      return res;
    });
    console.log(result);
    return (result);
  }
  return (
    <div className="Extended-panel">
      <div className="Extended-header">
        <div className="Extended-title">
          <h3>
            {name}
          </h3>
          <div className="SVG-indicator">
            <Indicator number={number} />
          </div>
        </div>
        <button type="button" className="SVG-close" onClick={() => changeExtended(false)} onKeyDown={() => changeExtended(false)}>
          <svg width="100%" height="100%" viewBox="0 0 65 65" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M38.455 32.5532L63.7647 7.24275C65.4118 5.59641 65.4118 2.9345 63.7647 1.28816C62.1184 -0.35818 59.4565 -0.35818 57.8101 1.28816L32.4996 26.5986L7.18993 1.28816C5.54281 -0.35818 2.88168 -0.35818 1.23533 1.28816C-0.411778 2.9345 -0.411778 5.59641 1.23533 7.24275L26.545 32.5532L1.23533 57.8637C-0.411778 59.51 -0.411778 62.172 1.23533 63.8183C2.05581 64.6395 3.1346 65.0521 4.21263 65.0521C5.29066 65.0521 6.36868 64.6395 7.18993 63.8183L32.4996 38.5078L57.8101 63.8183C58.6314 64.6395 59.7094 65.0521 60.7874 65.0521C61.8654 65.0521 62.9435 64.6395 63.7647 63.8183C65.4118 62.172 65.4118 59.51 63.7647 57.8637L38.455 32.5532Z" fill="#757575" />
          </svg>
        </button>
      </div>
      <div className="Extended-main">
        <div className="Extended-stats">
          { name === 'most_used_joints'
            ? <Stickman name={graphData[graphData.length - 1].value} />
            : Object.entries(dataStats[name]).map(([key, value]) => (
              <MeasurmentStat name={key} value={value} />
            ))}
        </div>
        <div className="Extended-graph-container Box">
          <div className="Extended-graph-header">
            <div className="Graph-panel Box">
              <button type="button" className={`Graph-panel-choice Left ${time === 5 ? 'selected' : ''}`} onClick={() => setTime(5)} onKeyDown={() => setTime(5)}>1 min</button>
              <button type="button" className={`Graph-panel-choice Center ${time === 10 ? 'selected' : ''}`} onClick={() => setTime(10)} onKeyDown={() => setTime(10)}>5 min</button>
              <button type="button" className={`Graph-panel-choice Center ${time === 20 ? 'selected' : ''}`} onClick={() => setTime(20)} onKeyDown={() => setTime(20)}>10 min</button>
              <button type="button" className={`Graph-panel-choice Right ${time === 10000 ? 'selected' : ''}`} onClick={() => setTime(10000)} onKeyDown={() => setTime(10000)}>All</button>
            </div>
            <div className="Box">
              <button type="button" className={`Graph-panel-choice Left ${graph === 'line' ? 'selected' : ''}`} onClick={() => setGraph('line')} onKeyDown={() => setGraph('line')}>
                <div className="SVG-close">
                  <svg width="100%" height="100%" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M30.6 1.70002C28.726 1.69663 27.2041 3.21308 27.2007 5.08714C27.1991 5.9704 27.542 6.81954 28.1565 7.45399L21.9447 19.8753C21.8086 19.8528 21.6712 19.8388 21.5334 19.8334C21.0944 19.8343 20.6598 19.9206 20.2538 20.0873L15.4315 14.6643C15.713 14.1666 15.8628 13.6053 15.8667 13.0334C15.8667 11.1557 14.3445 9.63344 12.4667 9.63344C10.5889 9.63344 9.06671 11.1557 9.06671 13.0334C9.07003 13.8451 9.36627 14.6282 9.90084 15.2389L4.00748 25.5612C3.8072 25.5227 3.60393 25.5022 3.4 25.5C1.52223 25.5 0 27.0222 0 28.9C0 30.7778 1.52223 32.3 3.4 32.3C5.27777 32.3 6.8 30.7778 6.8 28.9C6.79668 28.0884 6.50044 27.3053 5.96587 26.6945L11.8592 16.3721C12.4919 16.4971 13.1474 16.4301 13.7417 16.1795L18.5641 21.6025C18.2842 22.1006 18.1359 22.6619 18.1334 23.2334C18.1278 25.1111 19.6454 26.638 21.5231 26.6436C23.4009 26.6492 24.9277 25.1317 24.9334 23.2539C24.936 22.368 24.5928 21.5161 23.9768 20.8795L30.1886 8.45812C30.3247 8.48069 30.4621 8.49471 30.6 8.50002C32.4778 8.50002 34 6.97779 34 5.10002C34 3.22225 32.4778 1.70002 30.6 1.70002ZM3.4 30.0334C2.77405 30.0334 2.26664 29.526 2.26664 28.9C2.26664 28.2741 2.77405 27.7667 3.4 27.7667C4.02595 27.7667 4.53336 28.2741 4.53336 28.9C4.53336 29.526 4.02595 30.0334 3.4 30.0334ZM12.4666 14.1667C11.8407 14.1667 11.3333 13.6593 11.3333 13.0333C11.3333 12.4074 11.8407 11.9 12.4666 11.9C13.0926 11.9 13.6 12.4074 13.6 13.0333C13.6 13.6593 13.0926 14.1667 12.4666 14.1667ZM21.5334 24.3667C20.9074 24.3667 20.4 23.8593 20.4 23.2333C20.4 22.6074 20.9074 22.1 21.5334 22.1C22.1593 22.1 22.6667 22.6074 22.6667 23.2333C22.6666 23.8593 22.1592 24.3667 21.5334 24.3667ZM30.6 6.23337C29.9741 6.23337 29.4666 5.72596 29.4666 5.10002C29.4666 4.47407 29.9741 3.96666 30.6 3.96666C31.2259 3.96666 31.7334 4.47407 31.7334 5.10002C31.7334 5.72596 31.2259 6.23337 30.6 6.23337Z" fill="#757575" />
                  </svg>
                </div>
              </button>
              <button type="button" className={`Graph-panel-choice Right ${graph === 'bar' ? 'selected' : ''}`} onClick={() => setGraph('bar')} onKeyDown={() => setGraph('bar')}>
                <div className="SVG-close">
                  <svg width="100%" height="100%" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M7.5 11.7834H1.07322C0.483264 11.7834 0.00627615 12.2604 0 12.8567V28.9236C0 29.5198 0.483264 29.9968 1.07322 29.9968H7.5C8.09623 29.9968 8.57322 29.5136 8.57322 28.9236V12.8567C8.57322 12.2604 8.08996 11.7834 7.5 11.7834Z" fill="#757575" />
                    <path d="M18.2139 0.00317383H11.7871C11.1971 0.00317383 10.7139 0.480161 10.7139 1.07012V28.9237C10.7139 29.5199 11.1971 29.9969 11.7871 29.9969H18.2139C18.8101 29.9969 19.2871 29.5136 19.2871 28.9237V1.0764C19.2871 0.480161 18.8038 0.00317383 18.2139 0.00317383Z" fill="#757575" />
                    <path d="M28.9268 8.57007H22.5C21.9037 8.57007 21.4268 9.04706 21.4268 9.64329V28.9236C21.4268 29.5199 21.91 29.9968 22.5 29.9968H28.9268C29.523 29.9968 30 29.5136 30 28.9236V9.64329C30 9.04706 29.5167 8.57007 28.9268 8.57007Z" fill="#757575" />
                  </svg>
                </div>
              </button>
            </div>
          </div>
          { graph === 'line'
            ? <LineChart graphData={graphData} time={time} />
            : <BarGraph name={name} dataStats={formatStats(dataStats)} />}
        </div>
      </div>
    </div>
  );
}
