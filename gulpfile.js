'use strict';

var gulp = require('gulp');
var pug = require('gulp-pug');
var rename = require("gulp-rename");
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var autoprefixer = require('gulp-autoprefixer');
var todo = require('gulp-todo');
var browserSync = require('browser-sync');
var concat = require('gulp-concat');
var config = require('./gulpfile_config.json');

gulp.task('pug', () => {
	gulp.src(config.pug.src)
	.pipe(pug(config.pug.plugin))
	.pipe(rename(config.pug.rename))
	.pipe(gulp.dest(config.pug.dest))
});

gulp.task('styles', () => {
	gulp.src(config.sass.src)
	.pipe(sourcemaps.init())
		.pipe(sass(config.sass.plugin).on('error', sass.logError))
		.pipe(autoprefixer(config.sass.autoprefixer))
	.pipe(sourcemaps.write(''))
	.pipe(gulp.dest(config.sass.dest));
});

gulp.task('scripts', () => {
	return gulp.src(config.scripts.src)
	.pipe(concat('scripts.js'))
	.pipe(gulp.dest(config.scripts.dest));
});

gulp.task('todo', () => {
	gulp.src(config.todo.src)
	.pipe(todo(config.todo.plugin))
	.pipe(gulp.dest(config.todo.dest));
});

gulp.task('build', ['pug', 'styles', 'scripts']);

gulp.task('reload', (done) => {
	browserSync.reload();
	done();
});

// The default task (called when you run `gulp` from cli)
gulp.task('default', ['build'], () => {
	browserSync.init(config.server);
	gulp.watch(config.pug.watch, ['pug', 'reload']);
	gulp.watch(config.sass.watch, ['styles', 'reload']);
	gulp.watch(config.scripts.watch, ['scripts', 'reload']);
});
