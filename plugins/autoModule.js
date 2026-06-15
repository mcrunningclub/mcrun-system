// jsdoc-plugins/auto-module.js
exports.handlers = {
  beforeParse(e) {
    const path = require("path");
    const moduleName = path.basename(e.filename, path.extname(e.filename));
    e.source = `/** @module ${moduleName} */\n` + e.source;
  }
};