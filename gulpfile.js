var gulp = require('gulp');
var uncss = require('gulp-uncss');
var cssmin = require('gulp-cssmin');
var rename = require('gulp-rename');
var debug = require('gulp-debug');

var base = "matthieu.falce.net";

gulp.task('default',
         ['bootstrap_css', 'fontawesome_css', 'main_css']
    );

gulp.task('bootstrap_css', function() {
    gulp.src(base+'/html/assets/bootstrap-3.3.5-dist/css/bootstrap.css')
        .pipe(uncss({
            html: [base+'/html/index.html']
        }))
        .pipe(cssmin())
        .pipe(gulp.dest(base+'/html/assets/bootstrap-3.3.5-dist/uncss/'));
});

gulp.task('fontawesome_css', function() {
    gulp.src(base+'/html/assets/font-awesome-4.4.0/css/font-awesome.css')
        .pipe(uncss({
            html: [base+'/html/index.html']
        }))
        .pipe(cssmin())
        .pipe(gulp.dest(base+'/html/assets/font-awesome-4.4.0/uncss/'));
});

gulp.task('main_css', function() {
    gulp.src(base+'/html/assets/css/main.css')
        .pipe(uncss({
            html: [base+'/html/index.html']
        }))
        .pipe(cssmin())
        .pipe(gulp.dest(base+'/html/assets/uncss'));
});