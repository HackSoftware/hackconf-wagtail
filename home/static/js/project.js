$(document).ready(function() {
  if ($(document).scrollTop() == 0) {
    $(".go-top").fadeOut(200);
  }

  var allPastEvents = $(".past-events .row");
  allPastEvents.each(function(k, v) {
    $(v).css("left", k * 100 + 50 + "%");
  });
  allPastEvents.first().addClass("selected");
  $(".past-events-buttons .move-left").hide();
  if (allPastEvents.length < 2) $(".past-events-buttons .move-right").hide();
});

$(".go-top").click(function() {
  $("html, body").animate(
    {
      scrollTop: 0
    },
    500
  );
});
$(".menu-item").click(function(event) {
  event.preventDefault();

  $("body, html").animate(
    {
      scrollTop: $($.attr(this, "href")).offset().top
    },
    500
  );
});

$(window).scroll(function(e) {
  var arrow = $(".go-top");
  var duration = 200;
  if ($(document).scrollTop() > 0) {
    arrow.fadeIn(duration);
  } else {
    arrow.fadeOut(duration);
  }
});

$(".language-bar div").click(function() {
  var lang = $(this).attr("ref");
  var url = window.location.pathname.split(window.location.hostname);

  // remove the previous lang
  url.shift();

  var path = location.origin + "/" + lang + "/" + url.join("/");
  location.href = path;
});

var pastEventsLeftArrow = $(".past-events-buttons .move-right");
var pastEventsRightArrow = $(".past-events-buttons .move-left");
var allPastEvents = $(".past-events .row");

pastEventsLeftArrow.click(function() {
  if (allPastEvents.last().hasClass("selected")) return;

  var current = $(".past-events .row.selected");
  var next = current.next();

  next.addClass("selected");
  current.removeClass("selected");
  allPastEvents.animate({ left: "-=100%" }, 400);

  pastEventsRightArrow.show();
  if (allPastEvents.last().hasClass("selected")) {
    $(this).hide();
  }
});

pastEventsRightArrow.click(function() {
  if (allPastEvents.first().hasClass("selected")) return;

  var current = $(".past-events .row.selected");
  var prev = current.prev();

  prev.addClass("selected");
  current.removeClass("selected");
  allPastEvents.animate({ left: "+=100%" }, 400);

  pastEventsLeftArrow.show();
  if (allPastEvents.first().hasClass("selected")) {
    $(this).hide();
  }
});

$(".newsletter button[type='submit']").click(function(e) {
  var email = $(".newsletter")
    .find("input[type='email']")
    .val()
    .trim();
  if (email == "") return;
  window.open(
    "https://my.sendinblue.com/users/subscribe/js_id/26ky4/id/5/email/" + email
  );
});


// lecturer modal handlers
$(".lecturer .lecturer-modal-trigger").click(function() {
  $(this)
    .parents(".lecturer-container")
    .find(".lecturer-modal-wrapper")
    .show();
});

$(".lecturer-modal .close-button").click(function() {
  $(this)
    .parents(".lecturer-modal-wrapper")
    .hide();
});

// schedule modal handler
$(".schedule-item__more").click(function() {
  $("body").addClass("with-modal");
  $(this).parents(".schedule-item").find(".schedule-item-modal-wrapper").addClass("active");
})

$(".schedule-item-modal .close-button").click(function() {
  $("body").removeClass("with-modal");
  $(this).parents(".schedule-item").find(".schedule-item-modal-wrapper").removeClass("active");
})

// schedule tabbed interface switcher
$(".schedule-container__tabs > div").click(function() {
  var selectedTabContent = $(this).attr("ref");

  $(".tabs > div").removeClass("selected");
  $(this).addClass("selected")

  $(".tab-contents > div").removeClass("selected");
  $("."+selectedTabContent).addClass("selected");
})
