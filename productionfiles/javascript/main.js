window.onload = function () {
    var charts = []
    var axisX = {
        labelFormatter: function () {
          return ""
        },
        tickLength: 0,
        lineThickness: 0,
      },
      
      axisY = {
        labelFormatter: function () {
          return ""
        },
        tickLength: 0,
        gridThickness: 0,
      }
  
    var newUserOptions = {
      animationEnabled: true,
      theme: "light2",
      title: {
        text: "New Users",
        fontSize: 18,
        verticalAlign: "bottom",
      },
      axisX: axisX,
      axisY: axisY,
      data: [
        {
          type: "splineArea", //change type to bar, line, area, pie, etc
          markerSize: 0,
          dataPoints: [
            { x: new Date(2018, 00, 01), y: 74553 },
            { x: new Date(2018, 01, 01), y: 75374 },
            { x: new Date(2018, 02, 01), y: 76065 },
            { x: new Date(2018, 03, 01), y: 76521 },
            { x: new Date(2018, 04, 01), y: 76695 },
            { x: new Date(2018, 05, 01), y: 76381 },
            { x: new Date(2018, 06, 01), y: 76693 },
            { x: new Date(2018, 07, 01), y: 75624 },
            { x: new Date(2018, 08, 01), y: 76367 },
            { x: new Date(2018, 09, 01), y: 75426 },
            { x: new Date(2018, 10, 01), y: 76024 },
            { x: new Date(2018, 11, 01), y: 75960 },
          ],
        },
      ],
    }
    var bounceRateOptions = {
      animationEnabled: true,
      theme: "light2",
      title: {
        text: "Bounce Rate",
        fontSize: 18,
        verticalAlign: "bottom",
      },
      axisX: axisX,
      axisY: axisY,
      data: [
        {
          type: "splineArea", //change type to bar, line, area, pie, etc
          markerSize: 0,
          yValueFormatString: "#.##%",
          dataPoints: [
            { x: new Date(2018, 00, 01), y: 0.4731 },
            { x: new Date(2018, 01, 01), y: 0.4743 },
            { x: new Date(2018, 02, 01), y: 0.476 },
            { x: new Date(2018, 03, 01), y: 0.4751 },
            { x: new Date(2018, 04, 01), y: 0.4757 },
            { x: new Date(2018, 05, 01), y: 0.4761 },
            { x: new Date(2018, 06, 01), y: 0.4768 },
            { x: new Date(2018, 07, 01), y: 0.4771 },
            { x: new Date(2018, 08, 01), y: 0.4773 },
            { x: new Date(2018, 09, 01), y: 0.4764 },
            { x: new Date(2018, 10, 01), y: 0.4757 },
            { x: new Date(2018, 11, 01), y: 0.4751 },
          ],
        },
      ],
    }
  
    var pageViewsOptions = {
      animationEnabled: true,
      theme: "light2",
      title: {
        text: "Page Views",
        fontSize: 18,
        verticalAlign: "bottom",
      },
      axisX: axisX,
      axisY: axisY,
      data: [
        {
          type: "splineArea", //change type to bar, line, area, pie, etc
          markerSize: 0,
          dataPoints: [
            { x: new Date(2018, 00, 01), y: 897533 },
            { x: new Date(2018, 01, 01), y: 898699 },
            { x: new Date(2018, 02, 01), y: 900047 },
            { x: new Date(2018, 03, 01), y: 900348 },
            { x: new Date(2018, 04, 01), y: 900678 },
            { x: new Date(2018, 05, 01), y: 900407 },
            { x: new Date(2018, 06, 01), y: 900946 },
            { x: new Date(2018, 07, 01), y: 901937 },
            { x: new Date(2018, 08, 01), y: 902117 },
            { x: new Date(2018, 09, 01), y: 901936 },
            { x: new Date(2018, 10, 01), y: 903288 },
            { x: new Date(2018, 11, 01), y: 903107 },
          ],
        },
      ],
    }
  
    var visitorsOptions = {
      animationEnabled: true,
      theme: "light2", // "light1", "light2", "dark1", "dark2"
      title: {
        text: "Total Website Visitors",
      },
      axisY: {
        labelFormatter: addSymbols,
      },
      data: [
        {
          type: "column", //change type to bar, line, area, pie, etc
          color: "#6D78AD",
          dataPoints: [
            { x: new Date(2018, 00, 01), y: 130796 },
            { x: new Date(2018, 01, 01), y: 131774 },
            { x: new Date(2018, 02, 01), y: 132750 },
            { x: new Date(2018, 03, 01), y: 132850 },
            { x: new Date(2018, 04, 01), y: 133384 },
            { x: new Date(2018, 05, 01), y: 132607 },
            { x: new Date(2018, 06, 01), y: 132687 },
            { x: new Date(2018, 07, 01), y: 132443 },
            { x: new Date(2018, 08, 01), y: 133044 },
            { x: new Date(2018, 09, 01), y: 132095 },
            { x: new Date(2018, 10, 01), y: 132446 },
            { x: new Date(2018, 11, 01), y: 131648 },
          ],
        },
      ],
    }
  
    charts.push(new CanvasJS.Chart("chartContainer1", visitorsOptions))
    charts.push(new CanvasJS.Chart("chartContainer2", newUserOptions))
    charts.push(new CanvasJS.Chart("chartContainer3", pageViewsOptions))
    charts.push(new CanvasJS.Chart("chartContainer4", bounceRateOptions))
    syncTooltip(charts)
  
    for (var i = 0; i < charts.length; i++) {
      charts[i].render()
    }
  
    function syncTooltip(charts) {
      if (!this.onToolTipUpdated) {
        this.onToolTipUpdated = function (e) {
          for (var j = 0; j < charts.length; j++) {
            if (charts[j] != e.chart)
              charts[j].toolTip.showAtX(e.entries[0].xValue)
          }
        }
      }
  
      if (!this.onToolTipHidden) {
        this.onToolTipHidden = function (e) {
          for (var j = 0; j < charts.length; j++) {
            if (charts[j] != e.chart) charts[j].toolTip.hide()
          }
        }
      }
  
      for (var i = 0; i < charts.length; i++) {
        if (!charts[i].options.toolTip) charts[i].options.toolTip = {}
  
        charts[i].options.toolTip.updated = this.onToolTipUpdated
        charts[i].options.toolTip.hidden = this.onToolTipHidden
      }
    }
  
    function addSymbols(e) {
      var suffixes = ["", "K", "M", "B"]
  
      var order = Math.max(
        Math.floor(Math.log(Math.abs(e.value)) / Math.log(1000)),
        0,
      )
      if (order > suffixes.length - 1) order = suffixes.length - 1
  
      var suffix = suffixes[order]
      return CanvasJS.formatNumber(e.value / Math.pow(1000, order)) + suffix
    }
  }
  