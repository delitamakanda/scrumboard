var gulp = require('gulp'),
    runSequence = require('run-sequence'),
    jshint = require('gulp-jshint');


gulp.task('default', function () {
  runSequence('lint',
  'watch');
});

gulp.task('lint', function () {
  return gulp.src('./scrumboard/scripts/*.js')
  .pipe(jshint())
  .pipe(jshint.reporter('default'));
})

gulp.task('watch', function () {
  gulp.watch('./scrumboard/scripts/**/*.js', ['lint']);
})
