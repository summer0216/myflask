require.config({
    baseUrl:'/static/js',
    paths: {
        'angular':'lib/angular-1.3.0',
        text: 'lib/text',
        domReady: 'lib/domReady',
        css: 'lib/css',
        jquery: 'lib/jquery-2.1.1.min',
        bootstrap: 'lib/bootstrap.min',
    },
    shim: {
        'angular' : {'exports' : 'angular'},
        bootstrap: ['jquery']
    },
    urlArgs: "bust=" +  (new Date()).getTime()
});
