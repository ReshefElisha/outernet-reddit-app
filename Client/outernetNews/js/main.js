(function (window, $) {
  // List of locales that use right-to-left text direction
  var rtlLocales = ['ar'];

  // We need the current locale (language). We can either parse the URL (the
  // locale is always the first segment of the path) or we can use Librarian's
  // lang API.
  var locale = $.librarian.lang.getLocale();

  var postTemplate = [
    '<li class="post" id="ID">',
    '<div class="title">',
    '<a href="" onclick="toggleImage(\'ID\'); return false;">TITLE</a></div>',
    '<span class="date">DATE</span>',
    '<div class="post-image" style="display:none;"><img src="data:image;base64,CONTENT"/></div>',
    '</li>'
  ].join('');

  var emptyTwt = '<li class="post">No posts</li>';
  var async = [];
  var missingFolder = 'This folder does not exist';

  $.librarian.files.list('newsPosts', process);

  function process(dir_json) {
    if (!dir_json.files.length && dir_json.readme === missingFolder) {
      var output = '<li class="post"><p class="text">Posts directory does not yet exist. It will be created automatically when you get a new data file. Please wait until a data file has been downloaded to use this app.</p></li>';
      $('#posts').html(output);
      return;
    }
    if (!dir_json.files.length) {
      var output = '<li class="post"><p class="text">No posts in directory. Please wait until a data file has been downloaded to use this app.</p></li>';
      $('#posts').html(output);
      return;
    }
    var t;
    var xhr = [];
    var i = 0;
    dir_json.files.sort(function(a,b){
      return (a.name>b.name)?-1:(a.name<b.name)?1:0;
    });
    for (t in dir_json.files){
      post = $.librarian.files.url(dir_json['files'][t]['path']);
      console.log(post);
      (function(j){xhr.push($.getJSON(post).fail(function(){
        var rT = xhr[j].responseText.replace(/'/g, '"');
        var postobject = JSON.parse(rT);
        $('#posts').append(renderPost(postobject));
      }));})(i);
      async.push(xhr[i]);
      console.log(xhr[i]);
      i++;
    }
    $.when.apply($, async).done(function () {
      var results = [];
      var json;
      /*for (json in async) {
        var post_json = async[json]['responseJSON'];
        var post;
        for (post in post_json) {
          results.push(renderPost(post_json[tweet]));
          }
        }
      results.reverse();
      $('#posts').html(results);*/
    } );
    }

  function renderPost(message) {
    console.log(message);
    return postTemplate
      .replace(/ID/g, message['id'])
      .replace('TITLE', message['title'])
      .replace('DATE', message['date'])
      .replace('SUBREDDIT', message['subreddit'])
      .replace('CONTENT', message['content']);
  }

  toggleImage = function(id) {
    ($('#'+id+' .post-image').css('display') == 'none')?$('#'+id+' .post-image').css('display','block'):$('#'+id+' .post-image').css('display','none');
  }
}(this, jQuery));
