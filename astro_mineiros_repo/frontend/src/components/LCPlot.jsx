import React from 'react'
import Plot from 'react-plotly.js'

export default function LCPlot({time, flux}){
  return (
    <Plot data={[{x:time, y:flux, mode:'lines'}]} layout={{width:700, height:300, title:'Light Curve'}} />
  )
}
