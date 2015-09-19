/**
 * Created by lewis on 15-9-15.
 */
define(['app'], function (app) {
    'use strict';
    app.controller('ctr_app', function ($scope) {
        $scope.url='/tpl3/';
        $scope.toggleUrl= function () {
            $scope.url= $scope.url=='/tpl3/'?'/tpl4/':'/tpl3/';
        }
    });
    console.log('ctr_app执行完成！')
});