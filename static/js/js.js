$(window).load(function() {
    $(".loading").fadeOut()
})
$(function() {
    echarts_4();
    echarts_5();
    zb1();
    zb2();
    zb3();
    zb4();
    zb5();
    zb6();

    function echarts_4() {
        // $('#echart4').children().remove();
          $.ajax({
                 url: "/webimweek",
                 success: function (data) {
                     var barlineinfo = data;
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart4'));
        option = {
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    lineStyle: {
                        color: '#57617B'
                    }
                }
            },
            "legend": {

                "data": [{
                        "name": "IM总对话量"
                    },
                    {
                        "name": "IM有效对话量"
                    },
                    {
                        "name": "有效服务率"
                    }
                ],
                "top": "0%",
                "textStyle": {
                    "color": "rgba(255,255,255,1)", //图例文字
                    "fontSize": "16"
                }
            },

            "xAxis": [{
                "type": "category",

                data:barlineinfo[0],
                axisLine: {
                    lineStyle: {
                        color: "rgba(255,255,255,.1)"
                    }
                },
                axisLabel: {
                    textStyle: {
                        color: "rgb(255,255,255)",
                        fontSize: '16',
                    },
                },

            }, ],
            "yAxis": [{
                    "type": "value",
                    "name": "对话数",
                    "min": 0,
                    "interval": 50,
                    "axisLabel": {
                        "show": true,

                    },
                    axisLine: {
                        lineStyle: {
                            color: 'rgba(255,255,255,1)'
                        }
                    }, //左线色
                    splitLine: {
                        show: true,
                        lineStyle: {
                            color: "rgba(255,255,255,0.5)"
                        }
                    }, //x轴线
                },
                {
                    "type": "value",
                    "name": "有效服务率",
                    "show": true,
                    "axisLabel": {
                        "show": true,

                    },
                    axisLine: {
                        lineStyle: {
                            color: 'rgba(255,255,255,1 )'
                        }
                    }, //右线色
                    splitLine: {
                        show: true,
                        lineStyle: {
                            color: "rgba(255,255,255,0.2)"
                        }
                    }, //x轴线
                },
            ],
            "grid": {
                "top": "10%",
                "right": "30",
                "bottom": "30",
                "left": "30",
            },
            "series": [{
                    "name": "IM总对话量",

                    "type": "bar",
                    "data": barlineinfo[1],
                    "barWidth": "auto",
                    "itemStyle": {
                        "normal": {
                            "color": {
                                "type": "linear",
                                "x": 0,
                                "y": 0,
                                "x2": 0,
                                "y2": 1,
                                "colorStops": [{
                                        "offset": 0,
                                        "color": "#67E0E3"
                                    },

                                    {
                                        "offset": 1,
                                        "color": "#67E0E3"
                                    }
                                ],
                                "globalCoord": false
                            }
                        }
                    }
                },
                {
                    "name": "IM有效对话量",
                    "type": "bar",
                    "data": barlineinfo[2],
                    "barWidth": "auto",

                    "itemStyle": {
                        "normal": {
                            "color": {
                                "type": "linear",
                                "x": 0,
                                "y": 0,
                                "x2": 0,
                                "y2": 1,
                                "colorStops": [{
                                        "offset": 0,
                                        "color": "#FFDB5C"
                                    },
                                    {
                                        "offset": 1,
                                        "color": "#FFDB5C"
                                    }
                                ],
                                "globalCoord": false
                            }
                        }
                    },
                    "barGap": "0"
                },
                {
                    "name": "有效服务率",
                    "type": "line",
                    "yAxisIndex": 1,

                    "data": barlineinfo[3],
                    lineStyle: {
                        normal: {
                            width: 2
                        },
                    },
                    "itemStyle": {
                        "normal": {
                            "color": "#48f593",

                        }
                    },
                    "smooth": true
                }
            ]
        };


        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function() {
            myChart.resize();
        });
    }
          });
    }
     setInterval(echarts_4, 30000);
    function echarts_5() {
        // 基于准备好的dom，初始化echarts实例
        //  $('#echart5').children().remove();
          $.ajax({
                 url: "/hotline",
                 success: function (data) {
                     var barinfo = data;
        var myChart = echarts.init(document.getElementById('echart5'));
        var option = {
            tooltip: {
                trigger: 'axis',
                axisPointer: { // 坐标轴指示器，坐标轴触发有效
                    type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
                }
            },
            legend: {
                data: ['呼入接通数', '满意评价数', '不满意评价数'],
                textStyle: {
                    color: 'skyblue'
                }
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: {
                type: 'value',
                axisLine: {
                    lineStyle: {
                        color: 'rgba(255,255,255,1)'
                    }
                }, //左线色
            },
            yAxis: {
                type: 'category',
                axisLine: {
                    lineStyle: {
                        color: 'rgba(255,255,255,1)'
                    }
                }, //左线色
                splitLine: {
                    show: true,
                    lineStyle: {
                        color: "rgba(255,255,255,.1)"
                    }
                }, //x轴线
                data: barinfo[0]
            },
            series: [{
                    name: '呼入接通数',
                    type: 'bar',
                    stack: '总量',
                    itemStyle: {
                        color: '#37A2DA'
                    },
                    label: {
                        show: false,
                        position: 'insideRight'
                    },
                    data: barinfo[1]
                },
                {
                    name: '满意评价数',
                    type: 'bar',
                    stack: '总量',
                    itemStyle: {
                        color: '#67E0E3'
                    },
                    label: {
                        show: false,
                        position: 'insideRight'
                    },
                    data: barinfo[2]
                },
                {
                    name: '不满意评价数',
                    type: 'bar',
                    stack: '总量',
                    itemStyle: {
                        color: '#FFDB5C'
                    },
                    label: {
                        show: false,
                        position: 'insideRight'
                    },
                    data:barinfo[3]
                },
            ]
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function() {
            myChart.resize();
           });
    }
          });
    }
 setInterval(echarts_5, 30000);
    function zb1() {
        // 基于准备好的dom，初始化echarts实例
          $.ajax({
                 url: "/topkpi",
                 success: function (data) {
                     $('#zb1title').empty();
                     var pieinfo = data;
                    var myChart = echarts.init(document.getElementById('zb1'));
                    var tilte =pieinfo[0]+"<br/>绩效完成率最高";
                    var v2 = pieinfo[1] ;//已经完成
                    var v1 = pieinfo[2]-pieinfo[1]; //未完成
                    var v3 = pieinfo[2];//总完成;
                     var v4 = pieinfo[3];//完成率
                   $('#zb1title').append(tilte);
        option = {
            tooltip: {
                trigger: 'item',
            },
            series: [{

                type: 'pie',
                radius: ['60%', '70%'],
                color: '#37A2DA',
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: v2,
                    name: '已完成',
                    label: {
                        normal: {
                            formatter: v4 + '%',
                            textStyle: {
                                fontSize: 20,
                                color: '#fff',
                            }
                        }
                    }
                }, {
                    value: v1,
                    name: '未完成',
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '完成率'
                            },
                            textStyle: {
                                color: '#aaa',
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: 'rgba(255,255,255,.2)'
                        },
                        emphasis: {
                            color: '#fff'
                        }
                    },
                }]
            }]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function() {
            myChart.resize();
        });
    }
   });
    }
 setInterval(zb1, 10000);
    function zb2() {
          $.ajax({
                 url: "/tophotline",
                 success: function (data) {
                     $('#zb2title').empty();
                     var pieinfo = data;
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb2'));
        var title = pieinfo[0]+"<br/>热线接听数量最高";
        var v1 = pieinfo[1] //呼入数
        var v2 = pieinfo[2]-pieinfo[1]  //未接通数
        var v3 = v1 + v2 //
                     $('#zb2title').append(title);
        option = {

            tooltip: {
                trigger: 'item',
            },
            series: [{
                type: 'pie',
                radius: ['60%', '70%'],
                color: '#32C5E9',
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: v1,
                    name: '呼入接通数',
                    label: {
                        normal: {
                            formatter: v1 + '',
                            textStyle: {
                                fontSize: 20,
                                color: '#fff',
                            }
                        }
                    }
                }, {
                    value: v2,
                    name: '呼入未接通数',
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '呼入接通数'
                            },
                            textStyle: {
                                color: '#aaa',
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: 'rgba(255,255,255,.2)'
                        },
                        emphasis: {
                            color: '#fff'
                        }
                    },
                }]
            }]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function() {
            myChart.resize();
        });
    }
    });
    }
 setInterval(zb2, 10000);

    function zb3() {
         $.ajax({
                 url: "/topissue",
                 success: function (data) {
                     $('#zb3title').empty();
                     var pieinfo = data;
        // 基于准备好的dom，初始化echarts实例
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb3'));
          var title = pieinfo[0]+"<br/>支持网答复最高";
        var v1 = pieinfo[1]; //答复数
        // var v2 = 0 //答复数
        // var v3 = v1 + v2 //总消费
        $('#zb3title').append(title);
        option = {
            tooltip: {
                trigger: 'item',
            },
            series: [{

                type: 'pie',
                radius: ['60%', '70%'],
                color: '#67E0E3',
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: v1,
                    name: '答复数',
                    label: {
                        normal: {
                            formatter: v1 + '',
                            textStyle: {
                                fontSize: 20,
                                color: '#fff',
                            }
                        }
                    }
                }, {
                    value: 0,
                    name: '其他',
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '答复数'
                            },
                            textStyle: {
                                color: '#aaa',
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: 'rgba(255,255,255,.2)'
                        },
                        emphasis: {
                            color: '#fff'
                        }
                    },
                }]
            }]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function() {
            myChart.resize();
        });
    }
     });
    }
 setInterval(zb3, 10000);
    function zb4() {
        $.ajax({
                 url: "/topstudy",
                 success: function (data) {
                     $('#zb4title').empty();
                     var pieinfo = data;
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb4'));
        var title = pieinfo[0]+"<br/>季度学习成长最高";
        var v1 = pieinfo[1] ;//
        var v2 = pieinfo[1];//无效答复
        // var v3 = pieinfo[2];//有效答复
         $('#zb4title').append(title);
        option = {
            tooltip: {
                trigger: 'item',
            },
            series: [{

                type: 'pie',
                radius: ['60%', '70%'],
                color: '#9FE6B8',
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: v2,
                    name: '学习成长',
                    label: {
                        normal: {
                            formatter: v2 + '',
                            textStyle: {
                                fontSize: 20,
                                color: '#fff',
                            }
                        }
                    }
                }, {
                    value: 0,
                    name: '其他',
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '学习成长'
                            },
                            textStyle: {
                                color: '#aaa',
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: 'rgba(255,255,255,.2)'
                        },
                        emphasis: {
                            color: '#fff'
                        }
                    },
                }]
            }]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function() {
            myChart.resize();
        });
    }
    });
    }
 setInterval(zb4, 10000);

    function zb5() {
         $.ajax({
                 url: "/topcommunity",
                 success: function (data) {
                     $('#zb5title').empty();
                     var pieinfo = data;
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb5'));
         var title = pieinfo[0]+"<br/>社区答复楼层最多";
        var v1 = pieinfo[1]; //楼层
        // var v2 = 0; //死亡
        // var v3 = v1 + v2 ;//总消费
        $('#zb5title').append(title)
        option = {
            tooltip: {
                trigger: 'item',
            },
            series: [{

                type: 'pie',
                radius: ['60%', '70%'],
                color: '#FFDB5C',
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: v1,
                    name: '社区回复楼层',
                    label: {
                        normal: {
                            formatter: v1 + '',
                            textStyle: {
                                fontSize: 20,
                                color: '#fff',
                            }
                        }
                    }
                }, {
                    value: 0,
                    name: '其他',
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '社区回复楼层'
                            },
                            textStyle: {
                                color: '#aaa',
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: 'rgba(255,255,255,.2)'
                        },
                        emphasis: {
                            color: '#fff'
                        }
                    },
                }]
            }]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function() {
            myChart.resize();
        });
    }
    });
    }
 setInterval(zb5, 10000);


    function zb6() {
         $.ajax({
                 url: "/topwebim",
                 success: function (data) {
                     $('#zb6title').empty();
                     var pieinfo = data;
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb6'));
         var title = pieinfo[0]+"<br/>IM有效答复数最多";
        var v1 = pieinfo[1] ;//有效答复数
        // var v2 =pieinfo[1]-pieinfo[2]; //无效答复数
        // var v3 = pieinfo[1];
         $('#zb6title').append(title);
        option = {
            tooltip: {
                trigger: 'item',
            },
            series: [{

                type: 'pie',
                radius: ['60%', '70%'],
                color: '#FB7293',
                label: {
                    normal: {
                        position: 'center'
                    }
                },
                data: [{
                    value: v1,
                    name: '有效答复数',
                    label: {
                        normal: {
                            formatter: v1 + '',
                            textStyle: {
                                fontSize: 20,
                                color: '#fff',
                            }
                        }
                    }
                }, {
                    value: 0,
                    name: '其他',
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '有效答复数'
                            },
                            textStyle: {
                                color: '#aaa',
                                fontSize: 12
                            }
                        }
                    },
                    itemStyle: {
                        normal: {
                            color: 'rgba(255,255,255,.2)'
                        },
                        emphasis: {
                            color: '#fff'
                        }
                    },
                }]
            }]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function() {
            myChart.resize();
        });
    }
    });
    }
 setInterval(zb6, 10000);
})
