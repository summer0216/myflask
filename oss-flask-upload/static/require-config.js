require.config({
    baseUrl:'/static/js',
    paths: {
        'angular':'lib/angular.min',
        text: 'lib/text',
        domReady: 'lib/domReady',
        css: 'lib/css',
        jquery: 'lib/jquery-2.1.1.min',
        bootstrap: 'lib/bootstrap.min',
    },
    map: { '*': { 'css': '/static/js/lib/css.js' } } ,
    shim: {
        'angular' : {'exports' : 'angular'},
        bootstrap: ['jquery']
    },
    urlArgs: "bust=" +  (new Date()).getTime()
});
