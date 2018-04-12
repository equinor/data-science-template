# Reporting
This folder contains a basic flask template for an app that displays content including Plotly interactive graphs either embedded or hosted online.

## Instructions for use
The files are under webapp. app.py is the main entry point and will server up the template file index.html. Both these files should be customised as needed. You can choose to embed html to display static images or have this generated from python code. The default template uses tabs to swap between content. You can and expand upon the sample to serve multiple pages if so desired. This might be necessary for grouping content or with high memory content.

To run the flask app, change to teh webapp folder and type:

```
python app.py
```

A url should be printed to which you can browse.

### Graph Templates ###
HTML can be embedded into files in the Graph folder. These will be read in and available for embedding as named variables within the template file. Please ensure that you match the file and variable names correctly.

Note that when using embedded Plotly images you should ensure that the div id elements are unique and match with the contained Plotly.newPlot() parameter. If you notice plots not showing up then this coule be the reason.  
