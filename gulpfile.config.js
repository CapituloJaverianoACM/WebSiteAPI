'use strict';

import path from 'path';

const config = {
	"dev_dir": "dev",
	"build_dir": "WebSite/static",
	"server": {
		"proxy": "http://localhost:8000/"
	},
	"styles": {
		"src": "scss/styles.scss",
		"dest": "css",
		"watch": "scss/**/*.scss",
		"sass": {
			"outputStyle": "compressed"
		},
		"autoprefixer": {
			"browsers": "last 2 versions",
			"cascade": false
		}
	},
	"html": {
		"src": "pug/pages/**/*.pug",
		"dest": "../templates",
		"watch": "pug/**/*.pug",
		"pug": {
			"pretty": "\t",
			"locals": {}
		},
	},
	"scripts": {
		"src": "js/**/*.js",
		"dest": "js",
		"watch": "js/**/*.js",
		"index": "js/index.js"
	},
	"fonts": {
		"src": "fonts/**/*",
		"dest": "fonts"
	},
	"images": {
		"src": "images/**/*",
		"dest": "images"
	},
	"todolist": {
		"src": "**/*.!(eot|svg|png|jpg|jpeg|gif|ttf|woff|woff2|otf|md)",
		"todo": {
			"fileName": "todo.md",
			"reporter": "markdown",
			"verbose": true,
			"customTags": [],
			"skipUnsupported": true
		}
	}
};

const onChange = (file) => {
	console.log(`File modified: "${path.basename(file.path)}"`);
};

export {config, onChange};
