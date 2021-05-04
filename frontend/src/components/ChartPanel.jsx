/* eslint react/prop-types: 0 */
import React, { useEffect, useState } from 'react';
import './MeasurementExpansion.css';
import BarGraph from './BarGraph';
import LineGraph from './LineGraph';
import RadarGraph from './RadarGraph';
import RadarGraphSVG from './SVG/RadarGraphSVG';
import TableGraphSVG from './SVG/TableGraphSVG';
import LineGraphSVG from './SVG/LineGraphSVG';

export default function ChartPanel({
  name, graphData, dataStats, hasTextValue, specialMeasurements, setMeasurment,
}) {
  const [time, setTimeIndex] = useState(Infinity);
  const [minutes, setMinutes] = useState(Infinity);
  const [graph, setGraph] = useState(1);
  const [barStat, setBarStat] = useState('Max');

  function getLastMinutes(lastMinutes) {
    if (lastMinutes === Infinity) {
      setTimeIndex(Infinity);
      setMinutes(Infinity);
      return;
    }
    const timer = new Date(Date.now() - lastMinutes * 60000).toLocaleTimeString();
    for (let i = graphData.length - 1; i >= 0; i -= 1) {
      const dataTime = graphData[i].time;
      console.log(timer, dataTime, timer < dataTime);
      if (dataTime < timer) {
        setTimeIndex(graphData.length - 1 - i);
        setMinutes(lastMinutes);
        return;
      }
      // console.log(timer, dataTime, dataTime < timer);
    }
    setTimeIndex(Infinity);
    setMinutes(lastMinutes);
  }
  useEffect(() => {
    getLastMinutes(minutes);
  }, [graphData]);

  function formatStats(stats) {
    const copy = (
      Object.keys(stats).filter((key) => !specialMeasurements.includes(key)).map((key) => {
        const stat = stats[key];
        stat.Name = key;
        return stat;
      }));
    return copy;
  }

  function formatTextStats(stats) {
    return (Object.keys(stats).map((key) => ({ Count: stats[key], Name: key })));
  }
  if (hasTextValue) {
    return (
      <div className="Extended-graph-container Box">
        <div className="Extended-graph-header">
          <div className="Graph-panel Box">
            <button type="button" className={`Graph-panel-choice Left ${graph === 1 ? 'selected' : ''}`} onClick={() => setGraph(1)} onKeyDown={() => setGraph(1)}>
              <div className="SVG-close">
                <RadarGraphSVG />
              </div>
            </button>
            <button type="button" className={`Graph-panel-choice Right ${graph === 2 ? 'selected' : ''}`} onClick={() => setGraph(2)} onKeyDown={() => setGraph(2)}>
              <div className="SVG-close">
                <TableGraphSVG />
              </div>
            </button>
          </div>
        </div>
        {graph === 1
          ? <RadarGraph dataStats={formatTextStats(dataStats[name])} stat="Count" />
          : (
            <BarGraph
              dataStats={formatTextStats(dataStats[name])}
              stat="Count"
              name={name}
              setMeasurment={setMeasurment}
              specialMeasurements={specialMeasurements}
            />
          )}
      </div>
    );
  }
  return (
    <div className="Extended-graph-container Box">
      <div className="Extended-graph-header">
        {graph === 1
          ? (
            <div className="Button-panel Box">
              <button type="button" className={`Graph-panel-choice Left ${minutes === 1 ? 'selected' : ''}`} onClick={() => getLastMinutes(1)} onKeyDown={() => getLastMinutes(1)}>1 min</button>
              <button type="button" className={`Graph-panel-choice Center ${minutes === 3 ? 'selected' : ''}`} onClick={() => getLastMinutes(3)} onKeyDown={() => getLastMinutes(3)}>3 min</button>
              <button type="button" className={`Graph-panel-choice Center ${minutes === 5 ? 'selected' : ''}`} onClick={() => getLastMinutes(5)} onKeyDown={() => getLastMinutes(5)}>5 min</button>
              <button type="button" className={`Graph-panel-choice Right ${minutes === Infinity ? 'selected' : ''}`} onClick={() => getLastMinutes(Infinity)} onKeyDown={() => getLastMinutes(Infinity)}>All</button>
            </div>
          )
          : (
            <div className="Button-panel Box">
              <button type="button" className={`Graph-panel-choice Left ${barStat === 'Max' ? 'selected' : ''}`} onClick={() => setBarStat('Max')} onKeyDown={() => setBarStat('Max')}>Max</button>
              <button type="button" className={`Graph-panel-choice Center ${barStat === 'Min' ? 'selected' : ''}`} onClick={() => setBarStat('Min')} onKeyDown={() => setBarStat('Max')}>Min</button>
              <button type="button" className={`Graph-panel-choice Right ${barStat === 'Average' ? 'selected' : ''}`} onClick={() => setBarStat('Average')} onKeyDown={() => setBarStat('Max')}>Average</button>
            </div>
          )}
        <div className="Graph-panel Box">
          <button type="button" className={`Graph-panel-choice Left ${graph === 1 ? 'selected' : ''}`} onClick={() => setGraph(1)} onKeyDown={() => setGraph(1)}>
            <div className="SVG-close">
              <LineGraphSVG />
            </div>
          </button>
          <button type="button" className={`Graph-panel-choice Right ${graph === 2 ? 'selected' : ''}`} onClick={() => setGraph(2)} onKeyDown={() => setGraph(2)}>
            <div className="SVG-close">
              <TableGraphSVG />
            </div>
          </button>
        </div>
      </div>
      { graph === 1
        ? <LineGraph graphData={graphData} time={time} />
        : (
          <BarGraph
            stat={barStat}
            dataStats={formatStats(dataStats)}
            name={name}
            specialMeasurements={specialMeasurements}
            setMeasurment={setMeasurment}
          />
        )}
    </div>
  );
}
