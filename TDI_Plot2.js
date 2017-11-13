// You can reproduce this figure in plotly.js with the following code!

// Learn more about plotly.js here: https://plot.ly/javascript/getting-started

/* Here's an example minimal HTML template
 *
 * <!DOCTYPE html>
 *   <head>
 *     <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
 *   </head>
 *   <body>
 *   <!-- Plotly chart will be drawn inside this div -->
 *   <div id="plotly-div"></div>
 *     <script>
 *     // JAVASCRIPT CODE GOES HERE
 *     </script>
 *   </body>
 * </html>
 */

trace1 = {
  x: [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017], 
  y: [0.0739130434783, 0.0588235294118, 0.0548780487805, 0.0807086614173, 0.0667938931298, 0.0851851851852, 0.0413669064748, 0.0699300699301, 0.0867346938776, 0.0761589403974, 0.0741935483871, 0.138364779874, 0.157975460123, 0.194610778443, 0.22514619883, 0.182857142857, 0.135474860335, 0.19262295082, 0.20320855615], 
  type: 'scatter', 
  uid: 'a3a4e2', 
  xaxis: 'x', 
  xsrc: 'unguyen:4:e7e41a', 
  yaxis: 'y', 
  ysrc: 'unguyen:4:3c8d35'
};
trace2 = {
  x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
  y: [12, 11, 11, 14, 8, 12, 9, 14, 11, 50], 
  type: 'bar', 
  uid: 'c6976d', 
  xaxis: 'x2', 
  xsrc: 'unguyen:4:f9c6a0', 
  yaxis: 'y2', 
  ysrc: 'unguyen:4:7e2b22'
};
data = [trace1, trace2];
layout = {
  annotations: [
    {
      x: 0.225, 
      y: 1, 
      font: {size: 16}, 
      showarrow: false, 
      text: 'NYT coverage on sexual related issues', 
      xanchor: 'center', 
      xref: 'paper', 
      yanchor: 'bottom', 
      yref: 'paper'
    }, 
    {
      x: 0.775, 
      y: 1, 
      font: {size: 16}, 
      showarrow: false, 
      text: 'Count of articles per month in 2017', 
      xanchor: 'center', 
      xref: 'paper', 
      yanchor: 'bottom', 
      yref: 'paper'
    }
  ], 
  xaxis: {
    anchor: 'y', 
    autorange: true, 
    domain: [0, 0.45], 
    range: [1997.69198005, 2018.30801995], 
    title: 'Year', 
    type: 'linear'
  }, 
  xaxis2: {
    anchor: 'y2', 
    autorange: true, 
    domain: [0.55, 1], 
    range: [0.5, 10.5], 
    title: 'Month', 
    type: 'linear'
  }, 
  yaxis: {
    anchor: 'x', 
    autorange: true, 
    domain: [0, 1], 
    range: [0.028591629033, 0.237921476272], 
    title: 'Coverage percentage(%)', 
    type: 'linear'
  }, 
  yaxis2: {
    anchor: 'x2', 
    autorange: true, 
    domain: [0, 1], 
    range: [0, 52.6315789474], 
    title: 'Articles', 
    type: 'linear'
  }
};
Plotly.plot('plotly-div', {
  data: data,
  layout: layout
});