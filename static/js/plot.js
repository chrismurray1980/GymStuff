/* global dc , d3 , crossfilter , $ */


// Import macro plot data from HTML 
var macros_json_parsed = JSON.parse($('#macro_weight_data').html());

// Macro plot names 
const macro_weight_chart = new dc.BarChart('#macro-weight-chart');
const macro_percentage_chart = new dc.PieChart('#macro-percentage-chart');

// Macro data Crossfilter 
var macro= crossfilter([
   {name: "Carbs", grams: macros_json_parsed[0], percentage: macros_json_parsed[3]},
   {name: "Proteins", grams: macros_json_parsed[1], percentage: macros_json_parsed[4]},
   {name: "Fats", grams: macros_json_parsed[2], percentage: macros_json_parsed[5]}
]);

// Dimension //
var macro_dimension =  macro.dimension(function (d) { return d["name"]; });

// Groups //
var macro_weight_group = macro_dimension.group().reduceSum(function (d) { return d["grams"]; });
var macro_percentage_group = macro_dimension.group().reduceSum(function (d) { return d["percentage"]; });

// Color variable //
var macro_colors = d3.scaleOrdinal()
        .domain(["Carbs", "Proteins", "Fats"])
        .range(["blue", "red", "green"]);

// Create weight plot //        
macro_weight_chart
    .height( 250 )
    .width( 500 )
    .margins( { top: 10, right: 50, bottom: 50, left: 50 } )
    .dimension( macro_dimension )
    .group( macro_weight_group )
    .transitionDuration( 500 )
    .colorAccessor(function (d) { return d.key[3]; })
    .colors(macro_colors)
    .x( d3.scaleBand() )
    .xUnits( dc.units.ordinal )
    .xAxisLabel( 'Macronutrient' )
    .yAxisLabel( 'Daily macro weight (g)' )
    .yAxis()
    .ticks( 10 );

// Create percentage plot //        
macro_percentage_chart
   .width( 250 )
    .height( 250 )
    .dimension( macro_dimension )
    .group( macro_percentage_group )
    .colorAccessor(function (d) { return d.key[3]; })
    .colors(macro_colors)
    .label(function(d) {
    return d.key + ' ' + d.value + '%';});
    /*.height( 250 )
    .width( 500 )
    .margins( { top: 10, right: 50, bottom: 50, left: 50 } )
    .dimension( macro_dimension )
    .group( macro_percentage_group)
    .transitionDuration( 500 )
    .colorAccessor(function (d) { return d.key[3]; })
    .colors(macro_colors)*/
    //.x( d3.scaleBand() )
    //.xUnits( dc.units.ordinal )
    //.xAxisLabel( 'Macronutrient' )
    //.yAxisLabel( 'Daily macro weight (g)' )
    //.yAxis()
    //.ticks( 10 );
    
// Render all plots //
dc.renderAll();