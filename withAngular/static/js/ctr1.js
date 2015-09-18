/**
 * Created by lewis on 15-9-15.
 */
define(['app'], function (app) {
    'use strict';
    app.controller('ctr1', function ($scope) {
        $scope.list = appData.list
    });
    console.log('c1执行完成！')
});