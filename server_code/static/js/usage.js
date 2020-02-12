 $(function () {
      /*
     * BAR CHART
     * ---------
     */
    var receivedData = {{usage}};
    alert(receivedData);
    var bar_data = {
      data : [['bad ball joint', receivedData[0]],
      ['bad brake pad', receivedData[1]],
      ['engine running without oil+engine seizing up', receivedData[2]],
      ['failing water pump', receivedData[3]],
      ['hole in muffler', receivedData[4]],
      ['normal', receivedData[5]]],
      color: '#3c8dbc'
    }
    $.plot('#bar-chart', [bar_data], {
      grid  : {
        borderWidth: 1,
        borderColor: '#f3f3f3',
        tickColor  : '#f3f3f3'
      },
      series: {
        bars: {
          show    : true,
          barWidth: 0.5,
          align   : 'center'
        }
      },
      xaxis : {
        mode      : 'categories',
        tickLength: 0
      }
    })
    /* END BAR CHART */

    /*
     * DONUT CHART
     * -----------
     */
    var donutData = [
      { label: '', data: receivedData[0], color: '#56a0f0' },
      { label: '', data: receivedData[1], color: '#0073b7' },
      { label: '', data: receivedData[2], color: '#56c4f0' },
      { label: '', data: receivedData[3], color: '#414c9a' },
      { label: '', data: receivedData[4], color: '#6756f0' },
      { label: '', data: receivedData[5], color: '#9f56f0' }
    ]
    $.plot('#donut-chart', donutData, {
      series: {
        pie: {
          show       : true,
          radius     : 1,
          innerRadius: 0.5,
          label      : {
            show     : true,
            radius   : 2 / 3,
            formatter: labelFormatter,
            threshold: 0.1
          }

        }
      },
      legend: {
        show: false
      }
    })
    /*
     * END DONUT CHART
     */

  })

  /*
   * Custom Label formatter
   * ----------------------
   */
  function labelFormatter(label, series) {
    return '<div style="font-size:13px; text-align:center; padding:2px; color: #fff; font-weight: 600;">'
      + label
      + '<br>'
      + Math.round(series.percent) + '%</div>'
  }
