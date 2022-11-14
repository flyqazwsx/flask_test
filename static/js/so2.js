let chart2 = echarts.init(document.querySelector("#so2"));

$(document).ready(() => {
    so2();
});

window.onresize = function () {
    chart2.resize();
};





function so2() {
    chart2.showLoading();
    $.ajax(
        {
            url: "/data-so2",
            type: "GET",
            dataType: "json",
            success: (data) => {
                chart2.hideLoading();
                drawChart(data["sitename"], data["so2"], "二氧化硫", chart2, "#8b008b");
            },
            error: () => {
                chart2.hideLoading();
                alert("讀取資料失敗!");
            }
        }
    );
};





function drawChart(xdata, ydata, title = "", chart = null, color = "#00008b") {
    // 指定图表的配置项和数据
    let option = {
        title: {
            text: title
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'left',
            top: 'center',
            feature: {
                magicType: { show: true, type: ['line', 'bar', 'tiled'] },
                restore: { show: true },
                saveAsImage: { show: true }
            }
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: ['so2']
        },
        xAxis: {
            data: xdata,
            axisLabel: {
                inside: true,
                color: '#000000'
            },
            axisTick: {
                show: false
            },
            axisLine: {
                show: false
            },
            z: 10
        },

        yAxis: {
            axisLine: {
                show: false
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                color: '#999'
            }
        },
        dataZoom: [
            {
                type: 'inside'
            },
        ],
        series: [
            {

                type: 'bar',
                showBackground: true,
                itemStyle: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                        { offset: 0, color: '#83bff6' },
                        { offset: 0.5, color: '#188df0' },
                        { offset: 1, color: '#188df0' }
                    ])
                },
                emphasis: {
                    itemStyle: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                            { offset: 0, color: '#2378f7' },
                            { offset: 0.7, color: '#2378f7' },
                            { offset: 1, color: '#83bff6' }
                        ])
                    }
                },
                data: ydata
            }
        ]
    };

    chart.setOption(option);

};
