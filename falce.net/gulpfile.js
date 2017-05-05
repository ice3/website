require('es6-promise').polyfill();

var gulp = require('gulp');
var uncss = require('gulp-uncss');
var cssmin = require('gulp-cssmin');
var rename = require('gulp-rename');

gulp.task('default', ['bootstrap_css', 'fontawesome_css']);

gulp.task('bootstrap_css', function() {
    gulp.src('html/assets/bootstrap-3.3.5-dist/css/bootstrap.css')
        .pipe(uncss({
            html: ['./html/index.html', './html/presentation/index.html']
        }))
        .pipe(cssmin())
        .pipe(gulp.dest('html/assets/bootstrap-3.3.5-dist/uncss/'));
});

gulp.task('fontawesome_css', function() {
    gulp.src('html/assets/font-awesome-4.4.0/css/font-awesome.css')
        .pipe(uncss({
            html: ['./html/index.html', './html/presentation/index.html']
        }))
        .pipe(cssmin())
        .pipe(gulp.dest('html/assets/font-awesome-4.4.0/uncss/'));
});