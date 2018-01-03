'use strict';

import path from 'path';
import del from 'del';
import gulpIf from 'gulp-if';
import vinylPaths from 'vinyl-paths';
import concat from 'gulp-concat';
import gulp from 'gulp';
import sass from 'gulp-sass';
import sourcemaps from 'gulp-sourcemaps';
import autoprefixer from 'gulp-autoprefixer';
import pug from 'gulp-pug';
import browserSync from 'browser-sync';
import todo from 'gulp-todo';

import {config, onChange} from './gulpfile.config';

const server = browserSync.create();
const styles = config.styles;
const html = config.html;
const todolist = config.todolist;
const scripts = config.scripts;
const fonts = config.fonts;
const images = config.images;

const DEV_DIR = config.dev_dir;
const BUILD_DIR = config.build_dir;

gulp.task('build:styles', () => {
	gulp.src(path.join(DEV_DIR, styles.src))
	.pipe(sourcemaps.init())
	.pipe(sass(styles.sass).on('error', sass.logError))
	.pipe(autoprefixer())
	.pipe(sourcemaps.write(''))
	.pipe(gulp.dest(path.join(BUILD_DIR, styles.dest)));
});

gulp.task('build:html', () => {
	gulp.src(path.join(DEV_DIR, html.src))
	.pipe(pug(html.pug))
	.pipe(gulp.dest(path.join(BUILD_DIR, html.dest)));
});

gulp.task('build:scripts', () => {
	gulp.src(path.join(DEV_DIR, scripts.src))
	.pipe(concat('scripts.js'))
	.pipe(gulp.dest(path.join(BUILD_DIR, scripts.dest)));
});

gulp.task('build:fonts', () => {
	gulp.src(path.join(DEV_DIR, fonts.src))
	.pipe(gulp.dest(path.join(BUILD_DIR, fonts.dest)));
});

gulp.task('build:images', () => {
	gulp.src(path.join(DEV_DIR, images.src))
	.pipe(gulp.dest(path.join(BUILD_DIR, images.dest)));
});

gulp.task('generate:todolist', () => {
	gulp.src(path.join(DEV_DIR, todolist.src))
	.pipe(todo(todolist.todo))
	.pipe(gulpIf((file) => {
		console.log(`Founded ${file.todos.length}`);
		return file.todos && Boolean(file.todos.length);
	}, gulp.dest(DEV_DIR), vinylPaths(del)));
});

gulp.task('reload', () => { server.reload() });
gulp.task('clean', () => { del.sync([BUILD_DIR, path.join(BUILD_DIR, '../templates')]) });
gulp.task('build', ['build:styles', 'build:html', 'build:scripts', 'build:fonts', 'build:images', 'generate:todolist']);
gulp.task('clean:build', ['clean', 'build']);

gulp.task('watch',() => {
	gulp.watch(path.join(DEV_DIR, styles.watch), ['build:styles', 'reload']).on('change', onChange );
	gulp.watch(path.join(DEV_DIR, html.watch), ['build:html', 'reload']).on('change', onChange );
	gulp.watch(path.join(DEV_DIR, scripts.watch), ['build:scripts', 'reload']).on('change', onChange );
});

gulp.task('default', ['build', 'watch'], () => {
	server.init(config.server);
});
