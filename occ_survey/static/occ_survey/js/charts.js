var chart_data = [
    { date: data.dates[0], value: data.consumption[0] },
    { date: data.dates[1], value: data.consumption[1] },
    { date: data.dates[2], value: data.consumption[2] },
    { date: data.dates[3], value: data.consumption[3] },
    { date: data.dates[4], value: data.consumption[4] },
    //{ date: data.dates[5], value: data.consumption[5] },
    //{ date: data.dates[6], value: data.consumption[6] },
  ];

new Morris.Bar({
  // ID of the element in which to draw the chart.
  element: 'daily_consumption',
  // Chart data records -- each entry in this array corresponds to a point on
  // the chart.
  data:  chart_data,
  // The name of the data record attribute that contains x-values.
  xkey: 'date',
  // A list of names of data record attributes that contain y-values.
  ykeys: ['value'],
  // Labels for the ykeys -- will be displayed when you hover over the
  // chart.
  labels: ['Consumption (mins)'],
  barColors: ['#337AB7'],
  resize: true,
  gridTextSize: 12,
  
});