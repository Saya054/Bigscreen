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
                        "name": "呼入数量"
                    },
                    {
                        "name": "呼入接通数"
                    },
                    {
                        "name": "接听率"
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

                data: ['BLG', 'VG', 'FPX', 'EDG', 'RNG', 'LGD', 'WE', 'SN', 'IG', 'V5', 'JDG', 'TES'],
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
                    "name": "次数",
                    "min": 0,
                    "interval": 10,
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
                    "name": "胜率",
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
                    "name": "Victory",

                    "type": "bar",
                    "data": [17, 19, 23, 20, 21, 29, 25, 31, 26, 30, 33, 33],
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
                    "name": "Defeat",
                    "type": "bar",
                    "data": [
                        22, 22, 22, 18, 18, 25, 22, 21, 18, 19, 15, 12
                    ],
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
                    "name": "胜率",
                    "type": "line",
                    "yAxisIndex": 1,

                    "data": [43, 46, 51, 52, 53, 53, 53, 59, 59, 61, 68, 73],
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

    function echarts_5() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('echart5'));
        var option = {
            tooltip: {
                trigger: 'axis',
                axisPointer: { // 坐标轴指示器，坐标轴触发有效
                    type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
                }
            },
            legend: {
                data: ['出场次数', '总击杀', '总助攻', '总死亡', ],
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
                data: ['WeJiumeng', 'LGDxiye', 'TESknight', 'JDGKanavi', 'JackeyLove', 'SNSofM', 'V5Mole', 'EDGScout', 'SNhuanfeng', 'FPXDoinb']
            },
            series: [{
                    name: '出场次数',
                    type: 'bar',
                    stack: '总量',
                    itemStyle: {
                        color: '#37A2DA'
                    },
                    label: {
                        show: false,
                        position: 'insideRight'
                    },
                    data: [47, 52, 44, 48, 42, 52, 49, 37, 52, 45]
                },
                {
                    name: '总击杀',
                    type: 'bar',
                    stack: '总量',
                    itemStyle: {
                        color: '#67E0E3'
                    },
                    label: {
                        show: false,
                        position: 'insideRight'
                    },
                    data: [205, 191, 239, 169, 205, 125, 162, 136, 189, 157]
                },
                {
                    name: '总助攻',
                    type: 'bar',
                    stack: '总量',
                    itemStyle: {
                        color: '#FFDB5C'
                    },
                    label: {
                        show: false,
                        position: 'insideRight'
                    },
                    data: [266, 289, 299, 345, 278, 375, 270, 286, 315, 304]
                },
                {
                    name: '总死亡',
                    type: 'bar',
                    stack: '总量',
                    itemStyle: {
                        color: '#FF9F7F'
                    },
                    label: {
                        show: false,
                        position: 'insideRight'
                    },
                    data: [119, 124, 76, 122, 117, 136, 115, 73, 102, 115]
                },

            ]
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function() {
            myChart.resize();
        });
    }

    function zb1() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb1'));
        var v2 = 33 //胜利
        var v1 = 12 //战败
        var v3 = v1 + v2 //总消费 
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
                    name: '胜利',
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
                    value: v1,
                    name: '战败',
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '胜率' + Math.round(v2 / v3 * 100) + '%'
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

    function zb2() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb2'));
        var v1 = 738 //总击杀
        var v2 = 542 //总死亡
        var v3 = v1 + v2 //
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
                    name: '总击杀',
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
                    name: '总死亡',
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '总击杀'
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

    function zb3() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb3'));
        var v1 = 51 //排眼
        var v2 = 121 //插眼
        var v3 = v1 + v2 //总消费 
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
                    value: v2,
                    name: '插眼',
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
                    value: v1,
                    name: '排眼',
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '总插眼'
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

    function zb4() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb4'));
        var v1 = 76 //死亡
        var v2 = 239 //击杀
        var v3 = v1 + v2

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
                    name: '击杀',
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
                    value: v1,
                    name: '死亡',
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '总击杀'
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

    function zb5() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb5'));
        var v1 = 348 //助攻和击杀
        var v2 = 165 //死亡
        var v3 = v1 + v2 //总消费
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
                    value: v2,
                    name: '总死亡',
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
                    value: v1,
                    name: '击杀和助攻',
                    label: {
                        normal: {
                            formatter: function(params) {
                                return '总死亡'
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

    function zb6() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('zb6'));
        var k = 19;
        var a = 34;
        var d = 7;
        var v1 = d //死亡
        var v2 = k + a //击杀和助攻
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
                    value: v2,
                    name: '击杀和助攻',
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
                    value: v1,
                    name: '死亡',
                    label: {
                        normal: {
                            formatter: function(params) {
                                return 'KDA：' + Math.round((k + a) / d)
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
})