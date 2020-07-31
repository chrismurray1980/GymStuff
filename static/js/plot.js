/* global dc , d3 , crossfilter , $ */

// Create plot variable names

var IMCcat = [
        {color:'#F43E3E',min:40,max:200,name:'obésité morbide ou massive'},
        {color:'#F4B4B4',min:35,max:40,name:'obésité sévère'},
        {color:'#FAE9CA',min:30,max:35,name:'obésité modérée'},
        {color:'#FFFFD4',min:25,max:30,name:'surpoids'},
        {color:'#E9FFDA',min:18.5,max:25,name:'corpulence normale'},
        {color:'#FFFFD4',min:16.5,max:18.5,name:'maigreur'},
        {color:'#F43E3E',min:0,max:16.5,name:'famine'}
    ];
    
//reverse array so BMI is ascending 
IMCcat = IMCcat.reverse();

//create scale
var scale = d3.scale.threshold('bum');
  //set the domain equal to the min weights, w/ lowest removed
  scale.domain(IMCcat.map(function(d){ return d.min; }).slice(1)).range(IMCcat.map(function(d){ return d.color; }));

// render all charts on page
dc.renderAll(); 