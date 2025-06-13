import re

# Given HTML content (Replace this with your actual HTML content)
html_content = """
<!DOCTYPE html>
<html lang="te">
 <head>
  <title>
   Stunning Photos of Sravanthi: A Must-See! | Stunning Photos of Sravanthi: A Must-See!
  </title>
  <link href="/images/ico/favicon.ico?v=1" rel="icon" type="image/x-icon"/>
  <link href="/images/ico/favicon.ico?v=1" rel="shortcut icon" type="image/x-icon"/>
  <meta charset="utf-8"/>
  <meta content="IE=Edge" http-equiv="X-UA-Compatible"/>
  <meta content="width=device-width, initial-scale=1.0, maximum-scale=10.0,user-scalable=yes,minimum-scale=1.0" name="viewport"/>
  <meta content="Stunning Photos of Sravanthi: A Must-See! | Stunning Photos of Sravanthi: A Must-See!" name="title"/>
  <meta content="https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif" name="image"/>
  <meta content="Sravanthi Chokkarapu is a beloved figure in the film industry, known for her captivating presence both on and off the screen" name="description"/>
  <meta content="Tupaki" name="application-name"/>
  <meta content="Sravanthichokkarapu,Sravanthi,Tollywoodanchor,Photoshoots,Biggbosstelugu,Chokkarapu,Actressgallery" name="keywords"/>
  <link as="image" fetchpriority="high" href="/images/placeholder.jpg" rel="preload"/>
  <link as="script" crossorigin="" href="/scripts/hocalwirecommlightp1.min.38c2b3fd.js" rel="preload"/>
  <link as="script" crossorigin="" href="/scripts/hocalwirecommlightp2.min.b654f6c8.js" rel="preload"/>
  <link as="script" crossorigin="" href="/scripts/themetealjs.min.702fa29d.js" rel="preload"/>
  <link as="style" crossorigin="" href="/styles/themetealfile.min.8b61cce3.css" rel="preload"/>
  <meta content="Sravanthichokkarapu,Sravanthi,Tollywoodanchor,Photoshoots,Biggbosstelugu,Chokkarapu,Actressgallery" name="news_keywords"/>
  <meta content="te" http-equiv="Content-Language"/>
  <meta content="notranslate" name="google"/>
  <meta content="Tupaki Desk" name="author"/>
  <meta content="tupaki" name="copyright"/>
  <meta content="follow, index" name="robots"/>
  <meta content="max-image-preview:large" name="robots"/>
  <meta content="true" name="HandheldFriendly"/>
  <meta content="origin" name="referrer"/>
  <meta content="summary_large_image" name="twitter:card"/>
  <meta content="https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181" property="og:url"/>
  <meta content="te_IN" property="og:locale"/>
  <meta content="https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181" name="twitter:url"/>
  <meta content="https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181" name="original-source"/>
  <!-- -preloadImage = preloadImage.replace(".webp",".jpg")-->
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364263-hwruvmus.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364261-cjrlovqn.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364264-im0tc4s5.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364259-07ljlob0.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364260-hukk4yga.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364262-h9aw7plu.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364265-l32warm3.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364266-lvo0nds9.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364267-nbgi5rm2.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364268-1dpmwssc.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364270-fn504zp1.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364269-7xzgcvis.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364272-lf5hf7qs.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364273-l026egmx.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364271-hkr8qpm1.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364275-x5d2irzo.gif" rel="preload"/>
  <!-- -videoUrl = videoUrl.replace(".webp",".jpg")-->
  <link as="image" fetchpriority="high" href="https://content.tupaki.com/h-upload/2024/04/23/364274-pvlyq1sv.gif" rel="preload"/>
  <!-- -var preloadImage = meta.image-->
  <!-- -if(meta.imageOriginalWebp){-->
  <!--     -preloadImage = preloadImage.replace(".jpg",".webp")-->
  <!-- -}-->
  <!-- link(rel='preload' as='image' href="#{preloadImage}")-->
  <link href="//cdn.syndication.twimg.com" rel="dns-prefetch"/>
  <link href="//www.facebook.com" rel="dns-prefetch"/>
  <link href="//connect.facebook.net" rel="dns-prefetch"/>
  <link href="//pagead2.googlesyndication.com" rel="dns-prefetch"/>
  <link href="//www.youtube.com" rel="dns-prefetch"/>
  <link href="//platform.twitter.com" rel="dns-prefetch"/>
  <link href="//gstatic.com" rel="dns-prefetch"/>
  <link href="//www.google.com" rel="dns-prefetch"/>
  <link href="//www.google.co.in" rel="dns-prefetch"/>
  <link href="//s.ytimg.com" rel="dns-prefetch"/>
  <link href="//hocalwire.com" rel="dns-prefetch"/>
  <link href="//www.hocalwire.com" rel="dns-prefetch"/>
  <link href="//adservice.google.co.in" rel="dns-prefetch"/>
  <link href="//tpc.googlesyndication.com" rel="dns-prefetch"/>
  <link href="//cdnimg.izooto.com" rel="dns-prefetch"/>
  <link href="//fonts.googleapis.com" rel="dns-prefetch"/>
  <link href="//fonts.gstatic.com" rel="dns-prefetch"/>
  <link href="//www.googletagservices.com" rel="dns-prefetch"/>
  <link href="//securepubads.g.doubleclick.net" rel="dns-prefetch"/>
  <link href="//stats.g.doubleclick.net" rel="dns-prefetch"/>
  <link href="//cdn.syndication.twimg.com" rel="preconnect"/>
  <link href="//www.facebook.com" rel="preconnect"/>
  <link href="//connect.facebook.net" rel="preconnect"/>
  <link href="//pagead2.googlesyndication.com" rel="preconnect"/>
  <link href="//www.youtube.com" rel="preconnect"/>
  <link href="//platform.twitter.com" rel="preconnect"/>
  <link href="//gstatic.com" rel="preconnect"/>
  <link href="//www.google.com" rel="preconnect"/>
  <link href="//www.google.co.in" rel="preconnect"/>
  <link href="//s.ytimg.com" rel="preconnect"/>
  <link href="//hocalwire.com" rel="preconnect"/>
  <link href="//www.hocalwire.com" rel="preconnect"/>
  <link href="//adservice.google.co.in" rel="preconnect"/>
  <link href="//tpc.googlesyndication.com" rel="preconnect"/>
  <link href="//cdnimg.izooto.com" rel="preconnect"/>
  <link href="//fonts.googleapis.com" rel="preconnect"/>
  <link href="//fonts.gstatic.com" rel="preconnect"/>
  <link href="//www.googletagservices.com" rel="preconnect"/>
  <link href="//securepubads.g.doubleclick.net" rel="preconnect"/>
  <link href="//stats.g.doubleclick.net" rel="preconnect"/>
  <script>
   window.dynamicPage ="true";
window.support_article_infinite_scroll ="true";
window.similar_news_infinite_scroll ="true";
window.xhrPageLoad ="";
window.isNewsArticlePage ="true";
  </script>
  <script>
   window.infiniteScrollUrls = [];
window.infiniteScroll=true;
  </script>
  <meta content="656805295098940" property="fb:app_id"/>
  <link href="/manifest.json" rel="manifest"/>
  <meta content="article" property="og:type"/>
  <script>
   window.ignoreCoreScripts = "true";
window.exclude_dynamic_links_only =  "true";
window.disable_unveil = "";
window.enableTransliteration = "";
window.extra_whatsapp_share_message = "";

window.auto_play_videos_in_view = "";
window.comment_post_as = "";
  </script>
  <script>
   window.load_theme_resource_after_pageLoad = "true"
  </script>
  <meta content="Stunning Photos of Sravanthi: A Must-See!" property="og:title"/>
  <meta content="Sravanthi Chokkarapu is a beloved figure in the film industry, known for her captivating presence both on and off the screen" property="og:description"/>
  <meta content="https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif" itemprop="image" property="og:image"/>
  <meta content="https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif" itemprop="image" property="og:image:secure_url"/>
  <meta content="Stunning Photos of Sravanthi: A Must-See!" property="twitter:title"/>
  <meta content="Sravanthi Chokkarapu is a beloved figure in the film industry, known for her captivating presence both on and off the screen" property="twitter:description"/>
  <meta content="https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif" property="twitter:image"/>
  <meta content="Stunning Photos of Sravanthi: A Must-See!" property="twitter:image:alt"/>
  <meta content="https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif" itemprop="image" property="og:image:secure"/>
  <meta content="2024-04-23T20:18:00+05:30" property="article:published_time"/>
  <meta content="2024-04-23T20:18:00+05:30" property="article:modified_time"/>
  <meta content="2024-04-23T20:18:00+05:30" property="article:updated_time"/>
  <meta content="Photo Gallery" property="article:section"/>
  <meta content="Sravanthichokkarapu" property="article:tag"/>
  <meta content="Sravanthi" property="article:tag"/>
  <meta content="Tollywoodanchor" property="article:tag"/>
  <meta content="Photoshoots" property="article:tag"/>
  <meta content="Biggbosstelugu" property="article:tag"/>
  <meta content="Chokkarapu" property="article:tag"/>
  <meta content="Actressgallery" property="article:tag"/>
  <meta content="1200" property="og:image:width"/>
  <meta content="630" property="og:image:height"/>
  <script>
   window.single_source_news_url = ""
window.popup_ad_cookie_duration = ""
window.popup_ad_display_duration = ""
window.road_blocker_ad_cookie_duration="10"
window.road_blocker_ad_display_duration="30"
window.epaperClipRatio="7"
window.scriptLoadDelay=parseInt("1000")
window.scriptLoadDelayExternalScripts=parseInt("")
window.windowLoadedDelay=parseInt("")
window.exclude_common_ga="true"
window.exclude_all_ga=""
window.payment_success_redirect_url = ""
window.refresh_pages_on_interval = {"/":"660000"};
window.refresh_pages_on_interval_using_ajax = {};

window.maxAllowCropHeightFactor = ""
window.clipLogo = ""
window.disable_hcomment_email_mandatory = ""
window.disable_hcomment_name_mandatory = ""
window.track_pageview_only_once_infinite =  ""

window.sidekick_ad_cookie_duration = ""
window.sidekick_ad_display_duration = ""
window.sidekick_ad_autostart_duration = ""
window.pushdown_ad_close_duration = ""

window.ignore_webp_supprt_check = ""
window.max_dynamic_links_count = ""

window.use_non_ajax_path_for_mixin =  ""
window.no_show_initial_popup =  ""

window.use_advance_search_as_default = ""
window.locationContentPage = ""
  </script>
  <script async="" src="https://www.googletagmanager.com/gtag/js?id=G-4TW3Z4QVHF">
  </script>
  <script>
   window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-4TW3Z4QVHF');
  </script>
  <script>
   window.FBCODE = "656805295098940";
  </script>
  <script>
   window.COMSCORECODE = "39547594";
  </script>
  <script>
   window.insetLinkInCopy = '' || true;
window.insetLinkInCopyLoggedIn = '';
  </script>
  <script>
   window.trackingPageType = "dynamic";
  </script>
  <script>
   window.userDataToBePassedBack = {};
  </script>
  <script>
   window.externalResourcesVersion = "1";
window.externalResources = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js,https://www.instagram.com/embed.js,https://securepubads.g.doubleclick.net/tag/js/gpt.js,https://platform.twitter.com/widgets.js,https://cdn.izooto.com/scripts/d8702c295e4a9476c3d31e1694fbb318711922f9.js,https://t.seedtag.com/t/6537-0291-01.js";
window.externalResourcesLength = "6";
  </script>
  <script>
   window.Constants = {"url":{"xhrLogin":"/xhr/admin/login/loginUser","xhrLoginOrRegister":"/xhr/admin/login/loginOrRegisterUser","xhrRegister":"/xhr/admin/login/registerUser","xhrVerify":"/xhr/admin/login/verifyUser","xhrVerifyEmail":"/xhr/admin/login/verifyEmail","xhrForgotPassword":"/xhr/admin/login/forgotPassword","xhrResetPassword":"/xhr/admin/login/reset-password","xhrLogout":"/xhr/admin/login/logout","xhrRegenerateEmailCode":"/xhr/admin/login/regenerateEmailCode"}};
  </script>
  <script>
   window.enable_webp_images = "true";
  </script>
  <script>
   window.userDeviceType = "d";
  </script>
  <script>
   window.hasIntagram = ""
window.hasTwitter = ""
window.isIOS = ""
window.sendNewsReadState = "true"
window.image_quality_percentage = ""
window.enable_js_image_compress = ""
window.local_date_time_format = ""
window.partnerName  = "Tupaki"
window.partnerCopyrightName  = "tupaki"
window.ignoreInitialDFPIdChange = "";
window.tooltipMobileSidePadding = "";

window.isAdFree = "0";

window.isPremiumContent = "";
window.delaySecThemeScriptsAction = "1"
window.delaySecThemeScriptsActionOthers = "1"

window.ignore_also_read_image = ""

window.ip_based_login_enabled = ""; 
window.chars_per_min_read = "1000";
window.user_review_content_id = "";
window.user_review_content_id_ugc = "";
window.custom_data_to_be_passed = "";
window.includePartyTownScript = "";
window.open_paymentgate_default_on_checkout ="";
window.adCustomContentName = "";
window.subscriptionPageUrl = "";

window.externalSubscriberLandingUrl = "?token=";
window.partner_coupon_discount_message = "";

window.autoSlideGallery = "";
window.autoSlideGalleryTimeout = "";

window.isContentPageForSubscription = "true";


window.refresh_website_in_interval_using_ajax = "/";
  </script>
  <meta content="autoRotate:disabled" http-equiv="ScreenOrientation"/>
  <!-- -if(typeof data!="undefined" && data['extra_header_tags'] && data['extra_header_tags']['templateData'] && data['extra_header_tags']['templateData']['content']){-->
  <!--     !{data['extra_header_tags']['templateData']['content']}-->
  <!-- -}-->
  <style class="styles" type="text/css">
   body img,iframe,video{max-width:100%}.hide-scroll{overflow:hidden}img{height:auto}.details-content-story iframe.note-video-clip{width:100%}body,html{-webkit-overflow-scrolling:touch}#content{-webkit-overflow-scrolling:touch}#content{height:100%}#main #content{display:inline}.hide{display:none!important}.soft-hide{display:none}.bg-404{background:url(/images/404.jpg);background-repeat:no-repeat;background-size:100%;background-position:center;background-blend-mode:screen;min-height:400px;text-align:center}.bg-404 .error404-content{background:#fff;padding:20px;font-size:30px;opacity:.8}a img{max-width:100%}.newsSocialIcons li a{color:#fff}.newsSocialIcons li a:hover{text-decoration:none!important}.newsSocialIcons li a i{margin-right:4px}.newsSocialIcons{width:100%;display:inline-block;text-align:right}.newsSocialIcons a{padding:5px;display:inline-block}.hocalwire-cp-authors-social,.newsSocialIcons ul{width:100%;padding-left:0}.hocalwire-cp-authors-social{text-align:left}.newsSocialIcons li{list-style:none!important;width:25px;height:25px;text-decoration:none;font-family:Oswald!important;text-transform:uppercase;background:0 0;opacity:1;line-height:30px;padding:0;margin:0 3px;position:relative}.newsSocialIcons li a{color:#fff;height:21px}.newsSocialIcons li a:hover{text-decoration:none!important}.newsSocialIcons li a i{margin-right:4px}.newsSocialIcons li.facebook,.sticky li.facebook{border:0 solid #314b83;background-color:#4769a5}.newsSocialIcons li.whatsapp,.sticky li.whatsapp{border:0 solid #65bc54;background-color:#65bc54}.newsSocialIcons li.telegram,.sticky li.telegram{border:0 solid #379be5;background-color:#379be5}.newsSocialIcons li.pintrest{border:0;background-color:#d50c22}.newsSocialIcons li.twitter,.sticky li.twitter{border:0 solid #000;background-color:#000}.newsSocialIcons li.googleplus{border:0 solid #ab2b1d;background-color:#bf3727}.newsSocialIcons li.gplus{border:0 solid #ab2b1d;background-color:#bf3727}.newsSocialIcons li.linkedin,.sticky li.linkedin{border:0 solid #278cc0;background-color:#2ba3e1}.newsSocialIcons li.tumblr{border:0 solid #2c3c4c;background-color:#34495e}.newsSocialIcons li.pinterest,.sticky li.printrest{border:0 solid #ae1319;background-color:#cd252b}.newsSocialIcons li.email{border:0 solid #4b3b3b;background-color:#4b3b3b}.newsSocialIcons li.mail,.sticky li.mail{border:0 solid #18ae91;background-color:#1abc9c}.sticky li.email,.sticky li.mail{border:0 solid #4b3b3b;background-color:#4b3b3b}.newsSocialIcons li.print{border:0 solid #000;background-color:#000}.sticky li.print{border:0 solid #000;background-color:#000}.newsSocialIcons li.youtube{border:0 solid #e62117;background-color:#e62117}.newsSocialIcons li.insta{border:0 solid #0526c5;background-color:#0526c5}.newsSocialIcons li img{vertical-align:top}.newsSocialIcons ul{border-radius:3px;padding:5px;z-index:10;float:left;clear:both}.newsSocialIcons.right-navigation ul li+li{display:none;float:left;border-radius:30px;padding-top:2px}.newsSocialIcons li{float:left;border-radius:30px}.listing-social-share .newsSocialIcons li{border-radius:30px!important}.margin-top10{margin-top:10px}.sticky-container{position:fixed;top:40%;z-index:11111111111}.sticky-container ul li p{padding:5px}.sticky li.facebook{border:0 solid #314b83;background-color:#4769a5}.sticky li.twitter{border:0 solid #000;background-color:#000}.sticky li.googleplus{border:0 solid #ab2b1d;background-color:#bf3727}.sticky li.gplus{border:0 solid #ab2b1d;background-color:#bf3727}.sticky li.linkedin{border:0 solid #278cc0;background-color:#2ba3e1}.sticky li.tumblr{border:0 solid #2c3c4c;background-color:#34495e}.sticky li.pinterest{border:0 solid #ae1319;background-color:#cd252b}.sticky li.mail{border:0 solid #18ae91;background-color:#1abc9c}.sticky li.youtube{border:0 solid #e62117;background-color:#e62117}.sticky-container .fab{background:#03a9f4;width:37px;height:37px;text-align:center;color:#fff;box-shadow:0 0 3px rgba(0,0,0,.5),3px 3px 3px rgba(0,0,0,.25);position:fixed;right:1/4 * 3 * 64px;font-size:2.6667em;display:inline-block;cursor:default;bottom:100px;right:10px;z-index:10;box-sizing:border-box;padding:0 8px}.sticky-container .fab .not-logged-in img{vertical-align:top}.sticky-container .fab .logged-in img{vertical-align:top}.sticky-container .fab.child{right:(64px - 1 / 3 * 2 * 64px)/2 + 1/4 * 3 * 64px;width:1/3 * 2 * 64px;height:1/3 * 2 * 64px;display:none;opacity:0;font-size:2em}.sticky .fab img{height:auto;width:auto}.backdrop{position:fixed;top:0;left:0;width:100%;height:100%;background:#ececec;opacity:.3;display:none}#masterfab img{margin:auto;display:block;height:auto}#masterfab{padding:10px;max-width:38px;box-sizing:border-box}.details-content-story{overflow:hidden;display:inherit}.cd-top{cursor:pointer;position:fixed;bottom:100px;left:10px;width:35px;height:35px;background-color:#434343;box-shadow:0 0 10px rgba(0,0,0,.05);overflow:hidden;text-indent:100%;white-space:nowrap;background:rgba(232,98,86,.8) url(/images/cd-top-arrow.svg) no-repeat center 50%;visibility:hidden;opacity:0;-webkit-transition:opacity .3s 0s,visibility 0s .3s;-moz-transition:opacity .3s 0s,visibility 0s .3s;transition:opacity .3s 0s,visibility 0s .3s}.cd-top.cd-fade-out,.cd-top.cd-is-visible,.no-touch .cd-top:hover{-webkit-transition:opacity .3s 0s,visibility 0s 0s;-moz-transition:opacity .3s 0s,visibility 0s 0s;transition:opacity .3s 0s,visibility 0s 0s}.cd-top.cd-is-visible{visibility:visible;opacity:1;z-index:9999}.cd-top.cd-fade-out{opacity:.5}@-webkit-keyframes placeHolderShimmer{0%{background-position:-468px 0}100%{background-position:468px 0}}@keyframes placeHolderShimmer{0%{background-position:-468px 0}100%{background-position:468px 0}}.mixin-loader-wrapper{background-color:#e9eaed;color:#141823;padding:5px;border:1px solid #ccc;margin:0 auto 1em}.mixin-loader-item{background:#fff;border:1px solid;border-color:#e5e6e9 #dfe0e4 #d0d1d5;border-radius:3px;padding:12px;margin:0 auto}.placeholder_top{background:#fff;padding:5px;display:inline-block}.mixin-placeholder-details-wrapper{z-index:99;left:30%;display:inline-block;top:50px;color:#000;background:#0f0f0f;color:#fff;padding:10px}.placeholder_top .animated-background{-webkit-animation-duration:1s;animation-duration:1s;-webkit-animation-fill-mode:forwards;animation-fill-mode:forwards;-webkit-animation-iteration-count:infinite;animation-iteration-count:infinite;-webkit-animation-name:placeHolderShimmer;animation-name:placeHolderShimmer;-webkit-animation-timing-function:linear;animation-timing-function:linear;background:#f6f7f8;background:#eee;background:-webkit-gradient(linear,left top,right top,color-stop(8%,#eee),color-stop(18%,#ddd),color-stop(33%,#eee));background:-webkit-linear-gradient(left,#eee 8%,#ddd 18%,#eee 33%);background:linear-gradient(to right,#eee 8%,#ddd 18%,#eee 33%);-webkit-background-size:800px 104px;background-size:800px 104px}.hocal_col{width:100%;padding-top:5px;padding-bottom:5px}.padding_10{padding:10%}.padding_20{padding:20%}.placeholder_top .img.small{height:60px;max-width:80px}.placeholder_top .img.medium{height:150px;max-width:250px}.placeholder_top .img.big{height:300px;max-width:500px}.placeholder_top .img.supper-big{height:450px;max-width:750px}.content{margin-bottom:10px}.placeholder_top .content.small{height:10px;padding-left:5px;padding-right:5px}.placeholder_top .content.medium{height:20px;padding-left:10px;padding-right:10px}.placeholder_top .content.large{height:30px;padding-left:15px;padding-right:15px}.hocal_col_12{width:100%}.hocal_col_9{width:75%}.hocal_col_8{width:60%}.hocal_col_6{width:50%}.hocal_col_4{width:33%}.hocal_col_3{width:25%}.hocal_row{display:block}.hocal_col{display:block;float:left;position:relative}.placeholder_top .play{display:block;width:0;height:0;border-top:$size solid transparent;border-bottom:$size solid transparent;border-left:($size*$ratio) solid $foreground;margin:($size * 2) auto $size auto;position:relative;z-index:1;transition:all $transition-time;-webkit-transition:all $transition-time;-moz-transition:all $transition-time;left:($size*.2)}.placeholder_top .play:before{content:'';position:absolute;top:-75px;left:-115px;bottom:-75px;right:-35px;border-radius:50%;z-index:2;transition:all .3s;-webkit-transition:all .3s;-moz-transition:all .3s}.placeholder_top .play:after{content:'';opacity:0;transition:opacity .6s;-webkit-transition:opacity .6s;-moz-transition:opacity .6s}.details-content-story .inside_editor_caption.float-left,.details-content-story img.float-left{padding-right:10px;padding-bottom:10px;float:left;left:0}.details-content-story .inside_editor_caption.float-right,.details-content-story img.float-right{padding-left:10px;padding-bottom:10px;float:right;right:0}.details-content-story .image_caption{background:0 0}.details-content-story div,.details-content-story p{margin-bottom:15px!important;line-height:1.4;margin:0 auto}.details-content-story div.pasted-from-word-wrapper{margin-bottom:0!important}.details-content-story div.inside_editor_caption{display:none}.details-content-story .inside_editor_caption.edited-info{display:block}.details-content-story img{max-width:100%}.details-content-story .inside_editor_caption.float-left{margin-top:10px}.details-content-story .inside_editor_caption.float-right{margin-top:10px}.details-content-story img.float-none{margin:auto;float:none}.details-content-story .inside_editor_caption{font-size:16px;padding:2px;text-align:center;bottom:-20px;width:100%}.details-content-story .image-and-caption-wrapper{position:relative;margin-bottom:20px}.image-and-caption-wrapper{max-width:100%!important}.details-content-story .image-and-caption-wrapper.float-left{float:left;padding-right:10px;padding-bottom:10px}.details-content-story .image-and-caption-wrapper.float-right{float:right;padding-left:10px;padding-bottom:10px}.details-content-story .image-and-caption-wrapper.float-none{float:none;display:block;clear:both;left:0!important;margin:0 auto}.details-content-story .image-and-caption-wrapper.float-none img{display:block}.details-content-story .hide-on-web{display:none!important}.hide-on-web{display:none!important}.details-content-story .template-wrapper{padding:2px;width:100%}.details-content-story .template-wrapper .delete-lists-wrapper button{display:none}.details-content-story .template-wrapper .action-btn-wrapper{display:none}.details-content-story .list-item-heading{font-size:18px;margin-bottom:20px}.details-content-story li.list-item{margin-bottom:20px}.details-content-story .action-btn-wrapper span{padding:5px;margin:2px;background:#ccc}.details-content-story .template-wrapper{padding:2px;width:100%}.details-content-story .template-wrapper .delete-lists-wrapper{float:right;margin-top:10px}.details-content-story .template-wrapper .delete-lists-wrapper button{padding:10px;margin-right:10px;margin-top:-5px}.details-content-story .template-wrapper li.list-item{width:100%}.details-content-story .template-wrapper .action-btn-wrapper{float:left;margin-right:20px}.details-content-story .list-items-wrapper li{border:none!important}.details-content-story .list-items-wrapper.unordered-list ul{list-style-type:square}.modal_wrapper_frame{position:fixed;width:100%;top:0;height:100%;background:rgba(0,0,0,.7);opacity:1;z-index:9999999999}.modal_wrapper_frame #modal-content{position:absolute;left:20%;top:20%;right:20%;bottom:20%;border:1px solid #ccc;background:#fff}.modal_wrapper_frame .cross-btn{right:10px;top:10px;position:absolute;font-size:20px;cursor:pointer;padding:5px;z-index:9999}.modal_wrapper_frame iframe{width:100%;height:100%}.hocal_hide_on_desktop{display:none!important}.hocal_hide_on_mobile{display:block!important}.placeholder_top{width:100%}.placeholder_top .hocal_col{padding:5px;box-sizing:border-box}.also-read-media{display:none}.also-read-media-wrap{display:none}@media screen and (max-width:767px){.bg-404 .error404-content{background:#fff;padding:10px;font-size:20px}.hocal_hide_on_mobile{display:none!important}.hocal_hide_on_desktop{display:block!important}.modal_wrapper_frame #modal-content{left:2%;top:2%;right:2%;bottom:2%}.details-content-story .image-and-caption-wrapper.float-left,.details-content-story .image-and-caption-wrapper.float-right{display:inline;max-width:100%!important;float:none!important;padding:0!important}.details-content-story .inside_editor_caption.float-right,.details-content-story img.float-right{display:inline;max-width:100%!important;float:none!important;padding:0!important}.details-content-story .inside_editor_caption.float-left,.details-content-story img.float-left{display:inline;max-width:100%!important;float:none!important;padding:0!important}}#comments iframe{width:100%!important}#bottom_snackbar{width:30%;position:fixed;z-index:1;bottom:0;z-index:999999999999999999999999999999999999999999999999999999999999999999999;left:70%;background:#333}#bottom_snackbar .close-btn{position:absolute;right:3px;top:3px;padding:1px 8px;cursor:pointer;z-index:9999999999;font-size:20px;color:#fff}#bottom_snackbar.right{left:70%}#bottom_snackbar.left{left:0}#bottom_snackbar.center{left:35%}.bottom_snackbar_content{background:#0582e2}@media screen and (max-width:767px){#bottom_snackbar{width:100%}#bottom_snackbar,#bottom_snackbar.center,#bottom_snackbar.left,#bottom_snackbar.right{left:0}}.login-btn-in-message{color:#00f;text-decoration:underline;cursor:pointer;font-size:16px}.show-pass-wrap{float:right}#news_buzz_updates .buzz-timeline-wrapper{background:#f7f8f9}.buzz-timeline-wrapper .load-more-update-wrapper{text-align:center;cursor:pointer;width:100%}.buzz-timeline-wrapper .load-more-update-wrapper a{background:red;color:#fff;padding:4px 25px;display:inline-block;margin-bottom:10px}.buzz-timeline-wrapper .timeline{position:relative;max-width:1200px;margin:0 auto}.buzz-timeline-wrapper .timeline::after{content:'';position:absolute;width:6px;background-color:#c5c5c5;top:0;bottom:0;left:10%;margin-left:-3px}.buzz-timeline-wrapper .buzz-container{padding:10px 40px;position:relative;background-color:inherit;width:90%;list-style:none;box-sizing:border-box}.buzz-timeline-wrapper .buzz-container::after{content:'';position:absolute;width:25px;height:25px;right:-17px;background-color:#fff;border:4px solid #c5c5c5;top:15px;border-radius:50%;z-index:1}.buzz-timeline-wrapper .left{left:0}.buzz-timeline-wrapper .right{left:10%;text-align:right!important;float:none!important;margin-left:0!important}.buzz-timeline-wrapper .left::before{content:" ";height:0;position:absolute;top:22px;width:0;z-index:1;right:30px;border:medium solid #fff;border-width:10px 0 10px 10px;border-color:transparent transparent transparent #fff}.buzz-timeline-wrapper .right::before{content:" ";height:0;position:absolute;top:22px;width:0;z-index:1;left:30px;border:medium solid #fff;border-width:10px 10px 10px 0;border-color:transparent #fff transparent transparent}.buzz-timeline-wrapper .right::after{left:-13px}.buzz-timeline-wrapper .buzz_date{font-size:12px;color:#666}.buzz-timeline-wrapper .content{padding:10px 15px;background-color:#fff;position:relative;border-radius:6px;text-align:left}.buzz-timeline-wrapper .list_image{width:25%}.buzz-timeline-wrapper h2{margin-bottom:0!important;font-size:16px;margin-top:0;background:#fff;font-weight:400}.buzz_story{font-size:15px}.buzz-timeline-wrapper .buzz-image{float:left;margin-right:10px;max-width:50%}.buzz-timeline-wrapper .image-and-caption-wrapper{text-align:center;position:relative;display:inline-block;float:none!important;width:100%!important}.buzz-timeline-wrapper .image-and-caption-wrapper img{max-height:400px;width:auto!important;float:none!important}.buzz-timeline-wrapper .image_caption{background:#fff!important}.buzz-parent-wrapper .news_updates_heading{text-align:center}.buzz-parent-wrapper .news_updates_heading a{border-bottom:2px solid #ccc;padding-left:10px;padding-right:10px}@media screen and (max-width:600px){.buzz-timeline-wrapper .buzz-image{float:none;margin-right:0;max-width:1000%}.buzz-timeline-wrapper .list_image{width:100%}.buzz-timeline-wrapper .timeline::after{left:31px}.buzz-timeline-wrapper .buzz-container{width:100%;padding-left:70px;padding-right:25px}.buzz-timeline-wrapper .buzz-container::before{left:60px;border:medium solid #fff;border-width:10px 10px 10px 0;border-color:transparent #fff transparent transparent}.buzz-timeline-wrapper .left::after,.buzz-timeline-wrapper .right::after{left:17px}.buzz-timeline-wrapper .right{left:0}.buzz-timeline-wrapper .timeline::after{background-color:transparent}.buzz-timeline-wrapper .buzz-container{padding-left:10px;padding-right:10px}.buzz-timeline-wrapper .buzz-container::after{background-color:transparent;border:0 solid #c5c5c5}.buzz-timeline-wrapper .content{box-shadow:0 4px 8px 0 rgba(0,0,0,.2);transition:.3s}.buzz-timeline-wrapper .right::before{display:none}#news_buzz_updates .buzz-timeline-wrapper{background:#fff}.buzz-timeline-wrapper .timeline{padding:0}}.nextpage.divider{display:none;font-size:24px;text-align:center;width:75%;margin:40px auto}.nextpage.divider span{display:table-cell;position:relative}.nextpage.divider span:first-child,.nextpage.divider span:last-child{width:50%;top:13px;-moz-background-size:100% 2px;background-size:100% 2px;background-position:0 0,0 100%;background-repeat:no-repeat}.nextpage.divider span:first-child{background-image:-webkit-gradient(linear,0 0,0 100%,from(transparent),to(#000));background-image:-webkit-linear-gradient(180deg,transparent,#000);background-image:-moz-linear-gradient(180deg,transparent,#000);background-image:-o-linear-gradient(180deg,transparent,#000);background-image:linear-gradient(90deg,transparent,#000)}.nextpage.divider span:nth-child(2){color:#000;padding:0 5px;width:auto;white-space:nowrap}.nextpage.divider span:last-child{background-image:-webkit-gradient(linear,0 0,0 100%,from(#000),to(transparent));background-image:-webkit-linear-gradient(180deg,#000,transparent);background-image:-moz-linear-gradient(180deg,#000,transparent);background-image:-o-linear-gradient(180deg,#000,transparent);background-image:linear-gradient(90deg,#000,transparent)}.next-page-loader h2{color:#000;margin:0;font:.8em verdana;margin-top:20px;text-transform:uppercase;letter-spacing:.1em}.next-page-loader span{display:inline-block;vertical-align:middle;width:.6em;height:.6em;margin:.19em;background:#222;border-radius:.6em;animation:loading 1s infinite alternate}.next-page-loader span:nth-of-type(2){background:#222;animation-delay:.2s}.next-page-loader span:nth-of-type(3){background:#222;animation-delay:.4s}.next-page-loader span:nth-of-type(4){background:#222;animation-delay:.6s}.next-page-loader span:nth-of-type(5){background:#222;animation-delay:.8s}.next-page-loader span:nth-of-type(6){background:#222;animation-delay:1s}.next-page-loader span:nth-of-type(7){background:#222;animation-delay:1.2s}.pagi_wrap{width:100%;position:relative;position:relative}.pagi_wrap ul{margin:auto;display:block;text-align:center;width:100%;position:relative}.pagi_wrap ul li{display:inline-block;margin:0 15px;text-align:center;position:relative}.pagi_wrap ul li.active a{cursor:default}.pagi_wrap ul li span{color:#333;vertical-align:middle;display:inline-block;font-size:20px;line-height:45px;width:45px;height:45px;background:#dfebf9;text-align:center;border-radius:50%}.pagi_wrap ul li.active span{background:#ccc}.hocalwire-cp-authors-social,.newsSocialIcons ul{width:100%;padding-left:0}.hocalwire-cp-authors-social{text-align:center}.hocalwire-cp-authors-social li{width:20px;height:20px;padding:4px;margin:5px;display:inline-block}.hocalwire-cp-authors-social li:first-child{margin-left:0}.hocalwire-cp-authors-social li a{height:20px;position:relative;display:block}.hocalwire-cp-authors-social li.facebook,.hocalwire-cp-authors-social1 li.facebook{border:0 solid #314b83;background-color:#4769a5}.hocalwire-cp-authors-social li.twitter,.hocalwire-cp-authors-social1 li.twitter{border:0 solid #000;background-color:#000}.hocalwire-cp-authors-social li.googleplus,.hocalwire-cp-authors-social1 li.googleplus{border:0 solid #ab2b1d;background-color:#bf3727}.hocalwire-cp-authors-social li.gplus,.hocalwire-cp-authors-social1 li.gplus{border:0 solid #ab2b1d;background-color:#bf3727}.hocalwire-cp-authors-social li.linkedin,.hocalwire-cp-authors-social1 li.linkedin{border:0 solid #278cc0;background-color:#2ba3e1}.hocalwire-cp-authors-social li.dark{background-color:#ccc!important}.insert-more-buzz-here{display:inline-block;position:relative;width:100%}@keyframes loading{0%{opacity:0}100%{opacity:1}}#details-bottom-element-for-infinite-scroll{text-align:center}#state-selection{display:none}.details-content-story blockquote{width:100%;text-align:center}.details-content-story iframe{display:block;margin:0 auto;max-width:100%}.details-content-story video{width:100%;max-height:450px}.details-content-story video.hocal-uploaded-video.audio-file{max-height:70px}twitter-widget{margin:0 auto}.epaper-datepicker-img{display:inline-block;max-width:20px;position:absolute;top:10px;left:10px}.inline-block{position:relative}#epaper-datepicker{padding-left:30px}.track-on-infinite-scroll-view{min-height:1px}.cd-top{right:10px;left:auto}.buzz-timeline-wrapper .load-more-update-wrapper a.next-page-live-update,.buzz-timeline-wrapper .load-more-update-wrapper a.prev-page-live-update,.next-page-live-update,.prev-page-live-update{float:right;margin-left:10px;margin-right:10px;margin-top:20px;background:0 0;color:#000}.view-all-updates-xhr-wrap{display:block;width:100%;margin-top:20px;margin-bottom:20px;text-align:center}.view-all-updates-xhr-wrap a{background:#000!important;color:#fff!important;padding:10px 20px}.blog-share-socials-light{text-align:right}.blog-share-socials-light li{display:inline-block;position:relative;max-width:25px;margin:0 6px;border-radius:10px;text-align:right;padding:5px;box-sizing:border-box}.no-more-updates{text-align:center;color:#000;background:#cfcfcf;font-size:23px;padding:40px;margin-bottom:20px}.news-updates-pagination{width:100%;text-align:center;margin-top:20px;margin-bottom:20px;display:inline-block}.news-updates-pagination a{padding:10px;background:#000;margin:5px;color:#fff}.buzz-list-wrapper h2{padding-left:0;clear:none}.buzz-list-wrapper .latest_item h2 a{color:#000;font-size:18px;font-weight:700}.buzz-list-wrapper p{line-height:1.5}.hocalwire-editor-list li p{display:inline}.buzz-list-wrapper ul.hocalwire-editor-list li,.details-content-story ul li,.details-content-story ul.hocalwire-editor-list li{display:block!important;margin-bottom:15px}.buzz-list-wrapper ul.hocalwire-editor-list li:before,.details-content-story ul li::before,.details-content-story ul.hocalwire-editor-list li::before,.hocal_short_desc li::before{content:"\2022";color:#000;font-weight:700;display:inline-block;width:25px;margin-left:0;font-size:30px;vertical-align:sub}.details-content-story table{width:100%;margin-bottom:10px;margin-top:10px;display:block;overflow-x:scroll;border-spacing:0;border-collapse:collapse}.details-content-story table td,.details-content-story table th,.details-content-story table tr{border:1px solid #000;padding:5px;text-align:left;font-size:14px}.details-content-story table thead{background:#eaeaea}.details-content-story .h-embed-wrapper .twitter-tweet,.details-content-story .h-embed-wrapper>div{margin-left:auto;margin-right:auto}.fluid-width-video-wrapper{padding-top:0!important;display:inline-block;height:500px}.fluid-width-video-wrapper embed,.fluid-width-video-wrapper object{max-height:500px}.single-post-title{text-transform:inherit}.subscription-btn-on-login{display:none}#left-ad-full-screen{position:fixed;height:80%;top:20%;width:140px;left:10px}#right-ad-full-screen{position:fixed;height:80%;top:20%;width:140px;right:10px}.pasted-from-word-wrapper>div{margin-bottom:15px}iframe.instagram-media{margin:0 auto!important;width:100%!important;position:relative!important}.scroll div{display:inline-block}.loop-nav.pag-nav{background:#fff}.pag-nav{font-size:12px;line-height:20px;font-weight:700;text-align:center}.loop-nav{border-top:0 solid #ddd}.loop-nav-inner{border-top:1px solid #fff;padding:20px 0}.wp-pagenavi{clear:both}.pagenavi span{text-decoration:none;border:1px solid #bfbfbf;padding:3px 5px;margin:2px}.pag-nav a,.pag-nav span{color:#555;margin:0 4px 4px;border:1px solid #ccc;-webkit-border-radius:3px;border-radius:3px;display:inline-block;padding:4px 8px;background-color:#e7e7e7;background-image:-ms-linear-gradient(top,#eee,#e7e7e7);background-image:-moz-linear-gradient(top,#eee,#e7e7e7);background-image:-o-linear-gradient(top,#eee,#e7e7e7);background-image:-webkit-gradient(linear,left top,left bottom,from(#eee),to(#e7e7e7));background-image:-webkit-linear-gradient(top,#eee,#e7e7e7);background-image:linear-gradient(top,#eee,#e7e7e7);-webkit-box-shadow:inset 0 1px 0 #fff,0 1px 1px rgba(0,0,0,.1);box-shadow:inset 0 1px 0 #fff,0 1px 1px rgba(0,0,0,.1)}.pag-nav span{color:#999}.pag-nav .current{background:#f7f7f7;border:1px solid #bbb;-webkit-box-shadow:inset 0 1px 5px rgba(0,0,0,.25),0 1px 0 #fff;box-shadow:inset 0 1px 5px rgba(0,0,0,.25),0 1px 0 #fff}.pag-nav span{color:#999}.wp-pagenavi a:hover,.wp-pagenavi span.current{border-color:#000}.wp-pagenavi span.current{font-weight:700}.hocal-draggable iframe.note-video-clip{width:100%}.hocal-draggable iframe,.hocal-draggable video{text-align:center}.details-content-story ol,ol.hocalwire-editor-list{counter-reset:num_cntr;padding-left:35px}.details-content-story ol li,ol.hocalwire-editor-list li{counter-increment:num_cntr;position:relative;margin-bottom:10px}.sticky-container ul{list-style:none!important}.sticky-container .fab img{padding:2px;margin-top:-10px}.native-fb-wrap.facebook{display:inline-block;float:left;margin-top:8px;margin-right:10px}.amp-flying-carpet-wrapper{overflow:hidden}.amp-flying-carpet-text-border{background:#000;color:#fff;padding:.25em}.amp-fx-flying-carpet{height:300px;overflow:hidden;position:relative}.amp-fx-flying-carpet-clip{position:absolute;top:0;left:0;width:100%;height:100%;border:0;margin:0;padding:0;clip:rect(0,auto,auto,0);-webkit-clip-path:polygon(0 0,100% 0,100% 100%,0 100%);clip-path:polygon(0 0,100% 0,100% 100%,0 100%)}.amp-fx-flying-carpet-container{position:fixed;top:0;width:100%;height:100%;-webkit-transform:translateZ(0);display:-webkit-box;display:-ms-flexbox;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-ms-flex-direction:column;flex-direction:column;-webkit-box-align:center;-ms-flex-align:center;align-items:center;-webkit-box-pack:center;-ms-flex-pack:center;justify-content:center;max-width:320px;margin-top:120px}.dfp-ad{height:600px;width:300px;background:0 0;text-align:center;vertical-align:middle;display:table-cell;position:relative}.dfp-ad-container{position:absolute}.in-image-ad-wrap{position:absolute;bottom:0;width:100%;overflow:hidden;background:rgba(255,255,255,.5)}.in-image-ad-wrap .close-btn-in-img{display:inline-block;position:absolute;right:0;top:0;cursor:pointer}.in-image-ad-wrap .ad-content{width:100%;overflow-x:scroll}.in-image-ad-wrap .ad-content>div{margin:0 auto}.common-ad-block{margin:10px}.common-ad-block-pd{padding:10px}.popup-ad-content-wrap,.roadblocker-content-wrap{position:fixed;top:0;left:0;height:100%;width:100%;z-index:9999999}.popup-ad-content-wrap .popup-overlay-bg,.roadblocker-content-wrap .popup-overlay-bg{background:rgba(0,0,0,.5);width:100%;position:fixed;top:0;left:0;z-index:1;height:100%}.roadblocker-content-wrap .popup-overlay-bg{background:#fff}.popup-ad-content-wrap .popup-content-container,.roadblocker-content-wrap .popup-content-container{display:inline-block;width:100%;margin:0 auto;text-align:center;height:100%;position:absolute;z-index:99}.popup-ad-content-wrap .popup-content-container .center-content,.roadblocker-content-wrap .popup-content-container .center-content{position:relative;margin-top:120px}.popup-ad-content-wrap .popup-content-container .center-content .content-box,.roadblocker-content-wrap .popup-content-container .center-content .content-box{display:inline-block}.popup-ad-content-wrap .popup-content-container .center-content .content-box{max-height:550px;overflow:auto;max-width:80%}.popup-ad-content-wrap .popup-content-container .center-content .close-btn-popup,.roadblocker-content-wrap .popup-content-container .center-content .close-btn-popup{display:inline-block;position:absolute;top:0;background:#fff;color:#000!important;padding:5px 10px;cursor:pointer}.roadblocker-content-wrap .popup-content-container .close-btn-popup{position:absolute;top:10px;right:10px;background:rgba(0,0,0,.5)!important;padding:10px;color:#fff!important;cursor:pointer;z-index:999}.roadblocker-content-wrap .popup-content-container .road-blocker-timer{position:absolute;top:10px;right:48px;padding:10px;color:#000;font-size:1.3rem;cursor:pointer;z-index:999}.inline-heading-ad{display:inline-block;margin-left:10px}pre{max-width:100%;display:inline-block;position:relative;width:100%;white-space:pre-wrap;white-space:-moz-pre-wrap;white-space:-pre-wrap;white-space:-o-pre-wrap;word-wrap:break-word}.from-paytm-app .hide-for-paytm{display:none}.from-paytm-app .at-share-dock{display:none!important}@media all and (max-width:800px){.amp-fx-flying-carpet-container{margin-top:55px}.popup-ad-content-wrap .popup-content-container .center-content{margin-top:60px}.epaper_listing .hocalwire-col-md-3{width:100%!important;float:none!important}.epaper_listing{display:inline}.pagi_wrap ul li{margin:0 5px}.pagi_wrap ul li span{line-height:35px;width:35px;height:35px}#left-ad-full-screen{display:none}#right-ad-full-screen{display:none}.fluid-width-video-wrapper{height:300px}.fluid-width-video-wrapper embed,.fluid-width-video-wrapper object{max-height:300px}.epaper-filter-item .selectpicker{width:120px;font-size:12px}.epaper-filter-item #epaper-datepicker{width:125px;margin-left:-22px;padding-left:20px}.epaper-datepicker-img{display:inline-block;max-width:16px;position:absolute;top:7px;left:-14px}}@media all and (max-width:500px){.hocal_col_4{width:100%}.hocal_col_3{width:100%}.placeholder_top .img.medium{max-width:100%}}.common-user-pages .page_heading{text-align:center;font-size:25px;padding:5px 30px}.common-user-pages .form-links{min-height:20px}.ad_unit_wrapper_main{background:#f1f1f1;padding:0 5px 5px 5px;border:1px solid #ccc;margin:10px 0}.ad_unit_wrapper_main .ad_unit_label{text-align:center;font-size:12px}.read-this-also-wrap{padding:5px 0;margin:5px 0}.read-this-also-wrap .read-this-also{font-weight:700;color:#222}.dark .read-this-also-wrap .read-this-also{color:#908b8b}.read-this-also-wrap a{color:red}.read-this-also-wrap a:hover{color:#222}.desktop-only-embed,.mobile-only-embed,.tab-only-embed{display:none}.facebook-responsive iframe{width:auto}@media screen and (min-width:1025px){.desktop-only-embed{display:block}.facebook-responsive{overflow:hidden;padding-bottom:56.25%;position:relative;height:0}.facebook-responsive iframe{left:0;top:0;right:0;height:100%;width:100%;position:absolute;width:auto}}@media screen and (min-width:768px) and (max-width:1024px){.tab-only-embed{display:block}.facebook-responsive{overflow:hidden;padding-bottom:56.25%;position:relative;height:0}.facebook-responsive iframe{left:0;top:0;right:0;height:100%;width:100%;position:absolute;width:auto}}@media screen and (max-width:767px){.mobile-only-embed{display:block}}@media print{.ind-social-wrapper{display:none}}.buzz-timeline-wrapper .load-more-update-wrapper a.next-page-live-update,.buzz-timeline-wrapper .load-more-update-wrapper a.prev-page-live-update,.load-more-update-wrapper .next-page-live-update,.load-more-update-wrapper .prev-page-live-update{padding:0 7px;background:red;color:#fff;width:25px}.annotation-tooltip-parent sup{color:red;display:inline-block}.tooltip-wall{position:fixed;width:300px;z-index:9999;height:100%;background:#000;color:#fff;display:none;top:20%;right:0;background:0 0}.tooltip-wall .tooltip-popup-title{font-size:1.5rem;font-weight:700}.tooltip-wall .tooltip-wall-wrap{margin:10px;display:inline-block;position:fixed;height:auto;background-color:#f4f4f4;color:#000;padding:20px;border-radius:5px;box-shadow:1px 3px 4px 1px #c4c4c4}.tooltip-wall .tooltip-wall-wrap:after{content:' ';position:absolute;width:0;height:0;left:-27px;right:auto;top:20px;bottom:auto;border:12px solid;border-color:#f4f4f4 #f4f4f4 transparent transparent;width:0;height:0;border-top:20px solid transparent;border-bottom:20px solid transparent;border-right:20px solid #f4f4f4}.tooltip-popup-wrap{font-size:14px;line-height:20px;color:#333;padding:1px;background-color:#fff;border:1px solid #ccc;border:1px solid rgba(0,0,0,.2);-webkit-border-radius:6px;-moz-border-radius:6px;border-radius:6px;-webkit-box-shadow:0 5px 10px rgba(0,0,0,.2);-moz-box-shadow:0 5px 10px rgba(0,0,0,.2);box-shadow:0 5px 10px rgba(0,0,0,.2);-webkit-background-clip:padding-box;-moz-background-clip:padding;background-clip:padding-box;max-width:480px;width:90%;position:absolute;z-index:9}.tooltip-popup-wrap .tooltip-popup-header{padding:2px 14px;margin:0;min-height:30px;font-size:14px;font-weight:400;line-height:18px;background-color:#f7f7f7;border-bottom:1px solid #ebebeb;-webkit-border-radius:5px 5px 0 0;-moz-border-radius:5px 5px 0 0;border-radius:5px 5px 0 0;position:relative}.tooltip-popup-wrap .tooltip-popup-header .tooltip-popup-title,.tooltip-wall-wrap .tooltip-popup-header .tooltip-popup-title{margin-right:20px;max-width:100%;box-sizing:border-box;position:relative;display:block;font-size:16px}.tooltip-popup-wrap .tooltip-popup-header .tooltip-popup-close,.tooltip-wall-wrap .tooltip-popup-header .tooltip-popup-close{position:absolute;right:10px;top:3px}.tooltip-popup-wrap .tooltip-popup-header .tooltip-popup-close label{font-size:18px}.tooltip-popup-wrap .tooltip-popup-content{position:relative;padding:10px 10px;overflow:hidden;text-align:left;word-wrap:break-word;font-size:14px;display:block}.tooltip-inputbtn{display:none}.tooltip-inputbtn+label>.tooltip-popup-wrap{display:none;min-width:300px}.tooltip-inputbtn+label{display:inline;position:relative;padding:2px 4px;cursor:pointer}.tooltip-inputbtn:checked+label>.tooltip-popup-wrap{position:absolute;top:24px;left:0;z-index:100}.tooltip-popup-header{display:block}.tooltip-inputbtn+label>.tooltip-popup-wrap span{color:#000!important}.mixin-debug-mode-wrap{position:relative;width:100%;height:100%}.mixin-debug-mode-wrap .mixin-debug-mode-element{position:absolute;top:0;right:0;width:100%;height:100%;background:rgba(0,0,0,.8);z-index:999999999999999999}.mixin-debug-mode-wrap .mixin-debug-mode-element .text{color:#fff;font-size:20px;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);word-break:break-all;line-height:1.1}.story-highlight-block{border:1px solid #ccc;border-radius:5px}.story-highlight-block .story-highlight-block-heading{padding:1px 15px;background:#efefef;padding-bottom:1px}.story-highlight-block .story-highlight-block-heading a,.story-highlight-block .story-highlight-block-heading div,.story-highlight-block .story-highlight-block-heading p{color:#000;font-weight:700;padding-top:5px}.story-highlight-block-content{padding:0 10px}.adsbygoogle{overflow:hidden}.newsSocialIcons li.koo,.sticky li.koo{border:0 solid #fbd051;background-color:#fbd051}.h-resize-menu-container:not(.jsfield){overflow-x:inherit;-webkit-overflow-scrolling:inherit}.h-resize-menu-container.jsfield .h-resize-menu-primary{overflow:hidden;white-space:nowrap}.h-resize-menu-container .h-resize-menu-primary{overflow:scroll;white-space:nowrap;display:block}.h-resize-menu-container.jsfield.show-submenu .h-resize-menu-primary{overflow:inherit}.h-resize-menu-container .h-resize-menu-primary .h-resize-submenu{display:none;border-radius:0 0 10px 10px;position:absolute;right:0;z-index:111;background:#000;width:210px;padding:10px;line-height:30px;text-align:left;-webkit-animation:nav-secondary .2s;animation:nav-secondary .2s}.h-resize-menu-container.show-submenu .h-resize-submenu{display:block}.no-data-found{text-align:center;padding:20px;background:#eee;margin:10px}.sidekick{position:relative}.sidekick .sidebar-wrapper{position:fixed;top:0;left:0;height:100%;width:19rem;margin-left:-18rem;color:#fff;z-index:99999;padding:5px;background:#fff}.sidekick .sidebar-wrapper.right-side{right:0;left:auto;margin-right:-18rem}.sidekick .sidebar-wrapper .sidekick-nav-btn{font-size:1.2rem;position:absolute;top:48%;right:-1rem;border-radius:50%;width:30px;height:30px;background:#000;display:flex;align-items:center;vertical-align:middle;text-align:center;justify-content:center}.sidekick .sidebar-wrapper.right-side .sidekick-nav-btn{top:50%;left:-1rem}.sidekick-nav-btn img{width:24px;height:24px;border-radius:50%;position:absolute}.sidekick .sidebar-wrapper.show-sidebar{margin-left:0}.sidekick .sidebar-wrapper.show-sidebar.right-side{margin-right:0}.push-body{margin-left:18rem}.push-body.right-side{margin-right:18rem;margin-left:inherit}.sidekick-slide-over.push-body{margin-left:0;margin-right:0}.sidekick.closed-by-user.hide-on-close{display:none}.buzz_article_date_wrapper{display:none}.live-icon{display:none}.details-content-story{word-break:break-word}.gallery-slider-wrapper .rslides li{list-style:none!important}.referral-code-block{display:none}.referral-code-block.show{display:block}.mixin-debug-mode-element-refresh{background:#fff;border:2px solid #ccc;padding:10px;margin-bottom:20px;text-align:center}.mixin-debug-mode-element-refresh .refresh-mixin-btn{background:#000;margin:5px;padding:10px;color:#fff!important;position:relative;display:inline-block;cursor:pointer}.center-loading-msg{display:flex;align-items:center;vertical-align:middle;text-align:center;justify-content:center}.common-sign-in-with-wrapper{text-align:center;margin-bottom:20px}.common-sign-in-with-wrapper .sing-in-with-label{text-align:center;font-size:1.2rem;padding-top:10px;border-top:1px solid #ccc}.common-sign-in-with-wrapper .social-login img{max-height:24px;margin-right:10px}.common-sign-in-with-wrapper .social-login{padding:10px;border:1px solid #ccc}.common-sign-in-with-wrapper .social-login.facebook{background:#3b5998;margin-bottom:10px}.common-sign-in-with-wrapper .social-login.google{background:#de5246;margin-bottom:10px}.common-sign-in-with-wrapper .social-login a{color:#fff}.js-logout-button{cursor:pointer}.load-more-update-wrapper .next-page-live-update,.load-more-update-wrapper .prev-page-live-update{display:none!important}.roadblocker-content-wrap{overflow-y:auto}.road-blocker-parent-wraper{background:#f0f2f5;position:absolute;width:100%;height:100%}.timer-wraper-parent{display:flex;align-items:center;justify-content:space-between;position:fixed;left:0;right:0;top:0;z-index:99999;background:#fff}.roadblocker-content-wrap .popup-content-container .road-blocker-timer{color:#000;position:unset;padding:unset;flex-basis:10%}.road-blocker-title-wrap{display:flex;align-items:center;justify-content:space-between;flex-basis:80%}.road-blocker-title-wrap .title{flex-basis:70%;font-size:1.3rem;color:#000}.roadblocker-content-wrap .popup-content-container .close-btn-popup{position:unset!important;background:#d4eaed!important}.roadblocker-content-wrap .popup-content-container .center-content{padding-top:40px!important;margin-top:0!important}.road-blocker-skip{font-size:1.1rem;color:#337ab7}.road-blocker-logo-image img{max-width:120px;max-height:60px;width:100%;height:100%;object-fit:cover;margin-left:10px}.newsSocialIcons li.email img{padding:5px}.big-login-box{display:flex;justify-content:center;align-items:center;text-align:center;min-height:100vh}@media only screen and (max-width:1024px){.road-blocker-title-wrap{flex-basis:70%}.road-blocker-title-wrap .title{flex-basis:60%;font-size:1rem}}@media only screen and (max-width:450px){.roadblocker-content-wrap .popup-content-container .road-blocker-timer{flex-basis:25%;font-size:1rem}.road-blocker-skip{font-size:1rem}}@media only screen and (min-width:451px) and (max-width:1024){.roadblocker-content-wrap .popup-content-container .road-blocker-timer{flex-basis:11%}}.sticky-container .fab svg{padding:2px;margin-top:-10px}.app-lite-body-page-wrapper #iz-news-hub-main-container,.app-lite-body-page-wrapper #iz-newshub-container{display:none!important}.shake-tilt-slow{animation:tilt-shaking-slow .25s linear infinite}.shake-tilt-jerk{animation:tilt-shaking 1s linear infinite}@keyframes tilt-shaking-jerk{0%{transform:rotate(0)}40%{transform:rotate(0)}45%{transform:rotate(2deg)}50%{transform:rotate(0eg)}55%{transform:rotate(-2deg)}60%{transform:rotate(0)}100%{transform:rotate(0)}}.shake-tilt{animation:tilt-shaking .25s linear infinite}@keyframes tilt-shaking{0%{transform:rotate(0)}25%{transform:rotate(5deg)}50%{transform:rotate(0eg)}75%{transform:rotate(-5deg)}100%{transform:rotate(0)}}.shake-tilt-move-slow{animation:tilt-n-move-shaking-slow .25s linear infinite}@keyframes tilt-shaking-slow{0%{transform:rotate(0)}25%{transform:rotate(2deg)}50%{transform:rotate(0eg)}75%{transform:rotate(-2deg)}100%{transform:rotate(0)}}@keyframes tilt-n-move-shaking-slow{0%{transform:translate(0,0) rotate(0)}25%{transform:translate(5px,5px) rotate(2deg)}50%{transform:translate(0,0) rotate(0eg)}75%{transform:translate(-5px,5px) rotate(-2deg)}100%{transform:translate(0,0) rotate(0)}}.shake-tilt-move{animation:tilt-n-move-shaking .25s linear infinite}@keyframes tilt-n-move-shaking{0%{transform:translate(0,0) rotate(0)}25%{transform:translate(5px,5px) rotate(5deg)}50%{transform:translate(0,0) rotate(0eg)}75%{transform:translate(-5px,5px) rotate(-5deg)}100%{transform:translate(0,0) rotate(0)}}span.institute-name{font-weight:700}.institute-ip-message{overflow:auto;padding:20px;font-size:2rem;text-align:left;margin:0 auto}.insti-popup .close-btn-popup{right:5px}.ip-insti-frame-wrapper #modal-content{max-height:400px}@media screen and (min-width:1024px){.ip-insti-frame-wrapper #modal-content{max-height:200px}}
  </style>
  <!-- Begin comScore Tag -->
  <script>
   var _comscore = _comscore || [];    _comscore.push({      c1: "2",      c2: "39547594",      options: {        enableFirstPartyCookie: "true"      }    });    (function() {      var s = document.createElement("script"),        el = document.getElementsByTagName("script")[0];      s.async = true;      s.src = (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js";      el.parentNode.insertBefore(s, el);    })();
  </script>
  <noscript>
   <img src="https://sb.scorecardresearch.com/p?c1=2&amp;c2=39547594&amp;cv=3.9.1&amp;cj=1"/>
  </noscript>
  <!-- End comScore Tag -->
  <meta content="#ed3833" name="theme-color">
   <script>
    window._izq = window._izq || []; window._izq.push(["init"]);
   </script>
   <meta content="aiMOL2cKemm9gUYnVGvirRfH7Oj1ulo3o52aMhYjPj8" name="google-site-verification"/>
   <meta content="bWGRYHejTvlzr3PDKrxQ0FEb4Pel-CJRrwFy0eP-IiM" name="google-site-verification">
    <style>
     .politics-business .content-flex .politics-flex {      max-width: 290px;  }    @media only screen and (max-width: 768px){    #ad_after_header{  text-align: none !important;  }  div#tabs-headlines3 .entertainment-content p {      font-size: 19px;  }  }     .tab-content-flex .politics-business.top-news.topnews-left {      margin-top: 59px;  }    .reelss .loco_cat.loco_section .swiper-slide h4{  font-weight: 400 !important;  }      .level_5_ad_before{      display:none;        }  #top_buttons .nav-tabs li{   width: 240px !important;                    }  @media screen and (max-width: 1500px) and (min-width: 1366px){  .entertainment-telugu .entertainment-flex {      height: 870px !important;  }  }      #level_14 .title .story-heading a{      font-weight: bold;   }  #level_11 .s-amp-block-heading a{      font-weight: bold;  }  .single-gallery-click-zoom img{width:100%;}  .accordion__item .accordion__item:first-child {      padding-top: 12px;  }  .accordion__item .accordion__item span{        font-size:14px !important;  }  .accordion__item .accordion__item a {      font-family: 'Roboto', sans-serif;      font-style: normal;      font-weight: 700;      font-size: 14px !important;      padding: 0px 12px 0px 14px !important;      line-height: 261.68%;      color: #FFFFFF;  }  div#mySidenav{      height: -webkit-fill-available !important;  }  .accordion__item .accordion__item:not(:last-child) {      border-bottom: 0;  }  .accordion__item button.accordion__btn.has-sub-menu a {      color: white !important;  padding-left:12px !important;  }  .accordion__item a.accordion__btn {      display: flex;      justify-content: space-between;      width: 100%;      padding: 1.2rem 1.4rem;      background: #262626;      border: none;      outline: 0;      color: #fff !important;      font-size: 1.2rem;      text-align: left;      cursor: pointer;      transition: .1s;  }  @media screen  and (min-width:318px) and (max-width: 320px){    .ind-social-wrapper .ind-social-cover ul.ind-social-ul.color-mode li.ind-social-li.link {     display:none !important;    }     }    #follow_block .follow {      height: auto !important;       text-align: center;  }  .details-page-wrapper .content-flex p {  min-height:auto !important;  }    .overlay-rotate-device{    display: none;    position: fixed;    z-index: 9999999;    background: rgba(0,0,0,0.9);    top:48%;    text-align: center;  width:100%;    }  .overlay-rotate-device .rotate-message{    color:#fff;    font-size: 30px;    padding: 10px;  }    @media screen and (min-width: 320px) and (max-width: 1024px) and (orientation: landscape) {    .overlay-rotate-device {      display:block;    }  }
    </style>
    <style>
     #ad_after_header{  text-align: center !important;  }  #ad_after_header2{  display:none ;  text-align: center !important;  }  #level_2_ad_before{  display:none !important;  text-align: center !important;  }  #level_3_ad_before{  display:none !important;  text-align: center !important;  }  #level_3_3_ad{  display:none !important;  text-align: center !important;  }    #level_1_ad_1{  display : none !important;  }  #detail_wrap_ad_1{  display : none !important;  }  #left_level_1,#inside_post_content_ad_2,#inside_post_content_ad_3{  !important;  text-align: center !important;  }    @media only screen and (max-width: 768px) {  #ad_after_header2{  display:block !important;  text-align: center !important;  }  .level_5_ad_before{    display:block !important;  text-align: center !important;        }  #left_level_1,#inside_post_content_ad_1,#inside_post_content_ad_2,#inside_post_content_ad_3{  display:block !important;  text-align: center !important;  }  .image_wrapper.cutom-gallery.clearfix2 .slides-num {      display: none !important;  }  .image_wrapper.cutom-gallery.clearfix2{     margin-top:1rem;  }  #left_level_1{  min-height:100px !important;  display:block !important;  text-align: center !important;  }  .political-news .details-page h2{  font-size: 23px!important;  }  #detail_wrap_ad_1{  display : block !important;  }  #level_1_ad_1{  display : block !important;  }  #header_ad_1{  min-height:51px !important;  display:block !important;  text-align: center !important;  }  #list_ad_1{  min-height:292px !important ;  text-align: center !important;  }  #right_level_1{  min-height:292px !important ;  display:block !important;  text-align: center !important;  }  #level_3_3_ad{  min-height:292px !important ;  display:block !important;  text-align: center !important;  }  #level_3_ad_before{  min-height:292px !important ;  display:block !important;  text-align: center !important;  }  #level_2_ad_before{  min-height:292px !important ;  display:block !important;  text-align: center !important;  }  #ad_after_header{    display:block !important;  text-align: center !important;  }  #level_2_ad_before{  min-height:292px !important ;  display: block  !important;  text-align: center !important;  }  #level_3_ad_before{  min-height:292px !important;  display:block !important ;  text-align: center !important;  }  #level_3_3_ad{  min-height:292px !important;  display:block !important;  text-align: center !important;  }  }
    </style>
    <style>
     #level_1 .img-wrapper img{      aspect-ratio: 3/5 !important;  }  .news-link.tab-block-img{    max-width: 165px;  display:block;  }  #tabs-home3.politics-business .content-flex .politics img{    max-width: 150px;  display:block;  }  #tabs-profile3.politics-business.content-flex .politics img{         max-width: 100px;  display:block;  }  #level_3_3 .entertainment-scroll.grid-block-for-images{      margin-top: 10px;  }  #level_3_1 .entertainment-scroll.grid-block-for-images{      margin-top: 10px;  }   .photo-gallery-details-page .left_level_1{      min-height: 300px !important;      display: block !important;  }  .photo-gallery-details-page .right_level_1{   min-height: 300px !important;      display: block !important;  }      #level_3_2_ad{  min-height:292px !important;  display:block !important ;  text-align:center;  }  }    #gallery_right_level_1{  min-height: 300px !important;      display: block !important;  }    #left-ad-full-screen,#right-ad-full-screen{  margin-top:20px !important;  }    nav.navbar.navbar-default.navbar-fixed-top .topbar-logo .navbar-row .navbar-right:nth-child(3) {      margin: 0;  }      div#header_social_icons ul.list-inline {      max-width: calc(100% - 85px) !important;  }      nav.navbar.navbar-default.navbar-fixed-top .topbar-logo .navbar-row .navbar-right:nth-child(4) {      margin: 0;  }      div#header_social_icons ul.list-inline {      max-width: calc(100% - 85px) !important;  }    div#level_2_ad_before, #level_3_ad_before {      display: none ! IMPORTANT;  }
    </style>
    <script async="" custom-element="amp-ad" src="https://cdn.ampproject.org/v0/amp-ad-0.1.js">
    </script>
    <script async="" src="https://t.seedtag.com/t/6537-0291-01.js">
    </script>
    <style>
     #level_1{  display: none;  }
    </style>
    <meta content="#ed3833" name="theme-color">
     <script async="" custom-element="amp-iframe" src="https://cdn.ampproject.org/v0/amp-iframe-0.1.js">
      </script          <meta name="google-site-verification" content="aiMOL2cKemm9gUYnVGvirRfH7Oj1ulo3o52aMhYjPj8">  <link rel="preconnect" href="https://fonts.googleapis.com">  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>  <link href="https://fonts.googleapis.com/css2?family=Mallanna&display=swap" rel="stylesheet">  <style>  #level_14  .card-text-content h3{  font-family: 'Ramabhadra' !important;  }  #photo_stories .reels-heading a.news-link:hover{          font-family: 'Ramabhadra';  }  .entertainment-bg h2{        font-family: 'Ramabhadra';      font-weight: 500;  }  .andhra-content.political-news .andhra-pradesh h4{    line-height: 1.4;  }   #top .reviews .entertainment-scroll .share-content span{     font-weight: 500;    font-family: 'Mallanna';  font-size: 18px;  }  .movie-details-page .constent-review .about-section.reviews p{      font-weight: 500;  font-size: 18px;      font-family: 'Mallanna' !important;      font-family: 'Mallanna' !important;      font-weight: 500 !important;      font-size: 14px;  }  .share-content h3{        font-family: 'Ramabhadra';          font-weight: 500  }    .andhra-content.political-news .andhra-pradesh h4{   font-family: 'Ramabhadra';      font-weight: 300;  }  .andhra-district .andhra-pradesh .district .politics-business .content-flex p{    line-height: 16px;  }  .details-page-wrapper .content-flex p{       font-family: 'Mallanna' !important;    font-weight: 500 !important;;  }      .political-news h2{    font-family: 'Ramabhadra';      font-weight: 500;    }    .press-release.andhra-pradesh .content-padding p{  font-family: 'Ramabhadra';  }   .press-release h4{  font-family: 'Ramabhadra';     font-weight: 300;   }   .press-release h4 {     font-weight: 300;      font-size: 19PX;      font-family: 'Ramabhadra';  }  #level_11 .s-description-text{      font-size: 16px;        font-weight: 100;  line-height: 22px !important;  }  #level_7 .reelss .swiper-containernn .swiper-slide h3{         font-family: 'Ramabhadra';  font-weight: 100;      font-size: 17px;  }  #level_7 .reelss .heding h2{      font-family: 'Ramabhadra';  font-weight: 100;      font-size: 17px;  }  #level_7 .reelss .swiper-containernn .swiper-slide.swiper-slide-active h3{      font-family: 'Ramabhadra';  font-weight: 100;      font-size: 17px;  }  #tabs-home3 a.news-link p {  font-size: 18px !important;;  }  #tabs-profile3 a.news-link p {  font-size: 18px !important;;  }   .content-flex .entertainment-content p{  font-weight: 100;  }  .content-flex p{   font-family: 'Ramabhadra';          font-weight: 100;  }  .entertainment-scroll p{      font-weight: 100;  }  #parent .politics-flex p{     font-weight: 100;  }  a.news-link.news-list p {      font-family: 'Ramabhadra', sans-serif !important;      font-size: 17px;  }  div#level_3_2 a.news-link.news-list p {      font-family: 'Roboto', sans-serif !important;  }    a.news-link.atom_link.atom_valid p {      font-family: 'Ramabhadra', sans-serif !important;      font-size: 17px !important;  }  h2.s-amp-h3 {      font-family: 'Ramabhadra', sans-serif;  }  .politics-flex a.news-link p {      font-family: 'Ramabhadra', sans-serif !important;      font-size: 17px !important;  }  a.news-link p {      font-family: 'Ramabhadra', sans-serif !important;      font-size: 17px;  }  div#level_17 .content a.news-link h4 {      font-family: 'Ramabhadra', sans-serif;      font-size: 17px !important;  }  div#level_20 .content a h4 {      font-family: 'Ramabhadra', sans-serif !important;      font-size: 17px;  }  div#level_12 a.news-link h3 {      font-family: 'Ramabhadra', sans-serif;      font-size: 17px;  }   div#level_3_2 a.news-link.news-list p{      font-size: 16px;  }    @media only screen and (max-width: 767px){  .listing-page .level_1_left{     display:none;  }  .image_wrapper.cutom-gallery.clearfix2 .slides-num {      display: none !important;  }  .image_wrapper.cutom-gallery.clearfix2{     margin-top:1rem;  }  a.news-link.news-list p{      font-weight: 400 !important ;  }  .page details-page-wrapper.content-flex p{  font-size: 16px !important;  }    .andhra-district .andhra-pradesh .district .politics-business .content-flex p{      font-weight: 400;    }   div#level_3_2 a.news-link.news-list p{      font-size: 18px;  }  #tabs-profile3 a.news-link p{      font-weight: 400 !important;      font-size: 18px !important;  }  #tabs-home3 a.news-link p{      font-weight: 400 !important;      font-size: 18px !important;  }    .content-flex .entertainment-content p{  line-height: 30px;  }    .politics-business .content-flex .politics-flex p {      line-height: 24px;  font-weight: 400;      }      #parent .politics-flex p {      line-height: 24px;  }  .andhra-district .andhra-pradesh .district .politics-business .content-flex p {      line-height: 24px;      }        .reelss .loco_cat.loco_section .swiper-slide h4 {  line-height: 24px;  }    .latest-news-entertainment .entertainment-scroll p{  font-weight: 500;  }  }  </style>    <style>    #level_14 .ads-slider .card-text-content h3 {      font-family: 'Ramabhadra' !important;  }    #follow_block .follow {      height: auto !important;      text-align: center;    }    .movie-details-page .related.entertainment-sec #movie_right_level_2 img {      min-height: auto !important;  }    @media only screen and (max-width: 821px) {      div#level_3_2 .entertainment-scroll a.linked-media {          margin-top: 0px !important;      }        div#level_3_2 .entertainment-scroll a.news-link.news-list p {          font-size: 16px !important;          line-height: 20px;      }        #follow_block .follow p {          padding: 0px 10px !important;        }        .follow {          height: auto !important;          text-align: center;        }     }    #tabs-profile3 .content-flex .entertainment-content p {      color: #f00201;      font-size: 20px !important;      line-height: 30px;    }    #tabs-home3 .content-flex .entertainment-content p {      color: #f00201;      font-size: 20px !important;      line-height: 30px;    }    @media screen and (max-width: 767px) {      .footer-widget-heading h3 {          font-size: 14px !important;      }        .related.entertainment-sec .related-posts.movie-review .generic-right .entertainment-scroll {          flex-direction: row;      }        .single-image img {          min-height: 200px;      }        .pagination {          position: inherit !important;      }        .indrani h3 {          line-height: 25px !important;      }  }    .live-width .live-news {      background: red;  }      .read-this-also-wrap {      border: 1px solid #f00201;      text-align: center !important;  }    .read-this-also {      font-size: 16px !important;      color: #F00201 !important;      text-align: justify;  }    .read-this-also-wrap a:not(.also-read-media-wrap) {      font-family: 'Roboto', sans-serif;      font-style: normal;      font-weight: 400;      font-size: 14px;      color: #000000;      text-align: center;      padding: 5px;      margin: 0px;  }    .tabs-all-ul .active.btn {      cursor: auto;  }    #detail_wrap_1 {      width: 100%;  }    .indrani-slider .swiper-container .swiper-button-next {      right: 5px !important;  }    .indrani-slider .swiper-container .swiper-button-next,  .indrani-slider .swiper-container .swiper-button-prev {      background: #fff !important;      top: 40%;  }    .indrani-slider .swiper-container .swiper-button-prev {      left: 5px !important;  }      #level_3_2_ad img {      margin-bottom: 5px;  }    .pagination {      float: none !important;      justify-content: center;  }    .tags-section .content-flex {      width: 100% !important;  }    body {      overflow-y: scroll !important;  }    .clearfix2 .slides-num {      display: none;  }    </style>    <style>    .photo-gallery-details-page .share span {      display: none !important;  }  .ind-social-ul li span{      display: flex !important;  }  .photo-gallery-details-page .left_level_1{      min-height: 300px !important;      display: block !important;  }    .political-news .details-page h2 {      font-weight: 400;      font-size: 26px;      line-height: 1.2 !important;      margin-top: 18px;  }  .details-page-wrapper .content-flex p {      font-family: Mallanna!important;      font-weight: 500!important;      min-height: auto !important;      text-align: inherit !important;      padding: 5px 0px !important;  }    </style>        <style>      #pmLink {          visibility: hidden;          text-decoration: none;          cursor: pointer;          background: transparent;          border: none;      }        #pmLink:hover {          visibility: visible;          color: grey;      }  </style>    <script async custom-element="amp-iframe" src="https://cdn.ampproject.org/v0/amp-iframe-0.1.js">
     </script>
     <script type="text/javascript">
      window._taboola = window._taboola || [];  if(window.location.pathname=="/"){    _taboola.push({homepage:'auto'});  } else {    _taboola.push({article:'auto'});  }    !function (e, f, u, i) {      if (!document.getElementById(i)){        e.async = 1;        e.src = u;        e.id = i;        f.parentNode.insertBefore(e, f);      }    }(document.createElement('script'),    document.getElementsByTagName('script')[0],    '//cdn.taboola.com/libtrc/tupakiindia-tupakitelugu/loader.js',    'tb_loader_script');    if(window.performance && typeof window.performance.mark == 'function')      {window.performance.mark('tbl_ic');}
     </script>
     <script async="" src="https://t.seedtag.com/t/6537-0291-01.js">
     </script>
     <script async="" src="https://cdn.unibots.in/headerbidding/common/hb.js">
     </script>
     <script type="text/javascript">
      (function(){var o='script',s=top.document,a=s.createElement(o),m=s.getElementsByTagName(o)[0],d=new Date(),timestamp=""+d.getDate()+d.getMonth()+d.getHours();a.async=1;a.src='https://cdn4-hbs.affinitymatrix.com/hvrcnf/tupaki.com/'+ timestamp + '/index?t='+timestamp;m.parentNode.insertBefore(a,m)})();
     </script>
     <div id="v-tupaki-v6">
     </div>
     <script data-cfasync="false">
      (function(v,d,o,ai){ai=d.createElement('script');ai.defer=true;ai.async=true;ai.src=v.location.protocol+o;d.head.appendChild(ai);})(window, document, '//a.vdo.ai/core/v-tupaki-v6/vdo.ai.js');
     </script>
     <style class="styles" type="text/css">
      /*!
 * Bootstrap v3.4.1 (https://getbootstrap.com/)
 * Copyright 2011-2019 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 *//*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */html{font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}body{margin:0}article,aside,details,figcaption,figure,footer,header,hgroup,main,menu,nav,section,summary{display:block}audio,canvas,progress,video{display:inline-block;vertical-align:baseline}audio:not([controls]){display:none;height:0}[hidden],template{display:none}a{background-color:transparent}a:active,a:hover{outline:0}abbr[title]{border-bottom:none;text-decoration:underline;-webkit-text-decoration:underline dotted;-moz-text-decoration:underline dotted;text-decoration:underline dotted}b,strong{font-weight:700}dfn{font-style:italic}h1{font-size:2em;margin:.67em 0}mark{background:#ff0;color:#000}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}sup{top:-.5em}sub{bottom:-.25em}img{border:0}svg:not(:root){overflow:hidden}figure{margin:1em 40px}hr{-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box;height:0}pre{overflow:auto}code,kbd,pre,samp{font-family:monospace,monospace;font-size:1em}button,input,optgroup,select,textarea{color:inherit;font:inherit;margin:0}button{overflow:visible}button,select{text-transform:none}button,html input[type=button],input[type=reset],input[type=submit]{-webkit-appearance:button;cursor:pointer}button[disabled],html input[disabled]{cursor:default}button::-moz-focus-inner,input::-moz-focus-inner{border:0;padding:0}input{line-height:normal}input[type=checkbox],input[type=radio]{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;padding:0}input[type=number]::-webkit-inner-spin-button,input[type=number]::-webkit-outer-spin-button{height:auto}input[type=search]{-webkit-appearance:textfield;-webkit-box-sizing:content-box;-moz-box-sizing:content-box;box-sizing:content-box}input[type=search]::-webkit-search-cancel-button,input[type=search]::-webkit-search-decoration{-webkit-appearance:none}fieldset{border:1px solid silver;margin:0 2px;padding:.35em .625em .75em}legend{border:0;padding:0}textarea{overflow:auto}optgroup{font-weight:700}table{border-collapse:collapse;border-spacing:0}td,th{padding:0}/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */@media print{*,:after,:before{color:#000!important;text-shadow:none!important;background:0 0!important;-webkit-box-shadow:none!important;box-shadow:none!important}a,a:visited{text-decoration:underline}a[href]:after{content:" (" attr(href) ")"}abbr[title]:after{content:" (" attr(title) ")"}a[href^="#"]:after,a[href^="javascript:"]:after{content:""}blockquote,pre{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}img,tr{page-break-inside:avoid}img{max-width:100%!important}h2,h3,p{orphans:3;widows:3}h2,h3{page-break-after:avoid}.navbar{display:none}.btn>.caret,.dropup>.btn>.caret{border-top-color:#000!important}.label{border:1px solid #000}.table{border-collapse:collapse!important}.table td,.table th{background-color:#fff!important}.table-bordered td,.table-bordered th{border:1px solid #ddd!important}}@font-face{font-family:"Glyphicons Halflings";src:url(../fonts/glyphicons-halflings-regular.eot);src:url(../fonts/glyphicons-halflings-regular.eot?#iefix) format("embedded-opentype"),url(../fonts/glyphicons-halflings-regular.woff2) format("woff2"),url(../fonts/glyphicons-halflings-regular.woff) format("woff"),url(../fonts/glyphicons-halflings-regular.ttf) format("truetype"),url(../fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular) format("svg")}.glyphicon{position:relative;top:1px;display:inline-block;font-family:"Glyphicons Halflings";font-style:normal;font-weight:400;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.glyphicon-asterisk:before{content:"\002a"}.glyphicon-plus:before{content:"\002b"}.glyphicon-eur:before,.glyphicon-euro:before{content:"\20ac"}.glyphicon-minus:before{content:"\2212"}.glyphicon-cloud:before{content:"\2601"}.glyphicon-envelope:before{content:"\2709"}.glyphicon-pencil:before{content:"\270f"}.glyphicon-glass:before{content:"\e001"}.glyphicon-music:before{content:"\e002"}.glyphicon-search:before{content:"\e003"}.glyphicon-heart:before{content:"\e005"}.glyphicon-star:before{content:"\e006"}.glyphicon-star-empty:before{content:"\e007"}.glyphicon-user:before{content:"\e008"}.glyphicon-film:before{content:"\e009"}.glyphicon-th-large:before{content:"\e010"}.glyphicon-th:before{content:"\e011"}.glyphicon-th-list:before{content:"\e012"}.glyphicon-ok:before{content:"\e013"}.glyphicon-remove:before{content:"\e014"}.glyphicon-zoom-in:before{content:"\e015"}.glyphicon-zoom-out:before{content:"\e016"}.glyphicon-off:before{content:"\e017"}.glyphicon-signal:before{content:"\e018"}.glyphicon-cog:before{content:"\e019"}.glyphicon-trash:before{content:"\e020"}.glyphicon-home:before{content:"\e021"}.glyphicon-file:before{content:"\e022"}.glyphicon-time:before{content:"\e023"}.glyphicon-road:before{content:"\e024"}.glyphicon-download-alt:before{content:"\e025"}.glyphicon-download:before{content:"\e026"}.glyphicon-upload:before{content:"\e027"}.glyphicon-inbox:before{content:"\e028"}.glyphicon-play-circle:before{content:"\e029"}.glyphicon-repeat:before{content:"\e030"}.glyphicon-refresh:before{content:"\e031"}.glyphicon-list-alt:before{content:"\e032"}.glyphicon-lock:before{content:"\e033"}.glyphicon-flag:before{content:"\e034"}.glyphicon-headphones:before{content:"\e035"}.glyphicon-volume-off:before{content:"\e036"}.glyphicon-volume-down:before{content:"\e037"}.glyphicon-volume-up:before{content:"\e038"}.glyphicon-qrcode:before{content:"\e039"}.glyphicon-barcode:before{content:"\e040"}.glyphicon-tag:before{content:"\e041"}.glyphicon-tags:before{content:"\e042"}.glyphicon-book:before{content:"\e043"}.glyphicon-bookmark:before{content:"\e044"}.glyphicon-print:before{content:"\e045"}.glyphicon-camera:before{content:"\e046"}.glyphicon-font:before{content:"\e047"}.glyphicon-bold:before{content:"\e048"}.glyphicon-italic:before{content:"\e049"}.glyphicon-text-height:before{content:"\e050"}.glyphicon-text-width:before{content:"\e051"}.glyphicon-align-left:before{content:"\e052"}.glyphicon-align-center:before{content:"\e053"}.glyphicon-align-right:before{content:"\e054"}.glyphicon-align-justify:before{content:"\e055"}.glyphicon-list:before{content:"\e056"}.glyphicon-indent-left:before{content:"\e057"}.glyphicon-indent-right:before{content:"\e058"}.glyphicon-facetime-video:before{content:"\e059"}.glyphicon-picture:before{content:"\e060"}.glyphicon-map-marker:before{content:"\e062"}.glyphicon-adjust:before{content:"\e063"}.glyphicon-tint:before{content:"\e064"}.glyphicon-edit:before{content:"\e065"}.glyphicon-share:before{content:"\e066"}.glyphicon-check:before{content:"\e067"}.glyphicon-move:before{content:"\e068"}.glyphicon-step-backward:before{content:"\e069"}.glyphicon-fast-backward:before{content:"\e070"}.glyphicon-backward:before{content:"\e071"}.glyphicon-play:before{content:"\e072"}.glyphicon-pause:before{content:"\e073"}.glyphicon-stop:before{content:"\e074"}.glyphicon-forward:before{content:"\e075"}.glyphicon-fast-forward:before{content:"\e076"}.glyphicon-step-forward:before{content:"\e077"}.glyphicon-eject:before{content:"\e078"}.glyphicon-chevron-left:before{content:"\e079"}.glyphicon-chevron-right:before{content:"\e080"}.glyphicon-plus-sign:before{content:"\e081"}.glyphicon-minus-sign:before{content:"\e082"}.glyphicon-remove-sign:before{content:"\e083"}.glyphicon-ok-sign:before{content:"\e084"}.glyphicon-question-sign:before{content:"\e085"}.glyphicon-info-sign:before{content:"\e086"}.glyphicon-screenshot:before{content:"\e087"}.glyphicon-remove-circle:before{content:"\e088"}.glyphicon-ok-circle:before{content:"\e089"}.glyphicon-ban-circle:before{content:"\e090"}.glyphicon-arrow-left:before{content:"\e091"}.glyphicon-arrow-right:before{content:"\e092"}.glyphicon-arrow-up:before{content:"\e093"}.glyphicon-arrow-down:before{content:"\e094"}.glyphicon-share-alt:before{content:"\e095"}.glyphicon-resize-full:before{content:"\e096"}.glyphicon-resize-small:before{content:"\e097"}.glyphicon-exclamation-sign:before{content:"\e101"}.glyphicon-gift:before{content:"\e102"}.glyphicon-leaf:before{content:"\e103"}.glyphicon-fire:before{content:"\e104"}.glyphicon-eye-open:before{content:"\e105"}.glyphicon-eye-close:before{content:"\e106"}.glyphicon-warning-sign:before{content:"\e107"}.glyphicon-plane:before{content:"\e108"}.glyphicon-calendar:before{content:"\e109"}.glyphicon-random:before{content:"\e110"}.glyphicon-comment:before{content:"\e111"}.glyphicon-magnet:before{content:"\e112"}.glyphicon-chevron-up:before{content:"\e113"}.glyphicon-chevron-down:before{content:"\e114"}.glyphicon-retweet:before{content:"\e115"}.glyphicon-shopping-cart:before{content:"\e116"}.glyphicon-folder-close:before{content:"\e117"}.glyphicon-folder-open:before{content:"\e118"}.glyphicon-resize-vertical:before{content:"\e119"}.glyphicon-resize-horizontal:before{content:"\e120"}.glyphicon-hdd:before{content:"\e121"}.glyphicon-bullhorn:before{content:"\e122"}.glyphicon-bell:before{content:"\e123"}.glyphicon-certificate:before{content:"\e124"}.glyphicon-thumbs-up:before{content:"\e125"}.glyphicon-thumbs-down:before{content:"\e126"}.glyphicon-hand-right:before{content:"\e127"}.glyphicon-hand-left:before{content:"\e128"}.glyphicon-hand-up:before{content:"\e129"}.glyphicon-hand-down:before{content:"\e130"}.glyphicon-circle-arrow-right:before{content:"\e131"}.glyphicon-circle-arrow-left:before{content:"\e132"}.glyphicon-circle-arrow-up:before{content:"\e133"}.glyphicon-circle-arrow-down:before{content:"\e134"}.glyphicon-globe:before{content:"\e135"}.glyphicon-wrench:before{content:"\e136"}.glyphicon-tasks:before{content:"\e137"}.glyphicon-filter:before{content:"\e138"}.glyphicon-briefcase:before{content:"\e139"}.glyphicon-fullscreen:before{content:"\e140"}.glyphicon-dashboard:before{content:"\e141"}.glyphicon-paperclip:before{content:"\e142"}.glyphicon-heart-empty:before{content:"\e143"}.glyphicon-link:before{content:"\e144"}.glyphicon-phone:before{content:"\e145"}.glyphicon-pushpin:before{content:"\e146"}.glyphicon-usd:before{content:"\e148"}.glyphicon-gbp:before{content:"\e149"}.glyphicon-sort:before{content:"\e150"}.glyphicon-sort-by-alphabet:before{content:"\e151"}.glyphicon-sort-by-alphabet-alt:before{content:"\e152"}.glyphicon-sort-by-order:before{content:"\e153"}.glyphicon-sort-by-order-alt:before{content:"\e154"}.glyphicon-sort-by-attributes:before{content:"\e155"}.glyphicon-sort-by-attributes-alt:before{content:"\e156"}.glyphicon-unchecked:before{content:"\e157"}.glyphicon-expand:before{content:"\e158"}.glyphicon-collapse-down:before{content:"\e159"}.glyphicon-collapse-up:before{content:"\e160"}.glyphicon-log-in:before{content:"\e161"}.glyphicon-flash:before{content:"\e162"}.glyphicon-log-out:before{content:"\e163"}.glyphicon-new-window:before{content:"\e164"}.glyphicon-record:before{content:"\e165"}.glyphicon-save:before{content:"\e166"}.glyphicon-open:before{content:"\e167"}.glyphicon-saved:before{content:"\e168"}.glyphicon-import:before{content:"\e169"}.glyphicon-export:before{content:"\e170"}.glyphicon-send:before{content:"\e171"}.glyphicon-floppy-disk:before{content:"\e172"}.glyphicon-floppy-saved:before{content:"\e173"}.glyphicon-floppy-remove:before{content:"\e174"}.glyphicon-floppy-save:before{content:"\e175"}.glyphicon-floppy-open:before{content:"\e176"}.glyphicon-credit-card:before{content:"\e177"}.glyphicon-transfer:before{content:"\e178"}.glyphicon-cutlery:before{content:"\e179"}.glyphicon-header:before{content:"\e180"}.glyphicon-compressed:before{content:"\e181"}.glyphicon-earphone:before{content:"\e182"}.glyphicon-phone-alt:before{content:"\e183"}.glyphicon-tower:before{content:"\e184"}.glyphicon-stats:before{content:"\e185"}.glyphicon-sd-video:before{content:"\e186"}.glyphicon-hd-video:before{content:"\e187"}.glyphicon-subtitles:before{content:"\e188"}.glyphicon-sound-stereo:before{content:"\e189"}.glyphicon-sound-dolby:before{content:"\e190"}.glyphicon-sound-5-1:before{content:"\e191"}.glyphicon-sound-6-1:before{content:"\e192"}.glyphicon-sound-7-1:before{content:"\e193"}.glyphicon-copyright-mark:before{content:"\e194"}.glyphicon-registration-mark:before{content:"\e195"}.glyphicon-cloud-download:before{content:"\e197"}.glyphicon-cloud-upload:before{content:"\e198"}.glyphicon-tree-conifer:before{content:"\e199"}.glyphicon-tree-deciduous:before{content:"\e200"}.glyphicon-cd:before{content:"\e201"}.glyphicon-save-file:before{content:"\e202"}.glyphicon-open-file:before{content:"\e203"}.glyphicon-level-up:before{content:"\e204"}.glyphicon-copy:before{content:"\e205"}.glyphicon-paste:before{content:"\e206"}.glyphicon-alert:before{content:"\e209"}.glyphicon-equalizer:before{content:"\e210"}.glyphicon-king:before{content:"\e211"}.glyphicon-queen:before{content:"\e212"}.glyphicon-pawn:before{content:"\e213"}.glyphicon-bishop:before{content:"\e214"}.glyphicon-knight:before{content:"\e215"}.glyphicon-baby-formula:before{content:"\e216"}.glyphicon-tent:before{content:"\26fa"}.glyphicon-blackboard:before{content:"\e218"}.glyphicon-bed:before{content:"\e219"}.glyphicon-apple:before{content:"\f8ff"}.glyphicon-erase:before{content:"\e221"}.glyphicon-hourglass:before{content:"\231b"}.glyphicon-lamp:before{content:"\e223"}.glyphicon-duplicate:before{content:"\e224"}.glyphicon-piggy-bank:before{content:"\e225"}.glyphicon-scissors:before{content:"\e226"}.glyphicon-bitcoin:before{content:"\e227"}.glyphicon-btc:before{content:"\e227"}.glyphicon-xbt:before{content:"\e227"}.glyphicon-yen:before{content:"\00a5"}.glyphicon-jpy:before{content:"\00a5"}.glyphicon-ruble:before{content:"\20bd"}.glyphicon-rub:before{content:"\20bd"}.glyphicon-scale:before{content:"\e230"}.glyphicon-ice-lolly:before{content:"\e231"}.glyphicon-ice-lolly-tasted:before{content:"\e232"}.glyphicon-education:before{content:"\e233"}.glyphicon-option-horizontal:before{content:"\e234"}.glyphicon-option-vertical:before{content:"\e235"}.glyphicon-menu-hamburger:before{content:"\e236"}.glyphicon-modal-window:before{content:"\e237"}.glyphicon-oil:before{content:"\e238"}.glyphicon-grain:before{content:"\e239"}.glyphicon-sunglasses:before{content:"\e240"}.glyphicon-text-size:before{content:"\e241"}.glyphicon-text-color:before{content:"\e242"}.glyphicon-text-background:before{content:"\e243"}.glyphicon-object-align-top:before{content:"\e244"}.glyphicon-object-align-bottom:before{content:"\e245"}.glyphicon-object-align-horizontal:before{content:"\e246"}.glyphicon-object-align-left:before{content:"\e247"}.glyphicon-object-align-vertical:before{content:"\e248"}.glyphicon-object-align-right:before{content:"\e249"}.glyphicon-triangle-right:before{content:"\e250"}.glyphicon-triangle-left:before{content:"\e251"}.glyphicon-triangle-bottom:before{content:"\e252"}.glyphicon-triangle-top:before{content:"\e253"}.glyphicon-console:before{content:"\e254"}.glyphicon-superscript:before{content:"\e255"}.glyphicon-subscript:before{content:"\e256"}.glyphicon-menu-left:before{content:"\e257"}.glyphicon-menu-right:before{content:"\e258"}.glyphicon-menu-down:before{content:"\e259"}.glyphicon-menu-up:before{content:"\e260"}*{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}:after,:before{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}html{font-size:10px;-webkit-tap-highlight-color:transparent}body{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:14px;line-height:1.42857143;color:#333;background-color:#fff}button,input,select,textarea{font-family:inherit;font-size:inherit;line-height:inherit}a{color:#337ab7;text-decoration:none}a:focus,a:hover{color:#23527c;text-decoration:underline}a:focus{outline:5px auto -webkit-focus-ring-color;outline-offset:-2px}figure{margin:0}img{vertical-align:middle}.carousel-inner>.item>a>img,.carousel-inner>.item>img,.img-responsive,.thumbnail a>img,.thumbnail>img{display:block;max-width:100%;height:auto}.img-rounded{border-radius:6px}.img-thumbnail{padding:4px;line-height:1.42857143;background-color:#fff;border:1px solid #ddd;border-radius:4px;-webkit-transition:all .2s ease-in-out;-o-transition:all .2s ease-in-out;transition:all .2s ease-in-out;display:inline-block;max-width:100%;height:auto}.img-circle{border-radius:50%}hr{margin-top:20px;margin-bottom:20px;border:0;border-top:1px solid #eee}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);border:0}.sr-only-focusable:active,.sr-only-focusable:focus{position:static;width:auto;height:auto;margin:0;overflow:visible;clip:auto}[role=button]{cursor:pointer}.h1,.h2,.h3,.h4,.h5,.h6,h1,h2,h3,h4,h5,h6{font-family:inherit;font-weight:500;line-height:1.1;color:inherit}.h1 .small,.h1 small,.h2 .small,.h2 small,.h3 .small,.h3 small,.h4 .small,.h4 small,.h5 .small,.h5 small,.h6 .small,.h6 small,h1 .small,h1 small,h2 .small,h2 small,h3 .small,h3 small,h4 .small,h4 small,h5 .small,h5 small,h6 .small,h6 small{font-weight:400;line-height:1;color:#777}.h1,.h2,.h3,h1,h2,h3{margin-top:20px;margin-bottom:10px}.h1 .small,.h1 small,.h2 .small,.h2 small,.h3 .small,.h3 small,h1 .small,h1 small,h2 .small,h2 small,h3 .small,h3 small{font-size:65%}.h4,.h5,.h6,h4,h5,h6{margin-top:10px;margin-bottom:10px}.h4 .small,.h4 small,.h5 .small,.h5 small,.h6 .small,.h6 small,h4 .small,h4 small,h5 .small,h5 small,h6 .small,h6 small{font-size:75%}.h1,h1{font-size:36px}.h2,h2{font-size:30px}.h3,h3{font-size:24px}.h4,h4{font-size:18px}.h5,h5{font-size:14px}.h6,h6{font-size:12px}p{margin:0 0 10px}.lead{margin-bottom:20px;font-size:16px;font-weight:300;line-height:1.4}@media (min-width:768px){.lead{font-size:21px}}.small,small{font-size:85%}.mark,mark{padding:.2em;background-color:#fcf8e3}.text-left{text-align:left}.text-right{text-align:right}.text-center{text-align:center}.text-justify{text-align:justify}.text-nowrap{white-space:nowrap}.text-lowercase{text-transform:lowercase}.text-uppercase{text-transform:uppercase}.text-capitalize{text-transform:capitalize}.text-muted{color:#777}.text-primary{color:#337ab7}a.text-primary:focus,a.text-primary:hover{color:#286090}.text-success{color:#3c763d}a.text-success:focus,a.text-success:hover{color:#2b542c}.text-info{color:#31708f}a.text-info:focus,a.text-info:hover{color:#245269}.text-warning{color:#8a6d3b}a.text-warning:focus,a.text-warning:hover{color:#66512c}.text-danger{color:#a94442}a.text-danger:focus,a.text-danger:hover{color:#843534}.bg-primary{color:#fff;background-color:#337ab7}a.bg-primary:focus,a.bg-primary:hover{background-color:#286090}.bg-success{background-color:#dff0d8}a.bg-success:focus,a.bg-success:hover{background-color:#c1e2b3}.bg-info{background-color:#d9edf7}a.bg-info:focus,a.bg-info:hover{background-color:#afd9ee}.bg-warning{background-color:#fcf8e3}a.bg-warning:focus,a.bg-warning:hover{background-color:#f7ecb5}.bg-danger{background-color:#f2dede}a.bg-danger:focus,a.bg-danger:hover{background-color:#e4b9b9}.page-header{padding-bottom:9px;margin:40px 0 20px;border-bottom:1px solid #eee}ol,ul{margin-top:0;margin-bottom:10px}ol ol,ol ul,ul ol,ul ul{margin-bottom:0}.list-unstyled{padding-left:0;list-style:none}.list-inline{padding-left:0;list-style:none;margin-left:-5px}.list-inline>li{display:inline-block;padding-right:5px;padding-left:5px}dl{margin-top:0;margin-bottom:20px}dd,dt{line-height:1.42857143}dt{font-weight:700}dd{margin-left:0}@media (min-width:768px){.dl-horizontal dt{float:left;width:160px;clear:left;text-align:right;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.dl-horizontal dd{margin-left:180px}}abbr[data-original-title],abbr[title]{cursor:help}.initialism{font-size:90%;text-transform:uppercase}blockquote{padding:10px 20px;margin:0 0 20px;font-size:17.5px;border-left:5px solid #eee}blockquote ol:last-child,blockquote p:last-child,blockquote ul:last-child{margin-bottom:0}blockquote .small,blockquote footer,blockquote small{display:block;font-size:80%;line-height:1.42857143;color:#777}blockquote .small:before,blockquote footer:before,blockquote small:before{content:"\2014 \00A0"}.blockquote-reverse,blockquote.pull-right{padding-right:15px;padding-left:0;text-align:right;border-right:5px solid #eee;border-left:0}.blockquote-reverse .small:before,.blockquote-reverse footer:before,.blockquote-reverse small:before,blockquote.pull-right .small:before,blockquote.pull-right footer:before,blockquote.pull-right small:before{content:""}.blockquote-reverse .small:after,.blockquote-reverse footer:after,.blockquote-reverse small:after,blockquote.pull-right .small:after,blockquote.pull-right footer:after,blockquote.pull-right small:after{content:"\00A0 \2014"}address{margin-bottom:20px;font-style:normal;line-height:1.42857143}code,kbd,pre,samp{font-family:Menlo,Monaco,Consolas,"Courier New",monospace}code{padding:2px 4px;font-size:90%;color:#c7254e;background-color:#f9f2f4;border-radius:4px}kbd{padding:2px 4px;font-size:90%;color:#fff;background-color:#333;border-radius:3px;-webkit-box-shadow:inset 0 -1px 0 rgba(0,0,0,.25);box-shadow:inset 0 -1px 0 rgba(0,0,0,.25)}kbd kbd{padding:0;font-size:100%;font-weight:700;-webkit-box-shadow:none;box-shadow:none}pre{display:block;padding:9.5px;margin:0 0 10px;font-size:13px;line-height:1.42857143;color:#333;word-break:break-all;word-wrap:break-word;background-color:#f5f5f5;border:1px solid #ccc;border-radius:4px}pre code{padding:0;font-size:inherit;color:inherit;white-space:pre-wrap;background-color:transparent;border-radius:0}.pre-scrollable{max-height:340px;overflow-y:scroll}.container{padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}@media (min-width:768px){.container{width:750px}}@media (min-width:992px){.container{width:970px}}@media (min-width:1200px){.container{width:1170px}}.container-fluid{padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}.row{margin-right:-15px;margin-left:-15px}.row-no-gutters{margin-right:0;margin-left:0}.row-no-gutters [class*=col-]{padding-right:0;padding-left:0}.col-lg-1,.col-lg-10,.col-lg-11,.col-lg-12,.col-lg-2,.col-lg-3,.col-lg-4,.col-lg-5,.col-lg-6,.col-lg-7,.col-lg-8,.col-lg-9,.col-md-1,.col-md-10,.col-md-11,.col-md-12,.col-md-2,.col-md-3,.col-md-4,.col-md-5,.col-md-6,.col-md-7,.col-md-8,.col-md-9,.col-sm-1,.col-sm-10,.col-sm-11,.col-sm-12,.col-sm-2,.col-sm-3,.col-sm-4,.col-sm-5,.col-sm-6,.col-sm-7,.col-sm-8,.col-sm-9,.col-xs-1,.col-xs-10,.col-xs-11,.col-xs-12,.col-xs-2,.col-xs-3,.col-xs-4,.col-xs-5,.col-xs-6,.col-xs-7,.col-xs-8,.col-xs-9{position:relative;min-height:1px;padding-right:15px;padding-left:15px}.col-xs-1,.col-xs-10,.col-xs-11,.col-xs-12,.col-xs-2,.col-xs-3,.col-xs-4,.col-xs-5,.col-xs-6,.col-xs-7,.col-xs-8,.col-xs-9{float:left}.col-xs-12{width:100%}.col-xs-11{width:91.66666667%}.col-xs-10{width:83.33333333%}.col-xs-9{width:75%}.col-xs-8{width:66.66666667%}.col-xs-7{width:58.33333333%}.col-xs-6{width:50%}.col-xs-5{width:41.66666667%}.col-xs-4{width:33.33333333%}.col-xs-3{width:25%}.col-xs-2{width:16.66666667%}.col-xs-1{width:8.33333333%}.col-xs-pull-12{right:100%}.col-xs-pull-11{right:91.66666667%}.col-xs-pull-10{right:83.33333333%}.col-xs-pull-9{right:75%}.col-xs-pull-8{right:66.66666667%}.col-xs-pull-7{right:58.33333333%}.col-xs-pull-6{right:50%}.col-xs-pull-5{right:41.66666667%}.col-xs-pull-4{right:33.33333333%}.col-xs-pull-3{right:25%}.col-xs-pull-2{right:16.66666667%}.col-xs-pull-1{right:8.33333333%}.col-xs-pull-0{right:auto}.col-xs-push-12{left:100%}.col-xs-push-11{left:91.66666667%}.col-xs-push-10{left:83.33333333%}.col-xs-push-9{left:75%}.col-xs-push-8{left:66.66666667%}.col-xs-push-7{left:58.33333333%}.col-xs-push-6{left:50%}.col-xs-push-5{left:41.66666667%}.col-xs-push-4{left:33.33333333%}.col-xs-push-3{left:25%}.col-xs-push-2{left:16.66666667%}.col-xs-push-1{left:8.33333333%}.col-xs-push-0{left:auto}.col-xs-offset-12{margin-left:100%}.col-xs-offset-11{margin-left:91.66666667%}.col-xs-offset-10{margin-left:83.33333333%}.col-xs-offset-9{margin-left:75%}.col-xs-offset-8{margin-left:66.66666667%}.col-xs-offset-7{margin-left:58.33333333%}.col-xs-offset-6{margin-left:50%}.col-xs-offset-5{margin-left:41.66666667%}.col-xs-offset-4{margin-left:33.33333333%}.col-xs-offset-3{margin-left:25%}.col-xs-offset-2{margin-left:16.66666667%}.col-xs-offset-1{margin-left:8.33333333%}.col-xs-offset-0{margin-left:0}@media (min-width:768px){.col-sm-1,.col-sm-10,.col-sm-11,.col-sm-12,.col-sm-2,.col-sm-3,.col-sm-4,.col-sm-5,.col-sm-6,.col-sm-7,.col-sm-8,.col-sm-9{float:left}.col-sm-12{width:100%}.col-sm-11{width:91.66666667%}.col-sm-10{width:83.33333333%}.col-sm-9{width:75%}.col-sm-8{width:66.66666667%}.col-sm-7{width:58.33333333%}.col-sm-6{width:50%}.col-sm-5{width:41.66666667%}.col-sm-4{width:33.33333333%}.col-sm-3{width:25%}.col-sm-2{width:16.66666667%}.col-sm-1{width:8.33333333%}.col-sm-pull-12{right:100%}.col-sm-pull-11{right:91.66666667%}.col-sm-pull-10{right:83.33333333%}.col-sm-pull-9{right:75%}.col-sm-pull-8{right:66.66666667%}.col-sm-pull-7{right:58.33333333%}.col-sm-pull-6{right:50%}.col-sm-pull-5{right:41.66666667%}.col-sm-pull-4{right:33.33333333%}.col-sm-pull-3{right:25%}.col-sm-pull-2{right:16.66666667%}.col-sm-pull-1{right:8.33333333%}.col-sm-pull-0{right:auto}.col-sm-push-12{left:100%}.col-sm-push-11{left:91.66666667%}.col-sm-push-10{left:83.33333333%}.col-sm-push-9{left:75%}.col-sm-push-8{left:66.66666667%}.col-sm-push-7{left:58.33333333%}.col-sm-push-6{left:50%}.col-sm-push-5{left:41.66666667%}.col-sm-push-4{left:33.33333333%}.col-sm-push-3{left:25%}.col-sm-push-2{left:16.66666667%}.col-sm-push-1{left:8.33333333%}.col-sm-push-0{left:auto}.col-sm-offset-12{margin-left:100%}.col-sm-offset-11{margin-left:91.66666667%}.col-sm-offset-10{margin-left:83.33333333%}.col-sm-offset-9{margin-left:75%}.col-sm-offset-8{margin-left:66.66666667%}.col-sm-offset-7{margin-left:58.33333333%}.col-sm-offset-6{margin-left:50%}.col-sm-offset-5{margin-left:41.66666667%}.col-sm-offset-4{margin-left:33.33333333%}.col-sm-offset-3{margin-left:25%}.col-sm-offset-2{margin-left:16.66666667%}.col-sm-offset-1{margin-left:8.33333333%}.col-sm-offset-0{margin-left:0}}@media (min-width:992px){.col-md-1,.col-md-10,.col-md-11,.col-md-12,.col-md-2,.col-md-3,.col-md-4,.col-md-5,.col-md-6,.col-md-7,.col-md-8,.col-md-9{float:left}.col-md-12{width:100%}.col-md-11{width:91.66666667%}.col-md-10{width:83.33333333%}.col-md-9{width:75%}.col-md-8{width:66.66666667%}.col-md-7{width:58.33333333%}.col-md-6{width:50%}.col-md-5{width:41.66666667%}.col-md-4{width:33.33333333%}.col-md-3{width:25%}.col-md-2{width:16.66666667%}.col-md-1{width:8.33333333%}.col-md-pull-12{right:100%}.col-md-pull-11{right:91.66666667%}.col-md-pull-10{right:83.33333333%}.col-md-pull-9{right:75%}.col-md-pull-8{right:66.66666667%}.col-md-pull-7{right:58.33333333%}.col-md-pull-6{right:50%}.col-md-pull-5{right:41.66666667%}.col-md-pull-4{right:33.33333333%}.col-md-pull-3{right:25%}.col-md-pull-2{right:16.66666667%}.col-md-pull-1{right:8.33333333%}.col-md-pull-0{right:auto}.col-md-push-12{left:100%}.col-md-push-11{left:91.66666667%}.col-md-push-10{left:83.33333333%}.col-md-push-9{left:75%}.col-md-push-8{left:66.66666667%}.col-md-push-7{left:58.33333333%}.col-md-push-6{left:50%}.col-md-push-5{left:41.66666667%}.col-md-push-4{left:33.33333333%}.col-md-push-3{left:25%}.col-md-push-2{left:16.66666667%}.col-md-push-1{left:8.33333333%}.col-md-push-0{left:auto}.col-md-offset-12{margin-left:100%}.col-md-offset-11{margin-left:91.66666667%}.col-md-offset-10{margin-left:83.33333333%}.col-md-offset-9{margin-left:75%}.col-md-offset-8{margin-left:66.66666667%}.col-md-offset-7{margin-left:58.33333333%}.col-md-offset-6{margin-left:50%}.col-md-offset-5{margin-left:41.66666667%}.col-md-offset-4{margin-left:33.33333333%}.col-md-offset-3{margin-left:25%}.col-md-offset-2{margin-left:16.66666667%}.col-md-offset-1{margin-left:8.33333333%}.col-md-offset-0{margin-left:0}}@media (min-width:1200px){.col-lg-1,.col-lg-10,.col-lg-11,.col-lg-12,.col-lg-2,.col-lg-3,.col-lg-4,.col-lg-5,.col-lg-6,.col-lg-7,.col-lg-8,.col-lg-9{float:left}.col-lg-12{width:100%}.col-lg-11{width:91.66666667%}.col-lg-10{width:83.33333333%}.col-lg-9{width:75%}.col-lg-8{width:66.66666667%}.col-lg-7{width:58.33333333%}.col-lg-6{width:50%}.col-lg-5{width:41.66666667%}.col-lg-4{width:33.33333333%}.col-lg-3{width:25%}.col-lg-2{width:16.66666667%}.col-lg-1{width:8.33333333%}.col-lg-pull-12{right:100%}.col-lg-pull-11{right:91.66666667%}.col-lg-pull-10{right:83.33333333%}.col-lg-pull-9{right:75%}.col-lg-pull-8{right:66.66666667%}.col-lg-pull-7{right:58.33333333%}.col-lg-pull-6{right:50%}.col-lg-pull-5{right:41.66666667%}.col-lg-pull-4{right:33.33333333%}.col-lg-pull-3{right:25%}.col-lg-pull-2{right:16.66666667%}.col-lg-pull-1{right:8.33333333%}.col-lg-pull-0{right:auto}.col-lg-push-12{left:100%}.col-lg-push-11{left:91.66666667%}.col-lg-push-10{left:83.33333333%}.col-lg-push-9{left:75%}.col-lg-push-8{left:66.66666667%}.col-lg-push-7{left:58.33333333%}.col-lg-push-6{left:50%}.col-lg-push-5{left:41.66666667%}.col-lg-push-4{left:33.33333333%}.col-lg-push-3{left:25%}.col-lg-push-2{left:16.66666667%}.col-lg-push-1{left:8.33333333%}.col-lg-push-0{left:auto}.col-lg-offset-12{margin-left:100%}.col-lg-offset-11{margin-left:91.66666667%}.col-lg-offset-10{margin-left:83.33333333%}.col-lg-offset-9{margin-left:75%}.col-lg-offset-8{margin-left:66.66666667%}.col-lg-offset-7{margin-left:58.33333333%}.col-lg-offset-6{margin-left:50%}.col-lg-offset-5{margin-left:41.66666667%}.col-lg-offset-4{margin-left:33.33333333%}.col-lg-offset-3{margin-left:25%}.col-lg-offset-2{margin-left:16.66666667%}.col-lg-offset-1{margin-left:8.33333333%}.col-lg-offset-0{margin-left:0}}table{background-color:transparent}table col[class*=col-]{position:static;display:table-column;float:none}table td[class*=col-],table th[class*=col-]{position:static;display:table-cell;float:none}caption{padding-top:8px;padding-bottom:8px;color:#777;text-align:left}th{text-align:left}.table{width:100%;max-width:100%;margin-bottom:20px}.table>tbody>tr>td,.table>tbody>tr>th,.table>tfoot>tr>td,.table>tfoot>tr>th,.table>thead>tr>td,.table>thead>tr>th{padding:8px;line-height:1.42857143;vertical-align:top;border-top:1px solid #ddd}.table>thead>tr>th{vertical-align:bottom;border-bottom:2px solid #ddd}.table>caption+thead>tr:first-child>td,.table>caption+thead>tr:first-child>th,.table>colgroup+thead>tr:first-child>td,.table>colgroup+thead>tr:first-child>th,.table>thead:first-child>tr:first-child>td,.table>thead:first-child>tr:first-child>th{border-top:0}.table>tbody+tbody{border-top:2px solid #ddd}.table .table{background-color:#fff}.table-condensed>tbody>tr>td,.table-condensed>tbody>tr>th,.table-condensed>tfoot>tr>td,.table-condensed>tfoot>tr>th,.table-condensed>thead>tr>td,.table-condensed>thead>tr>th{padding:5px}.table-bordered{border:1px solid #ddd}.table-bordered>tbody>tr>td,.table-bordered>tbody>tr>th,.table-bordered>tfoot>tr>td,.table-bordered>tfoot>tr>th,.table-bordered>thead>tr>td,.table-bordered>thead>tr>th{border:1px solid #ddd}.table-bordered>thead>tr>td,.table-bordered>thead>tr>th{border-bottom-width:2px}.table-striped>tbody>tr:nth-of-type(odd){background-color:#f9f9f9}.table-hover>tbody>tr:hover{background-color:#f5f5f5}.table>tbody>tr.active>td,.table>tbody>tr.active>th,.table>tbody>tr>td.active,.table>tbody>tr>th.active,.table>tfoot>tr.active>td,.table>tfoot>tr.active>th,.table>tfoot>tr>td.active,.table>tfoot>tr>th.active,.table>thead>tr.active>td,.table>thead>tr.active>th,.table>thead>tr>td.active,.table>thead>tr>th.active{background-color:#f5f5f5}.table-hover>tbody>tr.active:hover>td,.table-hover>tbody>tr.active:hover>th,.table-hover>tbody>tr:hover>.active,.table-hover>tbody>tr>td.active:hover,.table-hover>tbody>tr>th.active:hover{background-color:#e8e8e8}.table>tbody>tr.success>td,.table>tbody>tr.success>th,.table>tbody>tr>td.success,.table>tbody>tr>th.success,.table>tfoot>tr.success>td,.table>tfoot>tr.success>th,.table>tfoot>tr>td.success,.table>tfoot>tr>th.success,.table>thead>tr.success>td,.table>thead>tr.success>th,.table>thead>tr>td.success,.table>thead>tr>th.success{background-color:#dff0d8}.table-hover>tbody>tr.success:hover>td,.table-hover>tbody>tr.success:hover>th,.table-hover>tbody>tr:hover>.success,.table-hover>tbody>tr>td.success:hover,.table-hover>tbody>tr>th.success:hover{background-color:#d0e9c6}.table>tbody>tr.info>td,.table>tbody>tr.info>th,.table>tbody>tr>td.info,.table>tbody>tr>th.info,.table>tfoot>tr.info>td,.table>tfoot>tr.info>th,.table>tfoot>tr>td.info,.table>tfoot>tr>th.info,.table>thead>tr.info>td,.table>thead>tr.info>th,.table>thead>tr>td.info,.table>thead>tr>th.info{background-color:#d9edf7}.table-hover>tbody>tr.info:hover>td,.table-hover>tbody>tr.info:hover>th,.table-hover>tbody>tr:hover>.info,.table-hover>tbody>tr>td.info:hover,.table-hover>tbody>tr>th.info:hover{background-color:#c4e3f3}.table>tbody>tr.warning>td,.table>tbody>tr.warning>th,.table>tbody>tr>td.warning,.table>tbody>tr>th.warning,.table>tfoot>tr.warning>td,.table>tfoot>tr.warning>th,.table>tfoot>tr>td.warning,.table>tfoot>tr>th.warning,.table>thead>tr.warning>td,.table>thead>tr.warning>th,.table>thead>tr>td.warning,.table>thead>tr>th.warning{background-color:#fcf8e3}.table-hover>tbody>tr.warning:hover>td,.table-hover>tbody>tr.warning:hover>th,.table-hover>tbody>tr:hover>.warning,.table-hover>tbody>tr>td.warning:hover,.table-hover>tbody>tr>th.warning:hover{background-color:#faf2cc}.table>tbody>tr.danger>td,.table>tbody>tr.danger>th,.table>tbody>tr>td.danger,.table>tbody>tr>th.danger,.table>tfoot>tr.danger>td,.table>tfoot>tr.danger>th,.table>tfoot>tr>td.danger,.table>tfoot>tr>th.danger,.table>thead>tr.danger>td,.table>thead>tr.danger>th,.table>thead>tr>td.danger,.table>thead>tr>th.danger{background-color:#f2dede}.table-hover>tbody>tr.danger:hover>td,.table-hover>tbody>tr.danger:hover>th,.table-hover>tbody>tr:hover>.danger,.table-hover>tbody>tr>td.danger:hover,.table-hover>tbody>tr>th.danger:hover{background-color:#ebcccc}.table-responsive{min-height:.01%;overflow-x:auto}@media screen and (max-width:767px){.table-responsive{width:100%;margin-bottom:15px;overflow-y:hidden;-ms-overflow-style:-ms-autohiding-scrollbar;border:1px solid #ddd}.table-responsive>.table{margin-bottom:0}.table-responsive>.table>tbody>tr>td,.table-responsive>.table>tbody>tr>th,.table-responsive>.table>tfoot>tr>td,.table-responsive>.table>tfoot>tr>th,.table-responsive>.table>thead>tr>td,.table-responsive>.table>thead>tr>th{white-space:nowrap}.table-responsive>.table-bordered{border:0}.table-responsive>.table-bordered>tbody>tr>td:first-child,.table-responsive>.table-bordered>tbody>tr>th:first-child,.table-responsive>.table-bordered>tfoot>tr>td:first-child,.table-responsive>.table-bordered>tfoot>tr>th:first-child,.table-responsive>.table-bordered>thead>tr>td:first-child,.table-responsive>.table-bordered>thead>tr>th:first-child{border-left:0}.table-responsive>.table-bordered>tbody>tr>td:last-child,.table-responsive>.table-bordered>tbody>tr>th:last-child,.table-responsive>.table-bordered>tfoot>tr>td:last-child,.table-responsive>.table-bordered>tfoot>tr>th:last-child,.table-responsive>.table-bordered>thead>tr>td:last-child,.table-responsive>.table-bordered>thead>tr>th:last-child{border-right:0}.table-responsive>.table-bordered>tbody>tr:last-child>td,.table-responsive>.table-bordered>tbody>tr:last-child>th,.table-responsive>.table-bordered>tfoot>tr:last-child>td,.table-responsive>.table-bordered>tfoot>tr:last-child>th{border-bottom:0}}fieldset{min-width:0;padding:0;margin:0;border:0}legend{display:block;width:100%;padding:0;margin-bottom:20px;font-size:21px;line-height:inherit;color:#333;border:0;border-bottom:1px solid #e5e5e5}label{display:inline-block;max-width:100%;margin-bottom:5px;font-weight:700}input[type=search]{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type=checkbox],input[type=radio]{margin:4px 0 0;line-height:normal}fieldset[disabled] input[type=checkbox],fieldset[disabled] input[type=radio],input[type=checkbox].disabled,input[type=checkbox][disabled],input[type=radio].disabled,input[type=radio][disabled]{cursor:not-allowed}input[type=file]{display:block}input[type=range]{display:block;width:100%}select[multiple],select[size]{height:auto}input[type=checkbox]:focus,input[type=file]:focus,input[type=radio]:focus{outline:5px auto -webkit-focus-ring-color;outline-offset:-2px}output{display:block;padding-top:7px;font-size:14px;line-height:1.42857143;color:#555}.form-control{display:block;width:100%;height:34px;padding:6px 12px;font-size:14px;line-height:1.42857143;color:#555;background-color:#fff;background-image:none;border:1px solid #ccc;border-radius:4px;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075);-webkit-transition:border-color ease-in-out .15s,box-shadow ease-in-out .15s;-o-transition:border-color ease-in-out .15s,box-shadow ease-in-out .15s;-webkit-transition:border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;transition:border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;transition:border-color ease-in-out .15s,box-shadow ease-in-out .15s;transition:border-color ease-in-out .15s,box-shadow ease-in-out .15s,-webkit-box-shadow ease-in-out .15s}.form-control:focus{border-color:#66afe9;outline:0;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 8px rgba(102,175,233,.6);box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 8px rgba(102,175,233,.6)}.form-control::-moz-placeholder{color:#999;opacity:1}.form-control:-ms-input-placeholder{color:#999}.form-control::-webkit-input-placeholder{color:#999}.form-control::-ms-expand{background-color:transparent;border:0}.form-control[disabled],.form-control[readonly],fieldset[disabled] .form-control{background-color:#eee;opacity:1}.form-control[disabled],fieldset[disabled] .form-control{cursor:not-allowed}textarea.form-control{height:auto}@media screen and (-webkit-min-device-pixel-ratio:0){input[type=date].form-control,input[type=datetime-local].form-control,input[type=month].form-control,input[type=time].form-control{line-height:34px}.input-group-sm input[type=date],.input-group-sm input[type=datetime-local],.input-group-sm input[type=month],.input-group-sm input[type=time],input[type=date].input-sm,input[type=datetime-local].input-sm,input[type=month].input-sm,input[type=time].input-sm{line-height:30px}.input-group-lg input[type=date],.input-group-lg input[type=datetime-local],.input-group-lg input[type=month],.input-group-lg input[type=time],input[type=date].input-lg,input[type=datetime-local].input-lg,input[type=month].input-lg,input[type=time].input-lg{line-height:46px}}.form-group{margin-bottom:15px}.checkbox,.radio{position:relative;display:block;margin-top:10px;margin-bottom:10px}.checkbox.disabled label,.radio.disabled label,fieldset[disabled] .checkbox label,fieldset[disabled] .radio label{cursor:not-allowed}.checkbox label,.radio label{min-height:20px;padding-left:20px;margin-bottom:0;font-weight:400;cursor:pointer}.checkbox input[type=checkbox],.checkbox-inline input[type=checkbox],.radio input[type=radio],.radio-inline input[type=radio]{position:absolute;margin-left:-20px}.checkbox+.checkbox,.radio+.radio{margin-top:-5px}.checkbox-inline,.radio-inline{position:relative;display:inline-block;padding-left:20px;margin-bottom:0;font-weight:400;vertical-align:middle;cursor:pointer}.checkbox-inline.disabled,.radio-inline.disabled,fieldset[disabled] .checkbox-inline,fieldset[disabled] .radio-inline{cursor:not-allowed}.checkbox-inline+.checkbox-inline,.radio-inline+.radio-inline{margin-top:0;margin-left:10px}.form-control-static{min-height:34px;padding-top:7px;padding-bottom:7px;margin-bottom:0}.form-control-static.input-lg,.form-control-static.input-sm{padding-right:0;padding-left:0}.input-sm{height:30px;padding:5px 10px;font-size:12px;line-height:1.5;border-radius:3px}select.input-sm{height:30px;line-height:30px}select[multiple].input-sm,textarea.input-sm{height:auto}.form-group-sm .form-control{height:30px;padding:5px 10px;font-size:12px;line-height:1.5;border-radius:3px}.form-group-sm select.form-control{height:30px;line-height:30px}.form-group-sm select[multiple].form-control,.form-group-sm textarea.form-control{height:auto}.form-group-sm .form-control-static{height:30px;min-height:32px;padding:6px 10px;font-size:12px;line-height:1.5}.input-lg{height:46px;padding:10px 16px;font-size:18px;line-height:1.3333333;border-radius:6px}select.input-lg{height:46px;line-height:46px}select[multiple].input-lg,textarea.input-lg{height:auto}.form-group-lg .form-control{height:46px;padding:10px 16px;font-size:18px;line-height:1.3333333;border-radius:6px}.form-group-lg select.form-control{height:46px;line-height:46px}.form-group-lg select[multiple].form-control,.form-group-lg textarea.form-control{height:auto}.form-group-lg .form-control-static{height:46px;min-height:38px;padding:11px 16px;font-size:18px;line-height:1.3333333}.has-feedback{position:relative}.has-feedback .form-control{padding-right:42.5px}.form-control-feedback{position:absolute;top:0;right:0;z-index:2;display:block;width:34px;height:34px;line-height:34px;text-align:center;pointer-events:none}.form-group-lg .form-control+.form-control-feedback,.input-group-lg+.form-control-feedback,.input-lg+.form-control-feedback{width:46px;height:46px;line-height:46px}.form-group-sm .form-control+.form-control-feedback,.input-group-sm+.form-control-feedback,.input-sm+.form-control-feedback{width:30px;height:30px;line-height:30px}.has-success .checkbox,.has-success .checkbox-inline,.has-success .control-label,.has-success .help-block,.has-success .radio,.has-success .radio-inline,.has-success.checkbox label,.has-success.checkbox-inline label,.has-success.radio label,.has-success.radio-inline label{color:#3c763d}.has-success .form-control{border-color:#3c763d;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075)}.has-success .form-control:focus{border-color:#2b542c;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 6px #67b168;box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 6px #67b168}.has-success .input-group-addon{color:#3c763d;background-color:#dff0d8;border-color:#3c763d}.has-success .form-control-feedback{color:#3c763d}.has-warning .checkbox,.has-warning .checkbox-inline,.has-warning .control-label,.has-warning .help-block,.has-warning .radio,.has-warning .radio-inline,.has-warning.checkbox label,.has-warning.checkbox-inline label,.has-warning.radio label,.has-warning.radio-inline label{color:#8a6d3b}.has-warning .form-control{border-color:#8a6d3b;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075)}.has-warning .form-control:focus{border-color:#66512c;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 6px #c0a16b;box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 6px #c0a16b}.has-warning .input-group-addon{color:#8a6d3b;background-color:#fcf8e3;border-color:#8a6d3b}.has-warning .form-control-feedback{color:#8a6d3b}.has-error .checkbox,.has-error .checkbox-inline,.has-error .control-label,.has-error .help-block,.has-error .radio,.has-error .radio-inline,.has-error.checkbox label,.has-error.checkbox-inline label,.has-error.radio label,.has-error.radio-inline label{color:#a94442}.has-error .form-control{border-color:#a94442;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075);box-shadow:inset 0 1px 1px rgba(0,0,0,.075)}.has-error .form-control:focus{border-color:#843534;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 6px #ce8483;box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 6px #ce8483}.has-error .input-group-addon{color:#a94442;background-color:#f2dede;border-color:#a94442}.has-error .form-control-feedback{color:#a94442}.has-feedback label~.form-control-feedback{top:25px}.has-feedback label.sr-only~.form-control-feedback{top:0}.help-block{display:block;margin-top:5px;margin-bottom:10px;color:#737373}@media (min-width:768px){.form-inline .form-group{display:inline-block;margin-bottom:0;vertical-align:middle}.form-inline .form-control{display:inline-block;width:auto;vertical-align:middle}.form-inline .form-control-static{display:inline-block}.form-inline .input-group{display:inline-table;vertical-align:middle}.form-inline .input-group .form-control,.form-inline .input-group .input-group-addon,.form-inline .input-group .input-group-btn{width:auto}.form-inline .input-group>.form-control{width:100%}.form-inline .control-label{margin-bottom:0;vertical-align:middle}.form-inline .checkbox,.form-inline .radio{display:inline-block;margin-top:0;margin-bottom:0;vertical-align:middle}.form-inline .checkbox label,.form-inline .radio label{padding-left:0}.form-inline .checkbox input[type=checkbox],.form-inline .radio input[type=radio]{position:relative;margin-left:0}.form-inline .has-feedback .form-control-feedback{top:0}}.form-horizontal .checkbox,.form-horizontal .checkbox-inline,.form-horizontal .radio,.form-horizontal .radio-inline{padding-top:7px;margin-top:0;margin-bottom:0}.form-horizontal .checkbox,.form-horizontal .radio{min-height:27px}.form-horizontal .form-group{margin-right:-15px;margin-left:-15px}@media (min-width:768px){.form-horizontal .control-label{padding-top:7px;margin-bottom:0;text-align:right}}.form-horizontal .has-feedback .form-control-feedback{right:15px}@media (min-width:768px){.form-horizontal .form-group-lg .control-label{padding-top:11px;font-size:18px}}@media (min-width:768px){.form-horizontal .form-group-sm .control-label{padding-top:6px;font-size:12px}}.btn{display:inline-block;margin-bottom:0;font-weight:400;text-align:center;white-space:nowrap;vertical-align:middle;-ms-touch-action:manipulation;touch-action:manipulation;cursor:pointer;background-image:none;border:1px solid transparent;padding:6px 12px;font-size:14px;line-height:1.42857143;border-radius:4px;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.btn.active.focus,.btn.active:focus,.btn.focus,.btn:active.focus,.btn:active:focus,.btn:focus{outline:5px auto -webkit-focus-ring-color;outline-offset:-2px}.btn.focus,.btn:focus,.btn:hover{color:#333;text-decoration:none}.btn.active,.btn:active{background-image:none;outline:0;-webkit-box-shadow:inset 0 3px 5px rgba(0,0,0,.125);box-shadow:inset 0 3px 5px rgba(0,0,0,.125)}.btn.disabled,.btn[disabled],fieldset[disabled] .btn{cursor:not-allowed;opacity:.65;-webkit-box-shadow:none;box-shadow:none}a.btn.disabled,fieldset[disabled] a.btn{pointer-events:none}.btn-default{color:#333;background-color:#fff;border-color:#ccc}.btn-default.focus,.btn-default:focus{color:#333;background-color:#e6e6e6;border-color:#8c8c8c}.btn-default:hover{color:#333;background-color:#e6e6e6;border-color:#adadad}.btn-default.active,.btn-default:active,.open>.dropdown-toggle.btn-default{color:#333;background-color:#e6e6e6;background-image:none;border-color:#adadad}.btn-default.active.focus,.btn-default.active:focus,.btn-default.active:hover,.btn-default:active.focus,.btn-default:active:focus,.btn-default:active:hover,.open>.dropdown-toggle.btn-default.focus,.open>.dropdown-toggle.btn-default:focus,.open>.dropdown-toggle.btn-default:hover{color:#333;background-color:#d4d4d4;border-color:#8c8c8c}.btn-default.disabled.focus,.btn-default.disabled:focus,.btn-default.disabled:hover,.btn-default[disabled].focus,.btn-default[disabled]:focus,.btn-default[disabled]:hover,fieldset[disabled] .btn-default.focus,fieldset[disabled] .btn-default:focus,fieldset[disabled] .btn-default:hover{background-color:#fff;border-color:#ccc}.btn-default .badge{color:#fff;background-color:#333}.btn-primary{color:#fff;background-color:#337ab7;border-color:#2e6da4}.btn-primary.focus,.btn-primary:focus{color:#fff;background-color:#286090;border-color:#122b40}.btn-primary:hover{color:#fff;background-color:#286090;border-color:#204d74}.btn-primary.active,.btn-primary:active,.open>.dropdown-toggle.btn-primary{color:#fff;background-color:#286090;background-image:none;border-color:#204d74}.btn-primary.active.focus,.btn-primary.active:focus,.btn-primary.active:hover,.btn-primary:active.focus,.btn-primary:active:focus,.btn-primary:active:hover,.open>.dropdown-toggle.btn-primary.focus,.open>.dropdown-toggle.btn-primary:focus,.open>.dropdown-toggle.btn-primary:hover{color:#fff;background-color:#204d74;border-color:#122b40}.btn-primary.disabled.focus,.btn-primary.disabled:focus,.btn-primary.disabled:hover,.btn-primary[disabled].focus,.btn-primary[disabled]:focus,.btn-primary[disabled]:hover,fieldset[disabled] .btn-primary.focus,fieldset[disabled] .btn-primary:focus,fieldset[disabled] .btn-primary:hover{background-color:#337ab7;border-color:#2e6da4}.btn-primary .badge{color:#337ab7;background-color:#fff}.btn-success{color:#fff;background-color:#5cb85c;border-color:#4cae4c}.btn-success.focus,.btn-success:focus{color:#fff;background-color:#449d44;border-color:#255625}.btn-success:hover{color:#fff;background-color:#449d44;border-color:#398439}.btn-success.active,.btn-success:active,.open>.dropdown-toggle.btn-success{color:#fff;background-color:#449d44;background-image:none;border-color:#398439}.btn-success.active.focus,.btn-success.active:focus,.btn-success.active:hover,.btn-success:active.focus,.btn-success:active:focus,.btn-success:active:hover,.open>.dropdown-toggle.btn-success.focus,.open>.dropdown-toggle.btn-success:focus,.open>.dropdown-toggle.btn-success:hover{color:#fff;background-color:#398439;border-color:#255625}.btn-success.disabled.focus,.btn-success.disabled:focus,.btn-success.disabled:hover,.btn-success[disabled].focus,.btn-success[disabled]:focus,.btn-success[disabled]:hover,fieldset[disabled] .btn-success.focus,fieldset[disabled] .btn-success:focus,fieldset[disabled] .btn-success:hover{background-color:#5cb85c;border-color:#4cae4c}.btn-success .badge{color:#5cb85c;background-color:#fff}.btn-info{color:#fff;background-color:#5bc0de;border-color:#46b8da}.btn-info.focus,.btn-info:focus{color:#fff;background-color:#31b0d5;border-color:#1b6d85}.btn-info:hover{color:#fff;background-color:#31b0d5;border-color:#269abc}.btn-info.active,.btn-info:active,.open>.dropdown-toggle.btn-info{color:#fff;background-color:#31b0d5;background-image:none;border-color:#269abc}.btn-info.active.focus,.btn-info.active:focus,.btn-info.active:hover,.btn-info:active.focus,.btn-info:active:focus,.btn-info:active:hover,.open>.dropdown-toggle.btn-info.focus,.open>.dropdown-toggle.btn-info:focus,.open>.dropdown-toggle.btn-info:hover{color:#fff;background-color:#269abc;border-color:#1b6d85}.btn-info.disabled.focus,.btn-info.disabled:focus,.btn-info.disabled:hover,.btn-info[disabled].focus,.btn-info[disabled]:focus,.btn-info[disabled]:hover,fieldset[disabled] .btn-info.focus,fieldset[disabled] .btn-info:focus,fieldset[disabled] .btn-info:hover{background-color:#5bc0de;border-color:#46b8da}.btn-info .badge{color:#5bc0de;background-color:#fff}.btn-warning{color:#fff;background-color:#f0ad4e;border-color:#eea236}.btn-warning.focus,.btn-warning:focus{color:#fff;background-color:#ec971f;border-color:#985f0d}.btn-warning:hover{color:#fff;background-color:#ec971f;border-color:#d58512}.btn-warning.active,.btn-warning:active,.open>.dropdown-toggle.btn-warning{color:#fff;background-color:#ec971f;background-image:none;border-color:#d58512}.btn-warning.active.focus,.btn-warning.active:focus,.btn-warning.active:hover,.btn-warning:active.focus,.btn-warning:active:focus,.btn-warning:active:hover,.open>.dropdown-toggle.btn-warning.focus,.open>.dropdown-toggle.btn-warning:focus,.open>.dropdown-toggle.btn-warning:hover{color:#fff;background-color:#d58512;border-color:#985f0d}.btn-warning.disabled.focus,.btn-warning.disabled:focus,.btn-warning.disabled:hover,.btn-warning[disabled].focus,.btn-warning[disabled]:focus,.btn-warning[disabled]:hover,fieldset[disabled] .btn-warning.focus,fieldset[disabled] .btn-warning:focus,fieldset[disabled] .btn-warning:hover{background-color:#f0ad4e;border-color:#eea236}.btn-warning .badge{color:#f0ad4e;background-color:#fff}.btn-danger{color:#fff;background-color:#d9534f;border-color:#d43f3a}.btn-danger.focus,.btn-danger:focus{color:#fff;background-color:#c9302c;border-color:#761c19}.btn-danger:hover{color:#fff;background-color:#c9302c;border-color:#ac2925}.btn-danger.active,.btn-danger:active,.open>.dropdown-toggle.btn-danger{color:#fff;background-color:#c9302c;background-image:none;border-color:#ac2925}.btn-danger.active.focus,.btn-danger.active:focus,.btn-danger.active:hover,.btn-danger:active.focus,.btn-danger:active:focus,.btn-danger:active:hover,.open>.dropdown-toggle.btn-danger.focus,.open>.dropdown-toggle.btn-danger:focus,.open>.dropdown-toggle.btn-danger:hover{color:#fff;background-color:#ac2925;border-color:#761c19}.btn-danger.disabled.focus,.btn-danger.disabled:focus,.btn-danger.disabled:hover,.btn-danger[disabled].focus,.btn-danger[disabled]:focus,.btn-danger[disabled]:hover,fieldset[disabled] .btn-danger.focus,fieldset[disabled] .btn-danger:focus,fieldset[disabled] .btn-danger:hover{background-color:#d9534f;border-color:#d43f3a}.btn-danger .badge{color:#d9534f;background-color:#fff}.btn-link{font-weight:400;color:#337ab7;border-radius:0}.btn-link,.btn-link.active,.btn-link:active,.btn-link[disabled],fieldset[disabled] .btn-link{background-color:transparent;-webkit-box-shadow:none;box-shadow:none}.btn-link,.btn-link:active,.btn-link:focus,.btn-link:hover{border-color:transparent}.btn-link:focus,.btn-link:hover{color:#23527c;text-decoration:underline;background-color:transparent}.btn-link[disabled]:focus,.btn-link[disabled]:hover,fieldset[disabled] .btn-link:focus,fieldset[disabled] .btn-link:hover{color:#777;text-decoration:none}.btn-group-lg>.btn,.btn-lg{padding:10px 16px;font-size:18px;line-height:1.3333333;border-radius:6px}.btn-group-sm>.btn,.btn-sm{padding:5px 10px;font-size:12px;line-height:1.5;border-radius:3px}.btn-group-xs>.btn,.btn-xs{padding:1px 5px;font-size:12px;line-height:1.5;border-radius:3px}.btn-block{display:block;width:100%}.btn-block+.btn-block{margin-top:5px}input[type=button].btn-block,input[type=reset].btn-block,input[type=submit].btn-block{width:100%}.fade{opacity:0;-webkit-transition:opacity .15s linear;-o-transition:opacity .15s linear;transition:opacity .15s linear}.fade.in{opacity:1}.collapse{display:none}.collapse.in{display:block}tr.collapse.in{display:table-row}tbody.collapse.in{display:table-row-group}.collapsing{position:relative;height:0;overflow:hidden;-webkit-transition-property:height,visibility;-o-transition-property:height,visibility;transition-property:height,visibility;-webkit-transition-duration:.35s;-o-transition-duration:.35s;transition-duration:.35s;-webkit-transition-timing-function:ease;-o-transition-timing-function:ease;transition-timing-function:ease}.caret{display:inline-block;width:0;height:0;margin-left:2px;vertical-align:middle;border-top:4px dashed;border-right:4px solid transparent;border-left:4px solid transparent}.dropdown,.dropup{position:relative}.dropdown-toggle:focus{outline:0}.dropdown-menu{position:absolute;top:100%;left:0;z-index:1000;display:none;float:left;min-width:160px;padding:5px 0;margin:2px 0 0;font-size:14px;text-align:left;list-style:none;background-color:#fff;background-clip:padding-box;border:1px solid #ccc;border:1px solid rgba(0,0,0,.15);border-radius:4px;-webkit-box-shadow:0 6px 12px rgba(0,0,0,.175);box-shadow:0 6px 12px rgba(0,0,0,.175)}.dropdown-menu.pull-right{right:0;left:auto}.dropdown-menu .divider{height:1px;margin:9px 0;overflow:hidden;background-color:#e5e5e5}.dropdown-menu>li>a{display:block;padding:3px 20px;clear:both;font-weight:400;line-height:1.42857143;color:#333;white-space:nowrap}.dropdown-menu>li>a:focus,.dropdown-menu>li>a:hover{color:#262626;text-decoration:none;background-color:#f5f5f5}.dropdown-menu>.active>a,.dropdown-menu>.active>a:focus,.dropdown-menu>.active>a:hover{color:#fff;text-decoration:none;background-color:#337ab7;outline:0}.dropdown-menu>.disabled>a,.dropdown-menu>.disabled>a:focus,.dropdown-menu>.disabled>a:hover{color:#777}.dropdown-menu>.disabled>a:focus,.dropdown-menu>.disabled>a:hover{text-decoration:none;cursor:not-allowed;background-color:transparent;background-image:none}.open>.dropdown-menu{display:block}.open>a{outline:0}.dropdown-menu-right{right:0;left:auto}.dropdown-menu-left{right:auto;left:0}.dropdown-header{display:block;padding:3px 20px;font-size:12px;line-height:1.42857143;color:#777;white-space:nowrap}.dropdown-backdrop{position:fixed;top:0;right:0;bottom:0;left:0;z-index:990}.pull-right>.dropdown-menu{right:0;left:auto}.dropup .caret,.navbar-fixed-bottom .dropdown .caret{content:"";border-top:0;border-bottom:4px dashed}.dropup .dropdown-menu,.navbar-fixed-bottom .dropdown .dropdown-menu{top:auto;bottom:100%;margin-bottom:2px}@media (min-width:768px){.navbar-right .dropdown-menu{right:0;left:auto}.navbar-right .dropdown-menu-left{right:auto;left:0}}.btn-group,.btn-group-vertical{position:relative;display:inline-block;vertical-align:middle}.btn-group-vertical>.btn,.btn-group>.btn{position:relative;float:left}.btn-group-vertical>.btn.active,.btn-group-vertical>.btn:active,.btn-group-vertical>.btn:focus,.btn-group-vertical>.btn:hover,.btn-group>.btn.active,.btn-group>.btn:active,.btn-group>.btn:focus,.btn-group>.btn:hover{z-index:2}.btn-group .btn+.btn,.btn-group .btn+.btn-group,.btn-group .btn-group+.btn,.btn-group .btn-group+.btn-group{margin-left:-1px}.btn-toolbar{margin-left:-5px}.btn-toolbar .btn,.btn-toolbar .btn-group,.btn-toolbar .input-group{float:left}.btn-toolbar>.btn,.btn-toolbar>.btn-group,.btn-toolbar>.input-group{margin-left:5px}.btn-group>.btn:not(:first-child):not(:last-child):not(.dropdown-toggle){border-radius:0}.btn-group>.btn:first-child{margin-left:0}.btn-group>.btn:first-child:not(:last-child):not(.dropdown-toggle){border-top-right-radius:0;border-bottom-right-radius:0}.btn-group>.btn:last-child:not(:first-child),.btn-group>.dropdown-toggle:not(:first-child){border-top-left-radius:0;border-bottom-left-radius:0}.btn-group>.btn-group{float:left}.btn-group>.btn-group:not(:first-child):not(:last-child)>.btn{border-radius:0}.btn-group>.btn-group:first-child:not(:last-child)>.btn:last-child,.btn-group>.btn-group:first-child:not(:last-child)>.dropdown-toggle{border-top-right-radius:0;border-bottom-right-radius:0}.btn-group>.btn-group:last-child:not(:first-child)>.btn:first-child{border-top-left-radius:0;border-bottom-left-radius:0}.btn-group .dropdown-toggle:active,.btn-group.open .dropdown-toggle{outline:0}.btn-group>.btn+.dropdown-toggle{padding-right:8px;padding-left:8px}.btn-group>.btn-lg+.dropdown-toggle{padding-right:12px;padding-left:12px}.btn-group.open .dropdown-toggle{-webkit-box-shadow:inset 0 3px 5px rgba(0,0,0,.125);box-shadow:inset 0 3px 5px rgba(0,0,0,.125)}.btn-group.open .dropdown-toggle.btn-link{-webkit-box-shadow:none;box-shadow:none}.btn .caret{margin-left:0}.btn-lg .caret{border-width:5px 5px 0;border-bottom-width:0}.dropup .btn-lg .caret{border-width:0 5px 5px}.btn-group-vertical>.btn,.btn-group-vertical>.btn-group,.btn-group-vertical>.btn-group>.btn{display:block;float:none;width:100%;max-width:100%}.btn-group-vertical>.btn-group>.btn{float:none}.btn-group-vertical>.btn+.btn,.btn-group-vertical>.btn+.btn-group,.btn-group-vertical>.btn-group+.btn,.btn-group-vertical>.btn-group+.btn-group{margin-top:-1px;margin-left:0}.btn-group-vertical>.btn:not(:first-child):not(:last-child){border-radius:0}.btn-group-vertical>.btn:first-child:not(:last-child){border-top-left-radius:4px;border-top-right-radius:4px;border-bottom-right-radius:0;border-bottom-left-radius:0}.btn-group-vertical>.btn:last-child:not(:first-child){border-top-left-radius:0;border-top-right-radius:0;border-bottom-right-radius:4px;border-bottom-left-radius:4px}.btn-group-vertical>.btn-group:not(:first-child):not(:last-child)>.btn{border-radius:0}.btn-group-vertical>.btn-group:first-child:not(:last-child)>.btn:last-child,.btn-group-vertical>.btn-group:first-child:not(:last-child)>.dropdown-toggle{border-bottom-right-radius:0;border-bottom-left-radius:0}.btn-group-vertical>.btn-group:last-child:not(:first-child)>.btn:first-child{border-top-left-radius:0;border-top-right-radius:0}.btn-group-justified{display:table;width:100%;table-layout:fixed;border-collapse:separate}.btn-group-justified>.btn,.btn-group-justified>.btn-group{display:table-cell;float:none;width:1%}.btn-group-justified>.btn-group .btn{width:100%}.btn-group-justified>.btn-group .dropdown-menu{left:auto}[data-toggle=buttons]>.btn input[type=checkbox],[data-toggle=buttons]>.btn input[type=radio],[data-toggle=buttons]>.btn-group>.btn input[type=checkbox],[data-toggle=buttons]>.btn-group>.btn input[type=radio]{position:absolute;clip:rect(0,0,0,0);pointer-events:none}.input-group{position:relative;display:table;border-collapse:separate}.input-group[class*=col-]{float:none;padding-right:0;padding-left:0}.input-group .form-control{position:relative;z-index:2;float:left;width:100%;margin-bottom:0}.input-group .form-control:focus{z-index:3}.input-group-lg>.form-control,.input-group-lg>.input-group-addon,.input-group-lg>.input-group-btn>.btn{height:46px;padding:10px 16px;font-size:18px;line-height:1.3333333;border-radius:6px}select.input-group-lg>.form-control,select.input-group-lg>.input-group-addon,select.input-group-lg>.input-group-btn>.btn{height:46px;line-height:46px}select[multiple].input-group-lg>.form-control,select[multiple].input-group-lg>.input-group-addon,select[multiple].input-group-lg>.input-group-btn>.btn,textarea.input-group-lg>.form-control,textarea.input-group-lg>.input-group-addon,textarea.input-group-lg>.input-group-btn>.btn{height:auto}.input-group-sm>.form-control,.input-group-sm>.input-group-addon,.input-group-sm>.input-group-btn>.btn{height:30px;padding:5px 10px;font-size:12px;line-height:1.5;border-radius:3px}select.input-group-sm>.form-control,select.input-group-sm>.input-group-addon,select.input-group-sm>.input-group-btn>.btn{height:30px;line-height:30px}select[multiple].input-group-sm>.form-control,select[multiple].input-group-sm>.input-group-addon,select[multiple].input-group-sm>.input-group-btn>.btn,textarea.input-group-sm>.form-control,textarea.input-group-sm>.input-group-addon,textarea.input-group-sm>.input-group-btn>.btn{height:auto}.input-group .form-control,.input-group-addon,.input-group-btn{display:table-cell}.input-group .form-control:not(:first-child):not(:last-child),.input-group-addon:not(:first-child):not(:last-child),.input-group-btn:not(:first-child):not(:last-child){border-radius:0}.input-group-addon,.input-group-btn{width:1%;white-space:nowrap;vertical-align:middle}.input-group-addon{padding:6px 12px;font-size:14px;font-weight:400;line-height:1;color:#555;text-align:center;background-color:#eee;border:1px solid #ccc;border-radius:4px}.input-group-addon.input-sm{padding:5px 10px;font-size:12px;border-radius:3px}.input-group-addon.input-lg{padding:10px 16px;font-size:18px;border-radius:6px}.input-group-addon input[type=checkbox],.input-group-addon input[type=radio]{margin-top:0}.input-group .form-control:first-child,.input-group-addon:first-child,.input-group-btn:first-child>.btn,.input-group-btn:first-child>.btn-group>.btn,.input-group-btn:first-child>.dropdown-toggle,.input-group-btn:last-child>.btn-group:not(:last-child)>.btn,.input-group-btn:last-child>.btn:not(:last-child):not(.dropdown-toggle){border-top-right-radius:0;border-bottom-right-radius:0}.input-group-addon:first-child{border-right:0}.input-group .form-control:last-child,.input-group-addon:last-child,.input-group-btn:first-child>.btn-group:not(:first-child)>.btn,.input-group-btn:first-child>.btn:not(:first-child),.input-group-btn:last-child>.btn,.input-group-btn:last-child>.btn-group>.btn,.input-group-btn:last-child>.dropdown-toggle{border-top-left-radius:0;border-bottom-left-radius:0}.input-group-addon:last-child{border-left:0}.input-group-btn{position:relative;font-size:0;white-space:nowrap}.input-group-btn>.btn{position:relative}.input-group-btn>.btn+.btn{margin-left:-1px}.input-group-btn>.btn:active,.input-group-btn>.btn:focus,.input-group-btn>.btn:hover{z-index:2}.input-group-btn:first-child>.btn,.input-group-btn:first-child>.btn-group{margin-right:-1px}.input-group-btn:last-child>.btn,.input-group-btn:last-child>.btn-group{z-index:2;margin-left:-1px}.nav{padding-left:0;margin-bottom:0;list-style:none}.nav>li{position:relative;display:block}.nav>li>a{position:relative;display:block;padding:10px 15px}.nav>li>a:focus,.nav>li>a:hover{text-decoration:none;background-color:#eee}.nav>li.disabled>a{color:#777}.nav>li.disabled>a:focus,.nav>li.disabled>a:hover{color:#777;text-decoration:none;cursor:not-allowed;background-color:transparent}.nav .open>a,.nav .open>a:focus,.nav .open>a:hover{background-color:#eee;border-color:#337ab7}.nav .nav-divider{height:1px;margin:9px 0;overflow:hidden;background-color:#e5e5e5}.nav>li>a>img{max-width:none}.nav-tabs{border-bottom:1px solid #ddd}.nav-tabs>li{float:left;margin-bottom:-1px}.nav-tabs>li>a{margin-right:2px;line-height:1.42857143;border:1px solid transparent;border-radius:4px 4px 0 0}.nav-tabs>li>a:hover{border-color:#eee #eee #ddd}.nav-tabs>li.active>a,.nav-tabs>li.active>a:focus,.nav-tabs>li.active>a:hover{color:#555;cursor:default;background-color:#fff;border:1px solid #ddd;border-bottom-color:transparent}.nav-tabs.nav-justified{width:100%;border-bottom:0}.nav-tabs.nav-justified>li{float:none}.nav-tabs.nav-justified>li>a{margin-bottom:5px;text-align:center}.nav-tabs.nav-justified>.dropdown .dropdown-menu{top:auto;left:auto}@media (min-width:768px){.nav-tabs.nav-justified>li{display:table-cell;width:1%}.nav-tabs.nav-justified>li>a{margin-bottom:0}}.nav-tabs.nav-justified>li>a{margin-right:0;border-radius:4px}.nav-tabs.nav-justified>.active>a,.nav-tabs.nav-justified>.active>a:focus,.nav-tabs.nav-justified>.active>a:hover{border:1px solid #ddd}@media (min-width:768px){.nav-tabs.nav-justified>li>a{border-bottom:1px solid #ddd;border-radius:4px 4px 0 0}.nav-tabs.nav-justified>.active>a,.nav-tabs.nav-justified>.active>a:focus,.nav-tabs.nav-justified>.active>a:hover{border-bottom-color:#fff}}.nav-pills>li{float:left}.nav-pills>li>a{border-radius:4px}.nav-pills>li+li{margin-left:2px}.nav-pills>li.active>a,.nav-pills>li.active>a:focus,.nav-pills>li.active>a:hover{color:#fff;background-color:#337ab7}.nav-stacked>li{float:none}.nav-stacked>li+li{margin-top:2px;margin-left:0}.nav-justified{width:100%}.nav-justified>li{float:none}.nav-justified>li>a{margin-bottom:5px;text-align:center}.nav-justified>.dropdown .dropdown-menu{top:auto;left:auto}@media (min-width:768px){.nav-justified>li{display:table-cell;width:1%}.nav-justified>li>a{margin-bottom:0}}.nav-tabs-justified{border-bottom:0}.nav-tabs-justified>li>a{margin-right:0;border-radius:4px}.nav-tabs-justified>.active>a,.nav-tabs-justified>.active>a:focus,.nav-tabs-justified>.active>a:hover{border:1px solid #ddd}@media (min-width:768px){.nav-tabs-justified>li>a{border-bottom:1px solid #ddd;border-radius:4px 4px 0 0}.nav-tabs-justified>.active>a,.nav-tabs-justified>.active>a:focus,.nav-tabs-justified>.active>a:hover{border-bottom-color:#fff}}.tab-content>.tab-pane{display:none}.tab-content>.active{display:block}.nav-tabs .dropdown-menu{margin-top:-1px;border-top-left-radius:0;border-top-right-radius:0}.navbar{position:relative;min-height:50px;margin-bottom:20px;border:1px solid transparent}@media (min-width:768px){.navbar{border-radius:4px}}@media (min-width:768px){.navbar-header{float:left}}.navbar-collapse{padding-right:15px;padding-left:15px;overflow-x:visible;border-top:1px solid transparent;-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,.1);box-shadow:inset 0 1px 0 rgba(255,255,255,.1);-webkit-overflow-scrolling:touch}.navbar-collapse.in{overflow-y:auto}@media (min-width:768px){.navbar-collapse{width:auto;border-top:0;-webkit-box-shadow:none;box-shadow:none}.navbar-collapse.collapse{display:block!important;height:auto!important;padding-bottom:0;overflow:visible!important}.navbar-collapse.in{overflow-y:visible}.navbar-fixed-bottom .navbar-collapse,.navbar-fixed-top .navbar-collapse,.navbar-static-top .navbar-collapse{padding-right:0;padding-left:0}}.navbar-fixed-bottom,.navbar-fixed-top{position:fixed;right:0;left:0;z-index:1030}.navbar-fixed-bottom .navbar-collapse,.navbar-fixed-top .navbar-collapse{max-height:340px}@media (max-device-width:480px) and (orientation:landscape){.navbar-fixed-bottom .navbar-collapse,.navbar-fixed-top .navbar-collapse{max-height:200px}}@media (min-width:768px){.navbar-fixed-bottom,.navbar-fixed-top{border-radius:0}}.navbar-fixed-top{top:0;border-width:0 0 1px}.navbar-fixed-bottom{bottom:0;margin-bottom:0;border-width:1px 0 0}.container-fluid>.navbar-collapse,.container-fluid>.navbar-header,.container>.navbar-collapse,.container>.navbar-header{margin-right:-15px;margin-left:-15px}@media (min-width:768px){.container-fluid>.navbar-collapse,.container-fluid>.navbar-header,.container>.navbar-collapse,.container>.navbar-header{margin-right:0;margin-left:0}}.navbar-static-top{z-index:1000;border-width:0 0 1px}@media (min-width:768px){.navbar-static-top{border-radius:0}}.navbar-brand{float:left;height:50px;padding:15px 15px;font-size:18px;line-height:20px}.navbar-brand:focus,.navbar-brand:hover{text-decoration:none}.navbar-brand>img{display:block}@media (min-width:768px){.navbar>.container .navbar-brand,.navbar>.container-fluid .navbar-brand{margin-left:-15px}}.navbar-toggle{position:relative;float:right;padding:9px 10px;margin-right:15px;margin-top:8px;margin-bottom:8px;background-color:transparent;background-image:none;border:1px solid transparent;border-radius:4px}.navbar-toggle:focus{outline:0}.navbar-toggle .icon-bar{display:block;width:22px;height:2px;border-radius:1px}.navbar-toggle .icon-bar+.icon-bar{margin-top:4px}@media (min-width:768px){.navbar-toggle{display:none}}.navbar-nav{margin:7.5px -15px}.navbar-nav>li>a{padding-top:10px;padding-bottom:10px;line-height:20px}@media (max-width:767px){.navbar-nav .open .dropdown-menu{position:static;float:none;width:auto;margin-top:0;background-color:transparent;border:0;-webkit-box-shadow:none;box-shadow:none}.navbar-nav .open .dropdown-menu .dropdown-header,.navbar-nav .open .dropdown-menu>li>a{padding:5px 15px 5px 25px}.navbar-nav .open .dropdown-menu>li>a{line-height:20px}.navbar-nav .open .dropdown-menu>li>a:focus,.navbar-nav .open .dropdown-menu>li>a:hover{background-image:none}}@media (min-width:768px){.navbar-nav{float:left;margin:0}.navbar-nav>li{float:left}.navbar-nav>li>a{padding-top:15px;padding-bottom:15px}}.navbar-form{padding:10px 15px;margin-right:-15px;margin-left:-15px;border-top:1px solid transparent;border-bottom:1px solid transparent;-webkit-box-shadow:inset 0 1px 0 rgba(255,255,255,.1),0 1px 0 rgba(255,255,255,.1);box-shadow:inset 0 1px 0 rgba(255,255,255,.1),0 1px 0 rgba(255,255,255,.1);margin-top:8px;margin-bottom:8px}@media (min-width:768px){.navbar-form .form-group{display:inline-block;margin-bottom:0;vertical-align:middle}.navbar-form .form-control{display:inline-block;width:auto;vertical-align:middle}.navbar-form .form-control-static{display:inline-block}.navbar-form .input-group{display:inline-table;vertical-align:middle}.navbar-form .input-group .form-control,.navbar-form .input-group .input-group-addon,.navbar-form .input-group .input-group-btn{width:auto}.navbar-form .input-group>.form-control{width:100%}.navbar-form .control-label{margin-bottom:0;vertical-align:middle}.navbar-form .checkbox,.navbar-form .radio{display:inline-block;margin-top:0;margin-bottom:0;vertical-align:middle}.navbar-form .checkbox label,.navbar-form .radio label{padding-left:0}.navbar-form .checkbox input[type=checkbox],.navbar-form .radio input[type=radio]{position:relative;margin-left:0}.navbar-form .has-feedback .form-control-feedback{top:0}}@media (max-width:767px){.navbar-form .form-group{margin-bottom:5px}.navbar-form .form-group:last-child{margin-bottom:0}}@media (min-width:768px){.navbar-form{width:auto;padding-top:0;padding-bottom:0;margin-right:0;margin-left:0;border:0;-webkit-box-shadow:none;box-shadow:none}}.navbar-nav>li>.dropdown-menu{margin-top:0;border-top-left-radius:0;border-top-right-radius:0}.navbar-fixed-bottom .navbar-nav>li>.dropdown-menu{margin-bottom:0;border-top-left-radius:4px;border-top-right-radius:4px;border-bottom-right-radius:0;border-bottom-left-radius:0}.navbar-btn{margin-top:8px;margin-bottom:8px}.navbar-btn.btn-sm{margin-top:10px;margin-bottom:10px}.navbar-btn.btn-xs{margin-top:14px;margin-bottom:14px}.navbar-text{margin-top:15px;margin-bottom:15px}@media (min-width:768px){.navbar-text{float:left;margin-right:15px;margin-left:15px}}@media (min-width:768px){.navbar-left{float:left!important}.navbar-right{float:right!important;margin-right:-15px}.navbar-right~.navbar-right{margin-right:0}}.navbar-default{background-color:#f8f8f8;border-color:#e7e7e7}.navbar-default .navbar-brand{color:#777}.navbar-default .navbar-brand:focus,.navbar-default .navbar-brand:hover{color:#5e5e5e;background-color:transparent}.navbar-default .navbar-text{color:#777}.navbar-default .navbar-nav>li>a{color:#777}.navbar-default .navbar-nav>li>a:focus,.navbar-default .navbar-nav>li>a:hover{color:#333;background-color:transparent}.navbar-default .navbar-nav>.active>a,.navbar-default .navbar-nav>.active>a:focus,.navbar-default .navbar-nav>.active>a:hover{color:#555;background-color:#e7e7e7}.navbar-default .navbar-nav>.disabled>a,.navbar-default .navbar-nav>.disabled>a:focus,.navbar-default .navbar-nav>.disabled>a:hover{color:#ccc;background-color:transparent}.navbar-default .navbar-nav>.open>a,.navbar-default .navbar-nav>.open>a:focus,.navbar-default .navbar-nav>.open>a:hover{color:#555;background-color:#e7e7e7}@media (max-width:767px){.navbar-default .navbar-nav .open .dropdown-menu>li>a{color:#777}.navbar-default .navbar-nav .open .dropdown-menu>li>a:focus,.navbar-default .navbar-nav .open .dropdown-menu>li>a:hover{color:#333;background-color:transparent}.navbar-default .navbar-nav .open .dropdown-menu>.active>a,.navbar-default .navbar-nav .open .dropdown-menu>.active>a:focus,.navbar-default .navbar-nav .open .dropdown-menu>.active>a:hover{color:#555;background-color:#e7e7e7}.navbar-default .navbar-nav .open .dropdown-menu>.disabled>a,.navbar-default .navbar-nav .open .dropdown-menu>.disabled>a:focus,.navbar-default .navbar-nav .open .dropdown-menu>.disabled>a:hover{color:#ccc;background-color:transparent}}.navbar-default .navbar-toggle{border-color:#ddd}.navbar-default .navbar-toggle:focus,.navbar-default .navbar-toggle:hover{background-color:#ddd}.navbar-default .navbar-toggle .icon-bar{background-color:#888}.navbar-default .navbar-collapse,.navbar-default .navbar-form{border-color:#e7e7e7}.navbar-default .navbar-link{color:#777}.navbar-default .navbar-link:hover{color:#333}.navbar-default .btn-link{color:#777}.navbar-default .btn-link:focus,.navbar-default .btn-link:hover{color:#333}.navbar-default .btn-link[disabled]:focus,.navbar-default .btn-link[disabled]:hover,fieldset[disabled] .navbar-default .btn-link:focus,fieldset[disabled] .navbar-default .btn-link:hover{color:#ccc}.navbar-inverse{background-color:#222;border-color:#080808}.navbar-inverse .navbar-brand{color:#9d9d9d}.navbar-inverse .navbar-brand:focus,.navbar-inverse .navbar-brand:hover{color:#fff;background-color:transparent}.navbar-inverse .navbar-text{color:#9d9d9d}.navbar-inverse .navbar-nav>li>a{color:#9d9d9d}.navbar-inverse .navbar-nav>li>a:focus,.navbar-inverse .navbar-nav>li>a:hover{color:#fff;background-color:transparent}.navbar-inverse .navbar-nav>.active>a,.navbar-inverse .navbar-nav>.active>a:focus,.navbar-inverse .navbar-nav>.active>a:hover{color:#fff;background-color:#080808}.navbar-inverse .navbar-nav>.disabled>a,.navbar-inverse .navbar-nav>.disabled>a:focus,.navbar-inverse .navbar-nav>.disabled>a:hover{color:#444;background-color:transparent}.navbar-inverse .navbar-nav>.open>a,.navbar-inverse .navbar-nav>.open>a:focus,.navbar-inverse .navbar-nav>.open>a:hover{color:#fff;background-color:#080808}@media (max-width:767px){.navbar-inverse .navbar-nav .open .dropdown-menu>.dropdown-header{border-color:#080808}.navbar-inverse .navbar-nav .open .dropdown-menu .divider{background-color:#080808}.navbar-inverse .navbar-nav .open .dropdown-menu>li>a{color:#9d9d9d}.navbar-inverse .navbar-nav .open .dropdown-menu>li>a:focus,.navbar-inverse .navbar-nav .open .dropdown-menu>li>a:hover{color:#fff;background-color:transparent}.navbar-inverse .navbar-nav .open .dropdown-menu>.active>a,.navbar-inverse .navbar-nav .open .dropdown-menu>.active>a:focus,.navbar-inverse .navbar-nav .open .dropdown-menu>.active>a:hover{color:#fff;background-color:#080808}.navbar-inverse .navbar-nav .open .dropdown-menu>.disabled>a,.navbar-inverse .navbar-nav .open .dropdown-menu>.disabled>a:focus,.navbar-inverse .navbar-nav .open .dropdown-menu>.disabled>a:hover{color:#444;background-color:transparent}}.navbar-inverse .navbar-toggle{border-color:#333}.navbar-inverse .navbar-toggle:focus,.navbar-inverse .navbar-toggle:hover{background-color:#333}.navbar-inverse .navbar-toggle .icon-bar{background-color:#fff}.navbar-inverse .navbar-collapse,.navbar-inverse .navbar-form{border-color:#101010}.navbar-inverse .navbar-link{color:#9d9d9d}.navbar-inverse .navbar-link:hover{color:#fff}.navbar-inverse .btn-link{color:#9d9d9d}.navbar-inverse .btn-link:focus,.navbar-inverse .btn-link:hover{color:#fff}.navbar-inverse .btn-link[disabled]:focus,.navbar-inverse .btn-link[disabled]:hover,fieldset[disabled] .navbar-inverse .btn-link:focus,fieldset[disabled] .navbar-inverse .btn-link:hover{color:#444}.breadcrumb{padding:8px 15px;margin-bottom:20px;list-style:none;background-color:#f5f5f5;border-radius:4px}.breadcrumb>li{display:inline-block}.breadcrumb>li+li:before{padding:0 5px;color:#ccc;content:"/\00a0"}.breadcrumb>.active{color:#777}.pagination{display:inline-block;padding-left:0;margin:20px 0;border-radius:4px}.pagination>li{display:inline}.pagination>li>a,.pagination>li>span{position:relative;float:left;padding:6px 12px;margin-left:-1px;line-height:1.42857143;color:#337ab7;text-decoration:none;background-color:#fff;border:1px solid #ddd}.pagination>li>a:focus,.pagination>li>a:hover,.pagination>li>span:focus,.pagination>li>span:hover{z-index:2;color:#23527c;background-color:#eee;border-color:#ddd}.pagination>li:first-child>a,.pagination>li:first-child>span{margin-left:0;border-top-left-radius:4px;border-bottom-left-radius:4px}.pagination>li:last-child>a,.pagination>li:last-child>span{border-top-right-radius:4px;border-bottom-right-radius:4px}.pagination>.active>a,.pagination>.active>a:focus,.pagination>.active>a:hover,.pagination>.active>span,.pagination>.active>span:focus,.pagination>.active>span:hover{z-index:3;color:#fff;cursor:default;background-color:#337ab7;border-color:#337ab7}.pagination>.disabled>a,.pagination>.disabled>a:focus,.pagination>.disabled>a:hover,.pagination>.disabled>span,.pagination>.disabled>span:focus,.pagination>.disabled>span:hover{color:#777;cursor:not-allowed;background-color:#fff;border-color:#ddd}.pagination-lg>li>a,.pagination-lg>li>span{padding:10px 16px;font-size:18px;line-height:1.3333333}.pagination-lg>li:first-child>a,.pagination-lg>li:first-child>span{border-top-left-radius:6px;border-bottom-left-radius:6px}.pagination-lg>li:last-child>a,.pagination-lg>li:last-child>span{border-top-right-radius:6px;border-bottom-right-radius:6px}.pagination-sm>li>a,.pagination-sm>li>span{padding:5px 10px;font-size:12px;line-height:1.5}.pagination-sm>li:first-child>a,.pagination-sm>li:first-child>span{border-top-left-radius:3px;border-bottom-left-radius:3px}.pagination-sm>li:last-child>a,.pagination-sm>li:last-child>span{border-top-right-radius:3px;border-bottom-right-radius:3px}.pager{padding-left:0;margin:20px 0;text-align:center;list-style:none}.pager li{display:inline}.pager li>a,.pager li>span{display:inline-block;padding:5px 14px;background-color:#fff;border:1px solid #ddd;border-radius:15px}.pager li>a:focus,.pager li>a:hover{text-decoration:none;background-color:#eee}.pager .next>a,.pager .next>span{float:right}.pager .previous>a,.pager .previous>span{float:left}.pager .disabled>a,.pager .disabled>a:focus,.pager .disabled>a:hover,.pager .disabled>span{color:#777;cursor:not-allowed;background-color:#fff}.label{display:inline;padding:.2em .6em .3em;font-size:75%;font-weight:700;line-height:1;color:#fff;text-align:center;white-space:nowrap;vertical-align:baseline;border-radius:.25em}a.label:focus,a.label:hover{color:#fff;text-decoration:none;cursor:pointer}.label:empty{display:none}.btn .label{position:relative;top:-1px}.label-default{background-color:#777}.label-default[href]:focus,.label-default[href]:hover{background-color:#5e5e5e}.label-primary{background-color:#337ab7}.label-primary[href]:focus,.label-primary[href]:hover{background-color:#286090}.label-success{background-color:#5cb85c}.label-success[href]:focus,.label-success[href]:hover{background-color:#449d44}.label-info{background-color:#5bc0de}.label-info[href]:focus,.label-info[href]:hover{background-color:#31b0d5}.label-warning{background-color:#f0ad4e}.label-warning[href]:focus,.label-warning[href]:hover{background-color:#ec971f}.label-danger{background-color:#d9534f}.label-danger[href]:focus,.label-danger[href]:hover{background-color:#c9302c}.badge{display:inline-block;min-width:10px;padding:3px 7px;font-size:12px;font-weight:700;line-height:1;color:#fff;text-align:center;white-space:nowrap;vertical-align:middle;background-color:#777;border-radius:10px}.badge:empty{display:none}.btn .badge{position:relative;top:-1px}.btn-group-xs>.btn .badge,.btn-xs .badge{top:0;padding:1px 5px}a.badge:focus,a.badge:hover{color:#fff;text-decoration:none;cursor:pointer}.list-group-item.active>.badge,.nav-pills>.active>a>.badge{color:#337ab7;background-color:#fff}.list-group-item>.badge{float:right}.list-group-item>.badge+.badge{margin-right:5px}.nav-pills>li>a>.badge{margin-left:3px}.jumbotron{padding-top:30px;padding-bottom:30px;margin-bottom:30px;color:inherit;background-color:#eee}.jumbotron .h1,.jumbotron h1{color:inherit}.jumbotron p{margin-bottom:15px;font-size:21px;font-weight:200}.jumbotron>hr{border-top-color:#d5d5d5}.container .jumbotron,.container-fluid .jumbotron{padding-right:15px;padding-left:15px;border-radius:6px}.jumbotron .container{max-width:100%}@media screen and (min-width:768px){.jumbotron{padding-top:48px;padding-bottom:48px}.container .jumbotron,.container-fluid .jumbotron{padding-right:60px;padding-left:60px}.jumbotron .h1,.jumbotron h1{font-size:63px}}.thumbnail{display:block;padding:4px;margin-bottom:20px;line-height:1.42857143;background-color:#fff;border:1px solid #ddd;border-radius:4px;-webkit-transition:border .2s ease-in-out;-o-transition:border .2s ease-in-out;transition:border .2s ease-in-out}.thumbnail a>img,.thumbnail>img{margin-right:auto;margin-left:auto}a.thumbnail.active,a.thumbnail:focus,a.thumbnail:hover{border-color:#337ab7}.thumbnail .caption{padding:9px;color:#333}.alert{padding:15px;margin-bottom:20px;border:1px solid transparent;border-radius:4px}.alert h4{margin-top:0;color:inherit}.alert .alert-link{font-weight:700}.alert>p,.alert>ul{margin-bottom:0}.alert>p+p{margin-top:5px}.alert-dismissable,.alert-dismissible{padding-right:35px}.alert-dismissable .close,.alert-dismissible .close{position:relative;top:-2px;right:-21px;color:inherit}.alert-success{color:#3c763d;background-color:#dff0d8;border-color:#d6e9c6}.alert-success hr{border-top-color:#c9e2b3}.alert-success .alert-link{color:#2b542c}.alert-info{color:#31708f;background-color:#d9edf7;border-color:#bce8f1}.alert-info hr{border-top-color:#a6e1ec}.alert-info .alert-link{color:#245269}.alert-warning{color:#8a6d3b;background-color:#fcf8e3;border-color:#faebcc}.alert-warning hr{border-top-color:#f7e1b5}.alert-warning .alert-link{color:#66512c}.alert-danger{color:#a94442;background-color:#f2dede;border-color:#ebccd1}.alert-danger hr{border-top-color:#e4b9c0}.alert-danger .alert-link{color:#843534}@-webkit-keyframes progress-bar-stripes{from{background-position:40px 0}to{background-position:0 0}}@-o-keyframes progress-bar-stripes{from{background-position:40px 0}to{background-position:0 0}}@keyframes progress-bar-stripes{from{background-position:40px 0}to{background-position:0 0}}.progress{height:20px;margin-bottom:20px;overflow:hidden;background-color:#f5f5f5;border-radius:4px;-webkit-box-shadow:inset 0 1px 2px rgba(0,0,0,.1);box-shadow:inset 0 1px 2px rgba(0,0,0,.1)}.progress-bar{float:left;width:0%;height:100%;font-size:12px;line-height:20px;color:#fff;text-align:center;background-color:#337ab7;-webkit-box-shadow:inset 0 -1px 0 rgba(0,0,0,.15);box-shadow:inset 0 -1px 0 rgba(0,0,0,.15);-webkit-transition:width .6s ease;-o-transition:width .6s ease;transition:width .6s ease}.progress-bar-striped,.progress-striped .progress-bar{background-image:-webkit-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:-o-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);-webkit-background-size:40px 40px;background-size:40px 40px}.progress-bar.active,.progress.active .progress-bar{-webkit-animation:progress-bar-stripes 2s linear infinite;-o-animation:progress-bar-stripes 2s linear infinite;animation:progress-bar-stripes 2s linear infinite}.progress-bar-success{background-color:#5cb85c}.progress-striped .progress-bar-success{background-image:-webkit-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:-o-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent)}.progress-bar-info{background-color:#5bc0de}.progress-striped .progress-bar-info{background-image:-webkit-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:-o-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent)}.progress-bar-warning{background-color:#f0ad4e}.progress-striped .progress-bar-warning{background-image:-webkit-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:-o-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent)}.progress-bar-danger{background-color:#d9534f}.progress-striped .progress-bar-danger{background-image:-webkit-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:-o-linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent);background-image:linear-gradient(45deg,rgba(255,255,255,.15) 25%,transparent 25%,transparent 50%,rgba(255,255,255,.15) 50%,rgba(255,255,255,.15) 75%,transparent 75%,transparent)}.media{margin-top:15px}.media:first-child{margin-top:0}.media,.media-body{overflow:hidden;zoom:1}.media-body{width:10000px}.media-object{display:block}.media-object.img-thumbnail{max-width:none}.media-right,.media>.pull-right{padding-left:10px}.media-left,.media>.pull-left{padding-right:10px}.media-body,.media-left,.media-right{display:table-cell;vertical-align:top}.media-middle{vertical-align:middle}.media-bottom{vertical-align:bottom}.media-heading{margin-top:0;margin-bottom:5px}.media-list{padding-left:0;list-style:none}.list-group{padding-left:0;margin-bottom:20px}.list-group-item{position:relative;display:block;padding:10px 15px;margin-bottom:-1px;background-color:#fff;border:1px solid #ddd}.list-group-item:first-child{border-top-left-radius:4px;border-top-right-radius:4px}.list-group-item:last-child{margin-bottom:0;border-bottom-right-radius:4px;border-bottom-left-radius:4px}.list-group-item.disabled,.list-group-item.disabled:focus,.list-group-item.disabled:hover{color:#777;cursor:not-allowed;background-color:#eee}.list-group-item.disabled .list-group-item-heading,.list-group-item.disabled:focus .list-group-item-heading,.list-group-item.disabled:hover .list-group-item-heading{color:inherit}.list-group-item.disabled .list-group-item-text,.list-group-item.disabled:focus .list-group-item-text,.list-group-item.disabled:hover .list-group-item-text{color:#777}.list-group-item.active,.list-group-item.active:focus,.list-group-item.active:hover{z-index:2;color:#fff;background-color:#337ab7;border-color:#337ab7}.list-group-item.active .list-group-item-heading,.list-group-item.active .list-group-item-heading>.small,.list-group-item.active .list-group-item-heading>small,.list-group-item.active:focus .list-group-item-heading,.list-group-item.active:focus .list-group-item-heading>.small,.list-group-item.active:focus .list-group-item-heading>small,.list-group-item.active:hover .list-group-item-heading,.list-group-item.active:hover .list-group-item-heading>.small,.list-group-item.active:hover .list-group-item-heading>small{color:inherit}.list-group-item.active .list-group-item-text,.list-group-item.active:focus .list-group-item-text,.list-group-item.active:hover .list-group-item-text{color:#c7ddef}a.list-group-item,button.list-group-item{color:#555}a.list-group-item .list-group-item-heading,button.list-group-item .list-group-item-heading{color:#333}a.list-group-item:focus,a.list-group-item:hover,button.list-group-item:focus,button.list-group-item:hover{color:#555;text-decoration:none;background-color:#f5f5f5}button.list-group-item{width:100%;text-align:left}.list-group-item-success{color:#3c763d;background-color:#dff0d8}a.list-group-item-success,button.list-group-item-success{color:#3c763d}a.list-group-item-success .list-group-item-heading,button.list-group-item-success .list-group-item-heading{color:inherit}a.list-group-item-success:focus,a.list-group-item-success:hover,button.list-group-item-success:focus,button.list-group-item-success:hover{color:#3c763d;background-color:#d0e9c6}a.list-group-item-success.active,a.list-group-item-success.active:focus,a.list-group-item-success.active:hover,button.list-group-item-success.active,button.list-group-item-success.active:focus,button.list-group-item-success.active:hover{color:#fff;background-color:#3c763d;border-color:#3c763d}.list-group-item-info{color:#31708f;background-color:#d9edf7}a.list-group-item-info,button.list-group-item-info{color:#31708f}a.list-group-item-info .list-group-item-heading,button.list-group-item-info .list-group-item-heading{color:inherit}a.list-group-item-info:focus,a.list-group-item-info:hover,button.list-group-item-info:focus,button.list-group-item-info:hover{color:#31708f;background-color:#c4e3f3}a.list-group-item-info.active,a.list-group-item-info.active:focus,a.list-group-item-info.active:hover,button.list-group-item-info.active,button.list-group-item-info.active:focus,button.list-group-item-info.active:hover{color:#fff;background-color:#31708f;border-color:#31708f}.list-group-item-warning{color:#8a6d3b;background-color:#fcf8e3}a.list-group-item-warning,button.list-group-item-warning{color:#8a6d3b}a.list-group-item-warning .list-group-item-heading,button.list-group-item-warning .list-group-item-heading{color:inherit}a.list-group-item-warning:focus,a.list-group-item-warning:hover,button.list-group-item-warning:focus,button.list-group-item-warning:hover{color:#8a6d3b;background-color:#faf2cc}a.list-group-item-warning.active,a.list-group-item-warning.active:focus,a.list-group-item-warning.active:hover,button.list-group-item-warning.active,button.list-group-item-warning.active:focus,button.list-group-item-warning.active:hover{color:#fff;background-color:#8a6d3b;border-color:#8a6d3b}.list-group-item-danger{color:#a94442;background-color:#f2dede}a.list-group-item-danger,button.list-group-item-danger{color:#a94442}a.list-group-item-danger .list-group-item-heading,button.list-group-item-danger .list-group-item-heading{color:inherit}a.list-group-item-danger:focus,a.list-group-item-danger:hover,button.list-group-item-danger:focus,button.list-group-item-danger:hover{color:#a94442;background-color:#ebcccc}a.list-group-item-danger.active,a.list-group-item-danger.active:focus,a.list-group-item-danger.active:hover,button.list-group-item-danger.active,button.list-group-item-danger.active:focus,button.list-group-item-danger.active:hover{color:#fff;background-color:#a94442;border-color:#a94442}.list-group-item-heading{margin-top:0;margin-bottom:5px}.list-group-item-text{margin-bottom:0;line-height:1.3}.panel{margin-bottom:20px;background-color:#fff;border:1px solid transparent;border-radius:4px;-webkit-box-shadow:0 1px 1px rgba(0,0,0,.05);box-shadow:0 1px 1px rgba(0,0,0,.05)}.panel-body{padding:15px}.panel-heading{padding:10px 15px;border-bottom:1px solid transparent;border-top-left-radius:3px;border-top-right-radius:3px}.panel-heading>.dropdown .dropdown-toggle{color:inherit}.panel-title{margin-top:0;margin-bottom:0;font-size:16px;color:inherit}.panel-title>.small,.panel-title>.small>a,.panel-title>a,.panel-title>small,.panel-title>small>a{color:inherit}.panel-footer{padding:10px 15px;background-color:#f5f5f5;border-top:1px solid #ddd;border-bottom-right-radius:3px;border-bottom-left-radius:3px}.panel>.list-group,.panel>.panel-collapse>.list-group{margin-bottom:0}.panel>.list-group .list-group-item,.panel>.panel-collapse>.list-group .list-group-item{border-width:1px 0;border-radius:0}.panel>.list-group:first-child .list-group-item:first-child,.panel>.panel-collapse>.list-group:first-child .list-group-item:first-child{border-top:0;border-top-left-radius:3px;border-top-right-radius:3px}.panel>.list-group:last-child .list-group-item:last-child,.panel>.panel-collapse>.list-group:last-child .list-group-item:last-child{border-bottom:0;border-bottom-right-radius:3px;border-bottom-left-radius:3px}.panel>.panel-heading+.panel-collapse>.list-group .list-group-item:first-child{border-top-left-radius:0;border-top-right-radius:0}.panel-heading+.list-group .list-group-item:first-child{border-top-width:0}.list-group+.panel-footer{border-top-width:0}.panel>.panel-collapse>.table,.panel>.table,.panel>.table-responsive>.table{margin-bottom:0}.panel>.panel-collapse>.table caption,.panel>.table caption,.panel>.table-responsive>.table caption{padding-right:15px;padding-left:15px}.panel>.table-responsive:first-child>.table:first-child,.panel>.table:first-child{border-top-left-radius:3px;border-top-right-radius:3px}.panel>.table-responsive:first-child>.table:first-child>tbody:first-child>tr:first-child,.panel>.table-responsive:first-child>.table:first-child>thead:first-child>tr:first-child,.panel>.table:first-child>tbody:first-child>tr:first-child,.panel>.table:first-child>thead:first-child>tr:first-child{border-top-left-radius:3px;border-top-right-radius:3px}.panel>.table-responsive:first-child>.table:first-child>tbody:first-child>tr:first-child td:first-child,.panel>.table-responsive:first-child>.table:first-child>tbody:first-child>tr:first-child th:first-child,.panel>.table-responsive:first-child>.table:first-child>thead:first-child>tr:first-child td:first-child,.panel>.table-responsive:first-child>.table:first-child>thead:first-child>tr:first-child th:first-child,.panel>.table:first-child>tbody:first-child>tr:first-child td:first-child,.panel>.table:first-child>tbody:first-child>tr:first-child th:first-child,.panel>.table:first-child>thead:first-child>tr:first-child td:first-child,.panel>.table:first-child>thead:first-child>tr:first-child th:first-child{border-top-left-radius:3px}.panel>.table-responsive:first-child>.table:first-child>tbody:first-child>tr:first-child td:last-child,.panel>.table-responsive:first-child>.table:first-child>tbody:first-child>tr:first-child th:last-child,.panel>.table-responsive:first-child>.table:first-child>thead:first-child>tr:first-child td:last-child,.panel>.table-responsive:first-child>.table:first-child>thead:first-child>tr:first-child th:last-child,.panel>.table:first-child>tbody:first-child>tr:first-child td:last-child,.panel>.table:first-child>tbody:first-child>tr:first-child th:last-child,.panel>.table:first-child>thead:first-child>tr:first-child td:last-child,.panel>.table:first-child>thead:first-child>tr:first-child th:last-child{border-top-right-radius:3px}.panel>.table-responsive:last-child>.table:last-child,.panel>.table:last-child{border-bottom-right-radius:3px;border-bottom-left-radius:3px}.panel>.table-responsive:last-child>.table:last-child>tbody:last-child>tr:last-child,.panel>.table-responsive:last-child>.table:last-child>tfoot:last-child>tr:last-child,.panel>.table:last-child>tbody:last-child>tr:last-child,.panel>.table:last-child>tfoot:last-child>tr:last-child{border-bottom-right-radius:3px;border-bottom-left-radius:3px}.panel>.table-responsive:last-child>.table:last-child>tbody:last-child>tr:last-child td:first-child,.panel>.table-responsive:last-child>.table:last-child>tbody:last-child>tr:last-child th:first-child,.panel>.table-responsive:last-child>.table:last-child>tfoot:last-child>tr:last-child td:first-child,.panel>.table-responsive:last-child>.table:last-child>tfoot:last-child>tr:last-child th:first-child,.panel>.table:last-child>tbody:last-child>tr:last-child td:first-child,.panel>.table:last-child>tbody:last-child>tr:last-child th:first-child,.panel>.table:last-child>tfoot:last-child>tr:last-child td:first-child,.panel>.table:last-child>tfoot:last-child>tr:last-child th:first-child{border-bottom-left-radius:3px}.panel>.table-responsive:last-child>.table:last-child>tbody:last-child>tr:last-child td:last-child,.panel>.table-responsive:last-child>.table:last-child>tbody:last-child>tr:last-child th:last-child,.panel>.table-responsive:last-child>.table:last-child>tfoot:last-child>tr:last-child td:last-child,.panel>.table-responsive:last-child>.table:last-child>tfoot:last-child>tr:last-child th:last-child,.panel>.table:last-child>tbody:last-child>tr:last-child td:last-child,.panel>.table:last-child>tbody:last-child>tr:last-child th:last-child,.panel>.table:last-child>tfoot:last-child>tr:last-child td:last-child,.panel>.table:last-child>tfoot:last-child>tr:last-child th:last-child{border-bottom-right-radius:3px}.panel>.panel-body+.table,.panel>.panel-body+.table-responsive,.panel>.table+.panel-body,.panel>.table-responsive+.panel-body{border-top:1px solid #ddd}.panel>.table>tbody:first-child>tr:first-child td,.panel>.table>tbody:first-child>tr:first-child th{border-top:0}.panel>.table-bordered,.panel>.table-responsive>.table-bordered{border:0}.panel>.table-bordered>tbody>tr>td:first-child,.panel>.table-bordered>tbody>tr>th:first-child,.panel>.table-bordered>tfoot>tr>td:first-child,.panel>.table-bordered>tfoot>tr>th:first-child,.panel>.table-bordered>thead>tr>td:first-child,.panel>.table-bordered>thead>tr>th:first-child,.panel>.table-responsive>.table-bordered>tbody>tr>td:first-child,.panel>.table-responsive>.table-bordered>tbody>tr>th:first-child,.panel>.table-responsive>.table-bordered>tfoot>tr>td:first-child,.panel>.table-responsive>.table-bordered>tfoot>tr>th:first-child,.panel>.table-responsive>.table-bordered>thead>tr>td:first-child,.panel>.table-responsive>.table-bordered>thead>tr>th:first-child{border-left:0}.panel>.table-bordered>tbody>tr>td:last-child,.panel>.table-bordered>tbody>tr>th:last-child,.panel>.table-bordered>tfoot>tr>td:last-child,.panel>.table-bordered>tfoot>tr>th:last-child,.panel>.table-bordered>thead>tr>td:last-child,.panel>.table-bordered>thead>tr>th:last-child,.panel>.table-responsive>.table-bordered>tbody>tr>td:last-child,.panel>.table-responsive>.table-bordered>tbody>tr>th:last-child,.panel>.table-responsive>.table-bordered>tfoot>tr>td:last-child,.panel>.table-responsive>.table-bordered>tfoot>tr>th:last-child,.panel>.table-responsive>.table-bordered>thead>tr>td:last-child,.panel>.table-responsive>.table-bordered>thead>tr>th:last-child{border-right:0}.panel>.table-bordered>tbody>tr:first-child>td,.panel>.table-bordered>tbody>tr:first-child>th,.panel>.table-bordered>thead>tr:first-child>td,.panel>.table-bordered>thead>tr:first-child>th,.panel>.table-responsive>.table-bordered>tbody>tr:first-child>td,.panel>.table-responsive>.table-bordered>tbody>tr:first-child>th,.panel>.table-responsive>.table-bordered>thead>tr:first-child>td,.panel>.table-responsive>.table-bordered>thead>tr:first-child>th{border-bottom:0}.panel>.table-bordered>tbody>tr:last-child>td,.panel>.table-bordered>tbody>tr:last-child>th,.panel>.table-bordered>tfoot>tr:last-child>td,.panel>.table-bordered>tfoot>tr:last-child>th,.panel>.table-responsive>.table-bordered>tbody>tr:last-child>td,.panel>.table-responsive>.table-bordered>tbody>tr:last-child>th,.panel>.table-responsive>.table-bordered>tfoot>tr:last-child>td,.panel>.table-responsive>.table-bordered>tfoot>tr:last-child>th{border-bottom:0}.panel>.table-responsive{margin-bottom:0;border:0}.panel-group{margin-bottom:20px}.panel-group .panel{margin-bottom:0;border-radius:4px}.panel-group .panel+.panel{margin-top:5px}.panel-group .panel-heading{border-bottom:0}.panel-group .panel-heading+.panel-collapse>.list-group,.panel-group .panel-heading+.panel-collapse>.panel-body{border-top:1px solid #ddd}.panel-group .panel-footer{border-top:0}.panel-group .panel-footer+.panel-collapse .panel-body{border-bottom:1px solid #ddd}.panel-default{border-color:#ddd}.panel-default>.panel-heading{color:#333;background-color:#f5f5f5;border-color:#ddd}.panel-default>.panel-heading+.panel-collapse>.panel-body{border-top-color:#ddd}.panel-default>.panel-heading .badge{color:#f5f5f5;background-color:#333}.panel-default>.panel-footer+.panel-collapse>.panel-body{border-bottom-color:#ddd}.panel-primary{border-color:#337ab7}.panel-primary>.panel-heading{color:#fff;background-color:#337ab7;border-color:#337ab7}.panel-primary>.panel-heading+.panel-collapse>.panel-body{border-top-color:#337ab7}.panel-primary>.panel-heading .badge{color:#337ab7;background-color:#fff}.panel-primary>.panel-footer+.panel-collapse>.panel-body{border-bottom-color:#337ab7}.panel-success{border-color:#d6e9c6}.panel-success>.panel-heading{color:#3c763d;background-color:#dff0d8;border-color:#d6e9c6}.panel-success>.panel-heading+.panel-collapse>.panel-body{border-top-color:#d6e9c6}.panel-success>.panel-heading .badge{color:#dff0d8;background-color:#3c763d}.panel-success>.panel-footer+.panel-collapse>.panel-body{border-bottom-color:#d6e9c6}.panel-info{border-color:#bce8f1}.panel-info>.panel-heading{color:#31708f;background-color:#d9edf7;border-color:#bce8f1}.panel-info>.panel-heading+.panel-collapse>.panel-body{border-top-color:#bce8f1}.panel-info>.panel-heading .badge{color:#d9edf7;background-color:#31708f}.panel-info>.panel-footer+.panel-collapse>.panel-body{border-bottom-color:#bce8f1}.panel-warning{border-color:#faebcc}.panel-warning>.panel-heading{color:#8a6d3b;background-color:#fcf8e3;border-color:#faebcc}.panel-warning>.panel-heading+.panel-collapse>.panel-body{border-top-color:#faebcc}.panel-warning>.panel-heading .badge{color:#fcf8e3;background-color:#8a6d3b}.panel-warning>.panel-footer+.panel-collapse>.panel-body{border-bottom-color:#faebcc}.panel-danger{border-color:#ebccd1}.panel-danger>.panel-heading{color:#a94442;background-color:#f2dede;border-color:#ebccd1}.panel-danger>.panel-heading+.panel-collapse>.panel-body{border-top-color:#ebccd1}.panel-danger>.panel-heading .badge{color:#f2dede;background-color:#a94442}.panel-danger>.panel-footer+.panel-collapse>.panel-body{border-bottom-color:#ebccd1}.embed-responsive{position:relative;display:block;height:0;padding:0;overflow:hidden}.embed-responsive .embed-responsive-item,.embed-responsive embed,.embed-responsive iframe,.embed-responsive object,.embed-responsive video{position:absolute;top:0;bottom:0;left:0;width:100%;height:100%;border:0}.embed-responsive-16by9{padding-bottom:56.25%}.embed-responsive-4by3{padding-bottom:75%}.well{min-height:20px;padding:19px;margin-bottom:20px;background-color:#f5f5f5;border:1px solid #e3e3e3;border-radius:4px;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.05);box-shadow:inset 0 1px 1px rgba(0,0,0,.05)}.well blockquote{border-color:#ddd;border-color:rgba(0,0,0,.15)}.well-lg{padding:24px;border-radius:6px}.well-sm{padding:9px;border-radius:3px}.close{float:right;font-size:21px;font-weight:700;line-height:1;color:#000;text-shadow:0 1px 0 #fff;opacity:.2}.close:focus,.close:hover{color:#000;text-decoration:none;cursor:pointer;opacity:.5}button.close{padding:0;cursor:pointer;background:0 0;border:0;-webkit-appearance:none;-moz-appearance:none;appearance:none}.modal-open{overflow:hidden}.modal{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1050;display:none;overflow:hidden;-webkit-overflow-scrolling:touch;outline:0}.modal.fade .modal-dialog{-webkit-transform:translate(0,-25%);-ms-transform:translate(0,-25%);-o-transform:translate(0,-25%);transform:translate(0,-25%);-webkit-transition:-webkit-transform .3s ease-out;-o-transition:-o-transform .3s ease-out;transition:-webkit-transform .3s ease-out;transition:transform .3s ease-out;transition:transform .3s ease-out,-webkit-transform .3s ease-out,-o-transform .3s ease-out}.modal.in .modal-dialog{-webkit-transform:translate(0,0);-ms-transform:translate(0,0);-o-transform:translate(0,0);transform:translate(0,0)}.modal-open .modal{overflow-x:hidden;overflow-y:auto}.modal-dialog{position:relative;width:auto;margin:10px}.modal-content{position:relative;background-color:#fff;background-clip:padding-box;border:1px solid #999;border:1px solid rgba(0,0,0,.2);border-radius:6px;-webkit-box-shadow:0 3px 9px rgba(0,0,0,.5);box-shadow:0 3px 9px rgba(0,0,0,.5);outline:0}.modal-backdrop{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1040;background-color:#000}.modal-backdrop.fade{opacity:0}.modal-backdrop.in{opacity:.5}.modal-header{padding:15px;border-bottom:1px solid #e5e5e5}.modal-header .close{margin-top:-2px}.modal-title{margin:0;line-height:1.42857143}.modal-body{position:relative;padding:15px}.modal-footer{padding:15px;text-align:right;border-top:1px solid #e5e5e5}.modal-footer .btn+.btn{margin-bottom:0;margin-left:5px}.modal-footer .btn-group .btn+.btn{margin-left:-1px}.modal-footer .btn-block+.btn-block{margin-left:0}.modal-scrollbar-measure{position:absolute;top:-9999px;width:50px;height:50px;overflow:scroll}@media (min-width:768px){.modal-dialog{width:600px;margin:30px auto}.modal-content{-webkit-box-shadow:0 5px 15px rgba(0,0,0,.5);box-shadow:0 5px 15px rgba(0,0,0,.5)}.modal-sm{width:300px}}@media (min-width:992px){.modal-lg{width:900px}}.tooltip{position:absolute;z-index:1070;display:block;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-style:normal;font-weight:400;line-height:1.42857143;line-break:auto;text-align:left;text-align:start;text-decoration:none;text-shadow:none;text-transform:none;letter-spacing:normal;word-break:normal;word-spacing:normal;word-wrap:normal;white-space:normal;font-size:12px;opacity:0}.tooltip.in{opacity:.9}.tooltip.top{padding:5px 0;margin-top:-3px}.tooltip.right{padding:0 5px;margin-left:3px}.tooltip.bottom{padding:5px 0;margin-top:3px}.tooltip.left{padding:0 5px;margin-left:-3px}.tooltip.top .tooltip-arrow{bottom:0;left:50%;margin-left:-5px;border-width:5px 5px 0;border-top-color:#000}.tooltip.top-left .tooltip-arrow{right:5px;bottom:0;margin-bottom:-5px;border-width:5px 5px 0;border-top-color:#000}.tooltip.top-right .tooltip-arrow{bottom:0;left:5px;margin-bottom:-5px;border-width:5px 5px 0;border-top-color:#000}.tooltip.right .tooltip-arrow{top:50%;left:0;margin-top:-5px;border-width:5px 5px 5px 0;border-right-color:#000}.tooltip.left .tooltip-arrow{top:50%;right:0;margin-top:-5px;border-width:5px 0 5px 5px;border-left-color:#000}.tooltip.bottom .tooltip-arrow{top:0;left:50%;margin-left:-5px;border-width:0 5px 5px;border-bottom-color:#000}.tooltip.bottom-left .tooltip-arrow{top:0;right:5px;margin-top:-5px;border-width:0 5px 5px;border-bottom-color:#000}.tooltip.bottom-right .tooltip-arrow{top:0;left:5px;margin-top:-5px;border-width:0 5px 5px;border-bottom-color:#000}.tooltip-inner{max-width:200px;padding:3px 8px;color:#fff;text-align:center;background-color:#000;border-radius:4px}.tooltip-arrow{position:absolute;width:0;height:0;border-color:transparent;border-style:solid}.popover{position:absolute;top:0;left:0;z-index:1060;display:none;max-width:276px;padding:1px;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-style:normal;font-weight:400;line-height:1.42857143;line-break:auto;text-align:left;text-align:start;text-decoration:none;text-shadow:none;text-transform:none;letter-spacing:normal;word-break:normal;word-spacing:normal;word-wrap:normal;white-space:normal;font-size:14px;background-color:#fff;background-clip:padding-box;border:1px solid #ccc;border:1px solid rgba(0,0,0,.2);border-radius:6px;-webkit-box-shadow:0 5px 10px rgba(0,0,0,.2);box-shadow:0 5px 10px rgba(0,0,0,.2)}.popover.top{margin-top:-10px}.popover.right{margin-left:10px}.popover.bottom{margin-top:10px}.popover.left{margin-left:-10px}.popover>.arrow{border-width:11px}.popover>.arrow,.popover>.arrow:after{position:absolute;display:block;width:0;height:0;border-color:transparent;border-style:solid}.popover>.arrow:after{content:"";border-width:10px}.popover.top>.arrow{bottom:-11px;left:50%;margin-left:-11px;border-top-color:#999;border-top-color:rgba(0,0,0,.25);border-bottom-width:0}.popover.top>.arrow:after{bottom:1px;margin-left:-10px;content:" ";border-top-color:#fff;border-bottom-width:0}.popover.right>.arrow{top:50%;left:-11px;margin-top:-11px;border-right-color:#999;border-right-color:rgba(0,0,0,.25);border-left-width:0}.popover.right>.arrow:after{bottom:-10px;left:1px;content:" ";border-right-color:#fff;border-left-width:0}.popover.bottom>.arrow{top:-11px;left:50%;margin-left:-11px;border-top-width:0;border-bottom-color:#999;border-bottom-color:rgba(0,0,0,.25)}.popover.bottom>.arrow:after{top:1px;margin-left:-10px;content:" ";border-top-width:0;border-bottom-color:#fff}.popover.left>.arrow{top:50%;right:-11px;margin-top:-11px;border-right-width:0;border-left-color:#999;border-left-color:rgba(0,0,0,.25)}.popover.left>.arrow:after{right:1px;bottom:-10px;content:" ";border-right-width:0;border-left-color:#fff}.popover-title{padding:8px 14px;margin:0;font-size:14px;background-color:#f7f7f7;border-bottom:1px solid #ebebeb;border-radius:5px 5px 0 0}.popover-content{padding:9px 14px}.carousel{position:relative}.carousel-inner{position:relative;width:100%;overflow:hidden}.carousel-inner>.item{position:relative;display:none;-webkit-transition:.6s ease-in-out left;-o-transition:.6s ease-in-out left;transition:.6s ease-in-out left}.carousel-inner>.item>a>img,.carousel-inner>.item>img{line-height:1}@media all and (transform-3d),(-webkit-transform-3d){.carousel-inner>.item{-webkit-transition:-webkit-transform .6s ease-in-out;-o-transition:-o-transform .6s ease-in-out;transition:-webkit-transform .6s ease-in-out;transition:transform .6s ease-in-out;transition:transform .6s ease-in-out,-webkit-transform .6s ease-in-out,-o-transform .6s ease-in-out;-webkit-backface-visibility:hidden;backface-visibility:hidden;-webkit-perspective:1000px;perspective:1000px}.carousel-inner>.item.active.right,.carousel-inner>.item.next{-webkit-transform:translate3d(100%,0,0);transform:translate3d(100%,0,0);left:0}.carousel-inner>.item.active.left,.carousel-inner>.item.prev{-webkit-transform:translate3d(-100%,0,0);transform:translate3d(-100%,0,0);left:0}.carousel-inner>.item.active,.carousel-inner>.item.next.left,.carousel-inner>.item.prev.right{-webkit-transform:translate3d(0,0,0);transform:translate3d(0,0,0);left:0}}.carousel-inner>.active,.carousel-inner>.next,.carousel-inner>.prev{display:block}.carousel-inner>.active{left:0}.carousel-inner>.next,.carousel-inner>.prev{position:absolute;top:0;width:100%}.carousel-inner>.next{left:100%}.carousel-inner>.prev{left:-100%}.carousel-inner>.next.left,.carousel-inner>.prev.right{left:0}.carousel-inner>.active.left{left:-100%}.carousel-inner>.active.right{left:100%}.carousel-control{position:absolute;top:0;bottom:0;left:0;width:15%;font-size:20px;color:#fff;text-align:center;text-shadow:0 1px 2px rgba(0,0,0,.6);background-color:rgba(0,0,0,0);opacity:.5}.carousel-control.left{background-image:-webkit-linear-gradient(left,rgba(0,0,0,.5) 0,rgba(0,0,0,.0001) 100%);background-image:-o-linear-gradient(left,rgba(0,0,0,.5) 0,rgba(0,0,0,.0001) 100%);background-image:-webkit-gradient(linear,left top,right top,from(rgba(0,0,0,.5)),to(rgba(0,0,0,.0001)));background-image:linear-gradient(to right,rgba(0,0,0,.5) 0,rgba(0,0,0,.0001) 100%);background-repeat:repeat-x}.carousel-control.right{right:0;left:auto;background-image:-webkit-linear-gradient(left,rgba(0,0,0,.0001) 0,rgba(0,0,0,.5) 100%);background-image:-o-linear-gradient(left,rgba(0,0,0,.0001) 0,rgba(0,0,0,.5) 100%);background-image:-webkit-gradient(linear,left top,right top,from(rgba(0,0,0,.0001)),to(rgba(0,0,0,.5)));background-image:linear-gradient(to right,rgba(0,0,0,.0001) 0,rgba(0,0,0,.5) 100%);background-repeat:repeat-x}.carousel-control:focus,.carousel-control:hover{color:#fff;text-decoration:none;outline:0;opacity:.9}.carousel-control .glyphicon-chevron-left,.carousel-control .glyphicon-chevron-right,.carousel-control .icon-next,.carousel-control .icon-prev{position:absolute;top:50%;z-index:5;display:inline-block;margin-top:-10px}.carousel-control .glyphicon-chevron-left,.carousel-control .icon-prev{left:50%;margin-left:-10px}.carousel-control .glyphicon-chevron-right,.carousel-control .icon-next{right:50%;margin-right:-10px}.carousel-control .icon-next,.carousel-control .icon-prev{width:20px;height:20px;font-family:serif;line-height:1}.carousel-control .icon-prev:before{content:"\2039"}.carousel-control .icon-next:before{content:"\203a"}.carousel-indicators{position:absolute;bottom:10px;left:50%;z-index:15;width:60%;padding-left:0;margin-left:-30%;text-align:center;list-style:none}.carousel-indicators li{display:inline-block;width:10px;height:10px;margin:1px;text-indent:-999px;cursor:pointer;background-color:rgba(0,0,0,0);border:1px solid #fff;border-radius:10px}.carousel-indicators .active{width:12px;height:12px;margin:0;background-color:#fff}.carousel-caption{position:absolute;right:15%;bottom:20px;left:15%;z-index:10;padding-top:20px;padding-bottom:20px;color:#fff;text-align:center;text-shadow:0 1px 2px rgba(0,0,0,.6)}.carousel-caption .btn{text-shadow:none}@media screen and (min-width:768px){.carousel-control .glyphicon-chevron-left,.carousel-control .glyphicon-chevron-right,.carousel-control .icon-next,.carousel-control .icon-prev{width:30px;height:30px;margin-top:-10px;font-size:30px}.carousel-control .glyphicon-chevron-left,.carousel-control .icon-prev{margin-left:-10px}.carousel-control .glyphicon-chevron-right,.carousel-control .icon-next{margin-right:-10px}.carousel-caption{right:20%;left:20%;padding-bottom:30px}.carousel-indicators{bottom:20px}}.btn-group-vertical>.btn-group:after,.btn-group-vertical>.btn-group:before,.btn-toolbar:after,.btn-toolbar:before,.clearfix:after,.clearfix:before,.container-fluid:after,.container-fluid:before,.container:after,.container:before,.dl-horizontal dd:after,.dl-horizontal dd:before,.form-horizontal .form-group:after,.form-horizontal .form-group:before,.modal-footer:after,.modal-footer:before,.modal-header:after,.modal-header:before,.nav:after,.nav:before,.navbar-collapse:after,.navbar-collapse:before,.navbar-header:after,.navbar-header:before,.navbar:after,.navbar:before,.pager:after,.pager:before,.panel-body:after,.panel-body:before,.row:after,.row:before{display:table;content:" "}.btn-group-vertical>.btn-group:after,.btn-toolbar:after,.clearfix:after,.container-fluid:after,.container:after,.dl-horizontal dd:after,.form-horizontal .form-group:after,.modal-footer:after,.modal-header:after,.nav:after,.navbar-collapse:after,.navbar-header:after,.navbar:after,.pager:after,.panel-body:after,.row:after{clear:both}.center-block{display:block;margin-right:auto;margin-left:auto}.pull-right{float:right!important}.pull-left{float:left!important}.hide{display:none!important}.show{display:block!important}.invisible{visibility:hidden}.text-hide{font:0/0 a;color:transparent;text-shadow:none;background-color:transparent;border:0}.hidden{display:none!important}.affix{position:fixed}@-ms-viewport{width:device-width}.visible-lg,.visible-md,.visible-sm,.visible-xs{display:none!important}.visible-lg-block,.visible-lg-inline,.visible-lg-inline-block,.visible-md-block,.visible-md-inline,.visible-md-inline-block,.visible-sm-block,.visible-sm-inline,.visible-sm-inline-block,.visible-xs-block,.visible-xs-inline,.visible-xs-inline-block{display:none!important}@media (max-width:767px){.visible-xs{display:block!important}table.visible-xs{display:table!important}tr.visible-xs{display:table-row!important}td.visible-xs,th.visible-xs{display:table-cell!important}}@media (max-width:767px){.visible-xs-block{display:block!important}}@media (max-width:767px){.visible-xs-inline{display:inline!important}}@media (max-width:767px){.visible-xs-inline-block{display:inline-block!important}}@media (min-width:768px) and (max-width:991px){.visible-sm{display:block!important}table.visible-sm{display:table!important}tr.visible-sm{display:table-row!important}td.visible-sm,th.visible-sm{display:table-cell!important}}@media (min-width:768px) and (max-width:991px){.visible-sm-block{display:block!important}}@media (min-width:768px) and (max-width:991px){.visible-sm-inline{display:inline!important}}@media (min-width:768px) and (max-width:991px){.visible-sm-inline-block{display:inline-block!important}}@media (min-width:992px) and (max-width:1199px){.visible-md{display:block!important}table.visible-md{display:table!important}tr.visible-md{display:table-row!important}td.visible-md,th.visible-md{display:table-cell!important}}@media (min-width:992px) and (max-width:1199px){.visible-md-block{display:block!important}}@media (min-width:992px) and (max-width:1199px){.visible-md-inline{display:inline!important}}@media (min-width:992px) and (max-width:1199px){.visible-md-inline-block{display:inline-block!important}}@media (min-width:1200px){.visible-lg{display:block!important}table.visible-lg{display:table!important}tr.visible-lg{display:table-row!important}td.visible-lg,th.visible-lg{display:table-cell!important}}@media (min-width:1200px){.visible-lg-block{display:block!important}}@media (min-width:1200px){.visible-lg-inline{display:inline!important}}@media (min-width:1200px){.visible-lg-inline-block{display:inline-block!important}}@media (max-width:767px){.hidden-xs{display:none!important}}@media (min-width:768px) and (max-width:991px){.hidden-sm{display:none!important}}@media (min-width:992px) and (max-width:1199px){.hidden-md{display:none!important}}@media (min-width:1200px){.hidden-lg{display:none!important}}.visible-print{display:none!important}@media print{.visible-print{display:block!important}table.visible-print{display:table!important}tr.visible-print{display:table-row!important}td.visible-print,th.visible-print{display:table-cell!important}}.visible-print-block{display:none!important}@media print{.visible-print-block{display:block!important}}.visible-print-inline{display:none!important}@media print{.visible-print-inline{display:inline!important}}.visible-print-inline-block{display:none!important}@media print{.visible-print-inline-block{display:inline-block!important}}@media print{.hidden-print{display:none!important}}[data-aos][data-aos][data-aos-duration="50"],body[data-aos-duration="50"] [data-aos]{transition-duration:50ms}[data-aos][data-aos][data-aos-delay="50"],body[data-aos-delay="50"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="50"].aos-animate,body[data-aos-delay="50"] [data-aos].aos-animate{transition-delay:50ms}[data-aos][data-aos][data-aos-duration="100"],body[data-aos-duration="100"] [data-aos]{transition-duration:.1s}[data-aos][data-aos][data-aos-delay="100"],body[data-aos-delay="100"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="100"].aos-animate,body[data-aos-delay="100"] [data-aos].aos-animate{transition-delay:.1s}[data-aos][data-aos][data-aos-duration="150"],body[data-aos-duration="150"] [data-aos]{transition-duration:.15s}[data-aos][data-aos][data-aos-delay="150"],body[data-aos-delay="150"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="150"].aos-animate,body[data-aos-delay="150"] [data-aos].aos-animate{transition-delay:.15s}[data-aos][data-aos][data-aos-duration="200"],body[data-aos-duration="200"] [data-aos]{transition-duration:.2s}[data-aos][data-aos][data-aos-delay="200"],body[data-aos-delay="200"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="200"].aos-animate,body[data-aos-delay="200"] [data-aos].aos-animate{transition-delay:.2s}[data-aos][data-aos][data-aos-duration="250"],body[data-aos-duration="250"] [data-aos]{transition-duration:.25s}[data-aos][data-aos][data-aos-delay="250"],body[data-aos-delay="250"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="250"].aos-animate,body[data-aos-delay="250"] [data-aos].aos-animate{transition-delay:.25s}[data-aos][data-aos][data-aos-duration="300"],body[data-aos-duration="300"] [data-aos]{transition-duration:.3s}[data-aos][data-aos][data-aos-delay="300"],body[data-aos-delay="300"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="300"].aos-animate,body[data-aos-delay="300"] [data-aos].aos-animate{transition-delay:.3s}[data-aos][data-aos][data-aos-duration="350"],body[data-aos-duration="350"] [data-aos]{transition-duration:.35s}[data-aos][data-aos][data-aos-delay="350"],body[data-aos-delay="350"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="350"].aos-animate,body[data-aos-delay="350"] [data-aos].aos-animate{transition-delay:.35s}[data-aos][data-aos][data-aos-duration="400"],body[data-aos-duration="400"] [data-aos]{transition-duration:.4s}[data-aos][data-aos][data-aos-delay="400"],body[data-aos-delay="400"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="400"].aos-animate,body[data-aos-delay="400"] [data-aos].aos-animate{transition-delay:.4s}[data-aos][data-aos][data-aos-duration="450"],body[data-aos-duration="450"] [data-aos]{transition-duration:.45s}[data-aos][data-aos][data-aos-delay="450"],body[data-aos-delay="450"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="450"].aos-animate,body[data-aos-delay="450"] [data-aos].aos-animate{transition-delay:.45s}[data-aos][data-aos][data-aos-duration="500"],body[data-aos-duration="500"] [data-aos]{transition-duration:.5s}[data-aos][data-aos][data-aos-delay="500"],body[data-aos-delay="500"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="500"].aos-animate,body[data-aos-delay="500"] [data-aos].aos-animate{transition-delay:.5s}[data-aos][data-aos][data-aos-duration="550"],body[data-aos-duration="550"] [data-aos]{transition-duration:.55s}[data-aos][data-aos][data-aos-delay="550"],body[data-aos-delay="550"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="550"].aos-animate,body[data-aos-delay="550"] [data-aos].aos-animate{transition-delay:.55s}[data-aos][data-aos][data-aos-duration="600"],body[data-aos-duration="600"] [data-aos]{transition-duration:.6s}[data-aos][data-aos][data-aos-delay="600"],body[data-aos-delay="600"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="600"].aos-animate,body[data-aos-delay="600"] [data-aos].aos-animate{transition-delay:.6s}[data-aos][data-aos][data-aos-duration="650"],body[data-aos-duration="650"] [data-aos]{transition-duration:.65s}[data-aos][data-aos][data-aos-delay="650"],body[data-aos-delay="650"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="650"].aos-animate,body[data-aos-delay="650"] [data-aos].aos-animate{transition-delay:.65s}[data-aos][data-aos][data-aos-duration="700"],body[data-aos-duration="700"] [data-aos]{transition-duration:.7s}[data-aos][data-aos][data-aos-delay="700"],body[data-aos-delay="700"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="700"].aos-animate,body[data-aos-delay="700"] [data-aos].aos-animate{transition-delay:.7s}[data-aos][data-aos][data-aos-duration="750"],body[data-aos-duration="750"] [data-aos]{transition-duration:.75s}[data-aos][data-aos][data-aos-delay="750"],body[data-aos-delay="750"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="750"].aos-animate,body[data-aos-delay="750"] [data-aos].aos-animate{transition-delay:.75s}[data-aos][data-aos][data-aos-duration="800"],body[data-aos-duration="800"] [data-aos]{transition-duration:.8s}[data-aos][data-aos][data-aos-delay="800"],body[data-aos-delay="800"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="800"].aos-animate,body[data-aos-delay="800"] [data-aos].aos-animate{transition-delay:.8s}[data-aos][data-aos][data-aos-duration="850"],body[data-aos-duration="850"] [data-aos]{transition-duration:.85s}[data-aos][data-aos][data-aos-delay="850"],body[data-aos-delay="850"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="850"].aos-animate,body[data-aos-delay="850"] [data-aos].aos-animate{transition-delay:.85s}[data-aos][data-aos][data-aos-duration="900"],body[data-aos-duration="900"] [data-aos]{transition-duration:.9s}[data-aos][data-aos][data-aos-delay="900"],body[data-aos-delay="900"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="900"].aos-animate,body[data-aos-delay="900"] [data-aos].aos-animate{transition-delay:.9s}[data-aos][data-aos][data-aos-duration="950"],body[data-aos-duration="950"] [data-aos]{transition-duration:.95s}[data-aos][data-aos][data-aos-delay="950"],body[data-aos-delay="950"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="950"].aos-animate,body[data-aos-delay="950"] [data-aos].aos-animate{transition-delay:.95s}[data-aos][data-aos][data-aos-duration="1000"],body[data-aos-duration="1000"] [data-aos]{transition-duration:1s}[data-aos][data-aos][data-aos-delay="1000"],body[data-aos-delay="1000"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1000"].aos-animate,body[data-aos-delay="1000"] [data-aos].aos-animate{transition-delay:1s}[data-aos][data-aos][data-aos-duration="1050"],body[data-aos-duration="1050"] [data-aos]{transition-duration:1.05s}[data-aos][data-aos][data-aos-delay="1050"],body[data-aos-delay="1050"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1050"].aos-animate,body[data-aos-delay="1050"] [data-aos].aos-animate{transition-delay:1.05s}[data-aos][data-aos][data-aos-duration="1100"],body[data-aos-duration="1100"] [data-aos]{transition-duration:1.1s}[data-aos][data-aos][data-aos-delay="1100"],body[data-aos-delay="1100"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1100"].aos-animate,body[data-aos-delay="1100"] [data-aos].aos-animate{transition-delay:1.1s}[data-aos][data-aos][data-aos-duration="1150"],body[data-aos-duration="1150"] [data-aos]{transition-duration:1.15s}[data-aos][data-aos][data-aos-delay="1150"],body[data-aos-delay="1150"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1150"].aos-animate,body[data-aos-delay="1150"] [data-aos].aos-animate{transition-delay:1.15s}[data-aos][data-aos][data-aos-duration="1200"],body[data-aos-duration="1200"] [data-aos]{transition-duration:1.2s}[data-aos][data-aos][data-aos-delay="1200"],body[data-aos-delay="1200"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1200"].aos-animate,body[data-aos-delay="1200"] [data-aos].aos-animate{transition-delay:1.2s}[data-aos][data-aos][data-aos-duration="1250"],body[data-aos-duration="1250"] [data-aos]{transition-duration:1.25s}[data-aos][data-aos][data-aos-delay="1250"],body[data-aos-delay="1250"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1250"].aos-animate,body[data-aos-delay="1250"] [data-aos].aos-animate{transition-delay:1.25s}[data-aos][data-aos][data-aos-duration="1300"],body[data-aos-duration="1300"] [data-aos]{transition-duration:1.3s}[data-aos][data-aos][data-aos-delay="1300"],body[data-aos-delay="1300"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1300"].aos-animate,body[data-aos-delay="1300"] [data-aos].aos-animate{transition-delay:1.3s}[data-aos][data-aos][data-aos-duration="1350"],body[data-aos-duration="1350"] [data-aos]{transition-duration:1.35s}[data-aos][data-aos][data-aos-delay="1350"],body[data-aos-delay="1350"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1350"].aos-animate,body[data-aos-delay="1350"] [data-aos].aos-animate{transition-delay:1.35s}[data-aos][data-aos][data-aos-duration="1400"],body[data-aos-duration="1400"] [data-aos]{transition-duration:1.4s}[data-aos][data-aos][data-aos-delay="1400"],body[data-aos-delay="1400"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1400"].aos-animate,body[data-aos-delay="1400"] [data-aos].aos-animate{transition-delay:1.4s}[data-aos][data-aos][data-aos-duration="1450"],body[data-aos-duration="1450"] [data-aos]{transition-duration:1.45s}[data-aos][data-aos][data-aos-delay="1450"],body[data-aos-delay="1450"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1450"].aos-animate,body[data-aos-delay="1450"] [data-aos].aos-animate{transition-delay:1.45s}[data-aos][data-aos][data-aos-duration="1500"],body[data-aos-duration="1500"] [data-aos]{transition-duration:1.5s}[data-aos][data-aos][data-aos-delay="1500"],body[data-aos-delay="1500"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1500"].aos-animate,body[data-aos-delay="1500"] [data-aos].aos-animate{transition-delay:1.5s}[data-aos][data-aos][data-aos-duration="1550"],body[data-aos-duration="1550"] [data-aos]{transition-duration:1.55s}[data-aos][data-aos][data-aos-delay="1550"],body[data-aos-delay="1550"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1550"].aos-animate,body[data-aos-delay="1550"] [data-aos].aos-animate{transition-delay:1.55s}[data-aos][data-aos][data-aos-duration="1600"],body[data-aos-duration="1600"] [data-aos]{transition-duration:1.6s}[data-aos][data-aos][data-aos-delay="1600"],body[data-aos-delay="1600"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1600"].aos-animate,body[data-aos-delay="1600"] [data-aos].aos-animate{transition-delay:1.6s}[data-aos][data-aos][data-aos-duration="1650"],body[data-aos-duration="1650"] [data-aos]{transition-duration:1.65s}[data-aos][data-aos][data-aos-delay="1650"],body[data-aos-delay="1650"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1650"].aos-animate,body[data-aos-delay="1650"] [data-aos].aos-animate{transition-delay:1.65s}[data-aos][data-aos][data-aos-duration="1700"],body[data-aos-duration="1700"] [data-aos]{transition-duration:1.7s}[data-aos][data-aos][data-aos-delay="1700"],body[data-aos-delay="1700"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1700"].aos-animate,body[data-aos-delay="1700"] [data-aos].aos-animate{transition-delay:1.7s}[data-aos][data-aos][data-aos-duration="1750"],body[data-aos-duration="1750"] [data-aos]{transition-duration:1.75s}[data-aos][data-aos][data-aos-delay="1750"],body[data-aos-delay="1750"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1750"].aos-animate,body[data-aos-delay="1750"] [data-aos].aos-animate{transition-delay:1.75s}[data-aos][data-aos][data-aos-duration="1800"],body[data-aos-duration="1800"] [data-aos]{transition-duration:1.8s}[data-aos][data-aos][data-aos-delay="1800"],body[data-aos-delay="1800"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1800"].aos-animate,body[data-aos-delay="1800"] [data-aos].aos-animate{transition-delay:1.8s}[data-aos][data-aos][data-aos-duration="1850"],body[data-aos-duration="1850"] [data-aos]{transition-duration:1.85s}[data-aos][data-aos][data-aos-delay="1850"],body[data-aos-delay="1850"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1850"].aos-animate,body[data-aos-delay="1850"] [data-aos].aos-animate{transition-delay:1.85s}[data-aos][data-aos][data-aos-duration="1900"],body[data-aos-duration="1900"] [data-aos]{transition-duration:1.9s}[data-aos][data-aos][data-aos-delay="1900"],body[data-aos-delay="1900"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1900"].aos-animate,body[data-aos-delay="1900"] [data-aos].aos-animate{transition-delay:1.9s}[data-aos][data-aos][data-aos-duration="1950"],body[data-aos-duration="1950"] [data-aos]{transition-duration:1.95s}[data-aos][data-aos][data-aos-delay="1950"],body[data-aos-delay="1950"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="1950"].aos-animate,body[data-aos-delay="1950"] [data-aos].aos-animate{transition-delay:1.95s}[data-aos][data-aos][data-aos-duration="2000"],body[data-aos-duration="2000"] [data-aos]{transition-duration:2s}[data-aos][data-aos][data-aos-delay="2000"],body[data-aos-delay="2000"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2000"].aos-animate,body[data-aos-delay="2000"] [data-aos].aos-animate{transition-delay:2s}[data-aos][data-aos][data-aos-duration="2050"],body[data-aos-duration="2050"] [data-aos]{transition-duration:2.05s}[data-aos][data-aos][data-aos-delay="2050"],body[data-aos-delay="2050"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2050"].aos-animate,body[data-aos-delay="2050"] [data-aos].aos-animate{transition-delay:2.05s}[data-aos][data-aos][data-aos-duration="2100"],body[data-aos-duration="2100"] [data-aos]{transition-duration:2.1s}[data-aos][data-aos][data-aos-delay="2100"],body[data-aos-delay="2100"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2100"].aos-animate,body[data-aos-delay="2100"] [data-aos].aos-animate{transition-delay:2.1s}[data-aos][data-aos][data-aos-duration="2150"],body[data-aos-duration="2150"] [data-aos]{transition-duration:2.15s}[data-aos][data-aos][data-aos-delay="2150"],body[data-aos-delay="2150"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2150"].aos-animate,body[data-aos-delay="2150"] [data-aos].aos-animate{transition-delay:2.15s}[data-aos][data-aos][data-aos-duration="2200"],body[data-aos-duration="2200"] [data-aos]{transition-duration:2.2s}[data-aos][data-aos][data-aos-delay="2200"],body[data-aos-delay="2200"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2200"].aos-animate,body[data-aos-delay="2200"] [data-aos].aos-animate{transition-delay:2.2s}[data-aos][data-aos][data-aos-duration="2250"],body[data-aos-duration="2250"] [data-aos]{transition-duration:2.25s}[data-aos][data-aos][data-aos-delay="2250"],body[data-aos-delay="2250"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2250"].aos-animate,body[data-aos-delay="2250"] [data-aos].aos-animate{transition-delay:2.25s}[data-aos][data-aos][data-aos-duration="2300"],body[data-aos-duration="2300"] [data-aos]{transition-duration:2.3s}[data-aos][data-aos][data-aos-delay="2300"],body[data-aos-delay="2300"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2300"].aos-animate,body[data-aos-delay="2300"] [data-aos].aos-animate{transition-delay:2.3s}[data-aos][data-aos][data-aos-duration="2350"],body[data-aos-duration="2350"] [data-aos]{transition-duration:2.35s}[data-aos][data-aos][data-aos-delay="2350"],body[data-aos-delay="2350"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2350"].aos-animate,body[data-aos-delay="2350"] [data-aos].aos-animate{transition-delay:2.35s}[data-aos][data-aos][data-aos-duration="2400"],body[data-aos-duration="2400"] [data-aos]{transition-duration:2.4s}[data-aos][data-aos][data-aos-delay="2400"],body[data-aos-delay="2400"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2400"].aos-animate,body[data-aos-delay="2400"] [data-aos].aos-animate{transition-delay:2.4s}[data-aos][data-aos][data-aos-duration="2450"],body[data-aos-duration="2450"] [data-aos]{transition-duration:2.45s}[data-aos][data-aos][data-aos-delay="2450"],body[data-aos-delay="2450"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2450"].aos-animate,body[data-aos-delay="2450"] [data-aos].aos-animate{transition-delay:2.45s}[data-aos][data-aos][data-aos-duration="2500"],body[data-aos-duration="2500"] [data-aos]{transition-duration:2.5s}[data-aos][data-aos][data-aos-delay="2500"],body[data-aos-delay="2500"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2500"].aos-animate,body[data-aos-delay="2500"] [data-aos].aos-animate{transition-delay:2.5s}[data-aos][data-aos][data-aos-duration="2550"],body[data-aos-duration="2550"] [data-aos]{transition-duration:2.55s}[data-aos][data-aos][data-aos-delay="2550"],body[data-aos-delay="2550"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2550"].aos-animate,body[data-aos-delay="2550"] [data-aos].aos-animate{transition-delay:2.55s}[data-aos][data-aos][data-aos-duration="2600"],body[data-aos-duration="2600"] [data-aos]{transition-duration:2.6s}[data-aos][data-aos][data-aos-delay="2600"],body[data-aos-delay="2600"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2600"].aos-animate,body[data-aos-delay="2600"] [data-aos].aos-animate{transition-delay:2.6s}[data-aos][data-aos][data-aos-duration="2650"],body[data-aos-duration="2650"] [data-aos]{transition-duration:2.65s}[data-aos][data-aos][data-aos-delay="2650"],body[data-aos-delay="2650"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2650"].aos-animate,body[data-aos-delay="2650"] [data-aos].aos-animate{transition-delay:2.65s}[data-aos][data-aos][data-aos-duration="2700"],body[data-aos-duration="2700"] [data-aos]{transition-duration:2.7s}[data-aos][data-aos][data-aos-delay="2700"],body[data-aos-delay="2700"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2700"].aos-animate,body[data-aos-delay="2700"] [data-aos].aos-animate{transition-delay:2.7s}[data-aos][data-aos][data-aos-duration="2750"],body[data-aos-duration="2750"] [data-aos]{transition-duration:2.75s}[data-aos][data-aos][data-aos-delay="2750"],body[data-aos-delay="2750"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2750"].aos-animate,body[data-aos-delay="2750"] [data-aos].aos-animate{transition-delay:2.75s}[data-aos][data-aos][data-aos-duration="2800"],body[data-aos-duration="2800"] [data-aos]{transition-duration:2.8s}[data-aos][data-aos][data-aos-delay="2800"],body[data-aos-delay="2800"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2800"].aos-animate,body[data-aos-delay="2800"] [data-aos].aos-animate{transition-delay:2.8s}[data-aos][data-aos][data-aos-duration="2850"],body[data-aos-duration="2850"] [data-aos]{transition-duration:2.85s}[data-aos][data-aos][data-aos-delay="2850"],body[data-aos-delay="2850"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2850"].aos-animate,body[data-aos-delay="2850"] [data-aos].aos-animate{transition-delay:2.85s}[data-aos][data-aos][data-aos-duration="2900"],body[data-aos-duration="2900"] [data-aos]{transition-duration:2.9s}[data-aos][data-aos][data-aos-delay="2900"],body[data-aos-delay="2900"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2900"].aos-animate,body[data-aos-delay="2900"] [data-aos].aos-animate{transition-delay:2.9s}[data-aos][data-aos][data-aos-duration="2950"],body[data-aos-duration="2950"] [data-aos]{transition-duration:2.95s}[data-aos][data-aos][data-aos-delay="2950"],body[data-aos-delay="2950"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="2950"].aos-animate,body[data-aos-delay="2950"] [data-aos].aos-animate{transition-delay:2.95s}[data-aos][data-aos][data-aos-duration="3000"],body[data-aos-duration="3000"] [data-aos]{transition-duration:3s}[data-aos][data-aos][data-aos-delay="3000"],body[data-aos-delay="3000"] [data-aos]{transition-delay:0}[data-aos][data-aos][data-aos-delay="3000"].aos-animate,body[data-aos-delay="3000"] [data-aos].aos-animate{transition-delay:3s}[data-aos][data-aos][data-aos-easing=linear],body[data-aos-easing=linear] [data-aos]{transition-timing-function:cubic-bezier(.25,.25,.75,.75)}[data-aos][data-aos][data-aos-easing=ease],body[data-aos-easing=ease] [data-aos]{transition-timing-function:ease}[data-aos][data-aos][data-aos-easing=ease-in],body[data-aos-easing=ease-in] [data-aos]{transition-timing-function:ease-in}[data-aos][data-aos][data-aos-easing=ease-out],body[data-aos-easing=ease-out] [data-aos]{transition-timing-function:ease-out}[data-aos][data-aos][data-aos-easing=ease-in-out],body[data-aos-easing=ease-in-out] [data-aos]{transition-timing-function:ease-in-out}[data-aos][data-aos][data-aos-easing=ease-in-back],body[data-aos-easing=ease-in-back] [data-aos]{transition-timing-function:cubic-bezier(.6,-.28,.735,.045)}[data-aos][data-aos][data-aos-easing=ease-out-back],body[data-aos-easing=ease-out-back] [data-aos]{transition-timing-function:cubic-bezier(.175,.885,.32,1.275)}[data-aos][data-aos][data-aos-easing=ease-in-out-back],body[data-aos-easing=ease-in-out-back] [data-aos]{transition-timing-function:cubic-bezier(.68,-.55,.265,1.55)}[data-aos][data-aos][data-aos-easing=ease-in-sine],body[data-aos-easing=ease-in-sine] [data-aos]{transition-timing-function:cubic-bezier(.47,0,.745,.715)}[data-aos][data-aos][data-aos-easing=ease-out-sine],body[data-aos-easing=ease-out-sine] [data-aos]{transition-timing-function:cubic-bezier(.39,.575,.565,1)}[data-aos][data-aos][data-aos-easing=ease-in-out-sine],body[data-aos-easing=ease-in-out-sine] [data-aos]{transition-timing-function:cubic-bezier(.445,.05,.55,.95)}[data-aos][data-aos][data-aos-easing=ease-in-quad],body[data-aos-easing=ease-in-quad] [data-aos]{transition-timing-function:cubic-bezier(.55,.085,.68,.53)}[data-aos][data-aos][data-aos-easing=ease-out-quad],body[data-aos-easing=ease-out-quad] [data-aos]{transition-timing-function:cubic-bezier(.25,.46,.45,.94)}[data-aos][data-aos][data-aos-easing=ease-in-out-quad],body[data-aos-easing=ease-in-out-quad] [data-aos]{transition-timing-function:cubic-bezier(.455,.03,.515,.955)}[data-aos][data-aos][data-aos-easing=ease-in-cubic],body[data-aos-easing=ease-in-cubic] [data-aos]{transition-timing-function:cubic-bezier(.55,.085,.68,.53)}[data-aos][data-aos][data-aos-easing=ease-out-cubic],body[data-aos-easing=ease-out-cubic] [data-aos]{transition-timing-function:cubic-bezier(.25,.46,.45,.94)}[data-aos][data-aos][data-aos-easing=ease-in-out-cubic],body[data-aos-easing=ease-in-out-cubic] [data-aos]{transition-timing-function:cubic-bezier(.455,.03,.515,.955)}[data-aos][data-aos][data-aos-easing=ease-in-quart],body[data-aos-easing=ease-in-quart] [data-aos]{transition-timing-function:cubic-bezier(.55,.085,.68,.53)}[data-aos][data-aos][data-aos-easing=ease-out-quart],body[data-aos-easing=ease-out-quart] [data-aos]{transition-timing-function:cubic-bezier(.25,.46,.45,.94)}[data-aos][data-aos][data-aos-easing=ease-in-out-quart],body[data-aos-easing=ease-in-out-quart] [data-aos]{transition-timing-function:cubic-bezier(.455,.03,.515,.955)}[data-aos^=fade][data-aos^=fade]{opacity:0;transition-property:opacity,transform}[data-aos^=fade][data-aos^=fade].aos-animate{opacity:1;transform:translateZ(0)}[data-aos=fade-up]{transform:translate3d(0,100px,0)}[data-aos=fade-down]{transform:translate3d(0,-100px,0)}[data-aos=fade-right]{transform:translate3d(-100px,0,0)}[data-aos=fade-left]{transform:translate3d(100px,0,0)}[data-aos=fade-up-right]{transform:translate3d(-100px,100px,0)}[data-aos=fade-up-left]{transform:translate3d(100px,100px,0)}[data-aos=fade-down-right]{transform:translate3d(-100px,-100px,0)}[data-aos=fade-down-left]{transform:translate3d(100px,-100px,0)}[data-aos^=zoom][data-aos^=zoom]{opacity:0;transition-property:opacity,transform}[data-aos^=zoom][data-aos^=zoom].aos-animate{opacity:1;transform:translateZ(0) scale(1)}[data-aos=zoom-in]{transform:scale(.6)}[data-aos=zoom-in-up]{transform:translate3d(0,100px,0) scale(.6)}[data-aos=zoom-in-down]{transform:translate3d(0,-100px,0) scale(.6)}[data-aos=zoom-in-right]{transform:translate3d(-100px,0,0) scale(.6)}[data-aos=zoom-in-left]{transform:translate3d(100px,0,0) scale(.6)}[data-aos=zoom-out]{transform:scale(1.2)}[data-aos=zoom-out-up]{transform:translate3d(0,100px,0) scale(1.2)}[data-aos=zoom-out-down]{transform:translate3d(0,-100px,0) scale(1.2)}[data-aos=zoom-out-right]{transform:translate3d(-100px,0,0) scale(1.2)}[data-aos=zoom-out-left]{transform:translate3d(100px,0,0) scale(1.2)}[data-aos^=slide][data-aos^=slide]{transition-property:transform}[data-aos^=slide][data-aos^=slide].aos-animate{transform:translateZ(0)}[data-aos=slide-up]{transform:translate3d(0,100%,0)}[data-aos=slide-down]{transform:translate3d(0,-100%,0)}[data-aos=slide-right]{transform:translate3d(-100%,0,0)}[data-aos=slide-left]{transform:translate3d(100%,0,0)}[data-aos^=flip][data-aos^=flip]{backface-visibility:hidden;transition-property:transform}[data-aos=flip-left]{transform:perspective(2500px) rotateY(-100deg)}[data-aos=flip-left].aos-animate{transform:perspective(2500px) rotateY(0)}[data-aos=flip-right]{transform:perspective(2500px) rotateY(100deg)}[data-aos=flip-right].aos-animate{transform:perspective(2500px) rotateY(0)}[data-aos=flip-up]{transform:perspective(2500px) rotateX(-100deg)}[data-aos=flip-up].aos-animate{transform:perspective(2500px) rotateX(0)}[data-aos=flip-down]{transform:perspective(2500px) rotateX(100deg)}[data-aos=flip-down].aos-animate{transform:perspective(2500px) rotateX(0)}@font-face{font-family:Roboto;src:url(/theme_teal/fonts/Roboto-Regular.ttf)}@font-face{font-family:Roboto;font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Mu72xKKTU1Kvnz.woff2) format('woff2');unicode-range:U+0460-052F,U+1C80-1C88,U+20B4,U+2DE0-2DFF,U+A640-A69F,U+FE2E-FE2F}@font-face{font-family:Roboto;font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Mu5mxKKTU1Kvnz.woff2) format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}@font-face{font-family:Roboto;font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Mu7mxKKTU1Kvnz.woff2) format('woff2');unicode-range:U+1F00-1FFF}@font-face{font-family:Roboto;font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Mu4WxKKTU1Kvnz.woff2) format('woff2');unicode-range:U+0370-03FF}@font-face{font-family:Roboto;font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Mu7WxKKTU1Kvnz.woff2) format('woff2');unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+1EA0-1EF9,U+20AB}@font-face{font-family:Roboto;font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Mu7GxKKTU1Kvnz.woff2) format('woff2');unicode-range:U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF}@font-face{font-family:Roboto;font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Mu4mxKKTU1Kg.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}@font-face{font-family:Roboto;font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmWUlfCRc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0460-052F,U+1C80-1C88,U+20B4,U+2DE0-2DFF,U+A640-A69F,U+FE2E-FE2F}@font-face{font-family:Roboto;font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmWUlfABc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116}@font-face{font-family:Roboto;font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmWUlfCBc4AMP6lbBP.woff2) format('woff2');unicode-range:U+1F00-1FFF}@font-face{font-family:Roboto;font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmWUlfBxc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0370-03FF}@font-face{font-family:Roboto;font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmWUlfCxc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+1EA0-1EF9,U+20AB}@font-face{font-family:Roboto;font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmWUlfChc4AMP6lbBP.woff2) format('woff2');unicode-range:U+0100-024F,U+0259,U+1E00-1EFF,U+2020,U+20A0-20AB,U+20AD-20CF,U+2113,U+2C60-2C7F,U+A720-A7FF}@font-face{font-family:Roboto;font-style:normal;font-weight:700;font-display:swap;src:url(https://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmWUlfBBc4AMP6lQ.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}@font-face{font-family:Ramabhadra;font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/ramabhadra/v15/EYq2maBOwqRW9P1SQ83LSghMXrmV03t9Qw.woff2) format('woff2');unicode-range:U+0951-0952,U+0964-0965,U+0C00-0C7F,U+1CDA,U+200C-200D,U+25CC}@font-face{font-family:Ramabhadra;font-style:normal;font-weight:400;font-display:swap;src:url(https://fonts.gstatic.com/s/ramabhadra/v15/EYq2maBOwqRW9P1SQ83LShRMXrmV03s.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}body{background:#d6d6d6}.heding h2{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:24px;text-transform:uppercase;color:#f00201;padding:0 20px 0!important}body{margin:0;padding:0;overflow-x:hidden}hr{margin-top:10px;margin-bottom:10px;border:0;border-top:1px solid #eee}.entertainment-telugu .entertainment-flex::-webkit-scrollbar{width:5px;height:10px;display:block}.entertainment-telugu .entertainment-flex::-webkit-scrollbar-track-piece{background:#f3f3f3}.text{text-align:center;height:100px;background:#262626;color:#fff}.text h2{margin:0;line-height:100px;font-size:48px}.text-white{color:#fff}.quote{color:rgba(0,0,0,.1);text-align:right;margin-bottom:0;position:relative;top:-45px}.close-menu,.open-menu{cursor:pointer;border:none;outline:0;color:#fff;background:0 0}.close-menu{position:absolute;top:0;right:2rem;border:none;outline:0;color:#fff;background:0 0}.close-menu svg{color:#f00201;top:-1px;position:relative}#ads2{margin:10px auto;text-align:center}#ads2{width:968px;height:90px}#ads2 img{width:968px;height:90px}de a{text-decoration:none}aside li,aside ul{list-style:none;margin:0;padding:0}aside{width:100%;float:left;padding:0}aside.horiz{width:100%;margin-top:40px}aside a.nhoodButton{display:block;width:100%;padding:10px 0;font-size:20px;margin:0 0 12px 0;-webkit-transition:all .1s ease-in-out;-moz-transition:all .1s ease-in-out;-ms-transition:all .1s ease-in-out;-o-transition:all .1s ease-in-out;transition:all .1s ease-in-out;color:#fff}aside.horiz a.nhoodButton{margin-bottom:0}aside>ul li{position:relative}aside.horiz>ul>li{width:30%;float:left}aside.horiz>ul>li:first-child{margin-right:5%}aside.horiz>ul>li:last-child{float:right}aside>ul i.fa{position:absolute;padding:0 12px 0 12px;top:10px;right:0;font-size:20px!important;color:#fff;border:solid 0 #fff;cursor:pointer;text-shadow:0 1px 1px #000}aside>ul ul.nhoodDropInner{position:absolute;z-index:10;display:none;background:#333}aside>ul ul.nhoodDropInner.top{z-index:11}aside>ul li.openInner ul.nhoodDropInner{display:block;top:42px;left:0;width:100%;border-bottom:solid 5px #000;border-top:solid 1px #fff}aside>ul ul.nhoodDropInner li{padding:10px 10px;text-align:left;font-size:15px;border-bottom:1px solid #f3f3f3}aside>ul ul.nhoodDropInner li a{color:#fff}aside>ul ul.nhoodDropInner li a.active{color:#999}.ott .andhra-pradesh{padding:0 15px}.andhra-content.ott .reelss-ul{width:80%}.ott .politics img{border-radius:7px;display:block}.ott .politics{max-width:42px;margin-right:10px}.ott .politics-flex h5{margin-right:15px;color:#f00201;font-size:18px;font-weight:600;white-space:nowrap}.ott .content-flex p.active{width:100%;margin-right:15px}.ott .content-flex label{margin:0;color:#f00201}.span-btn{background:#f00201;color:#fff;border:0;border-radius:5px;margin-bottom:10px}.ott-bg{background:#d6d6d6;padding:10px;margin:0 10px}.ott .reelss-ul a{display:none}.ott .andhra-pradesh .politics-business .politics-flex{width:80%;display:flex;align-items:center;margin-left:0}.ott .politics-flex span{background-color:#f3f3f300;text-align:left;padding:0}@media (max-width:800px){aside{min-width:300px}}@media (max-width:600px){aside.horiz{width:300px}aside.horiz ul li{width:100%;margin-bottom:10px}aside.horiz ul li:last-child{margin-bottom:0}}.search{font-size:12px;font-weight:100;padding:15px}.reelss-ul{display:flex;align-items:center;width:100%;justify-content:space-between;margin:0 auto}.reelss-ul img{padding-right:10px}.reelss-ul a{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:16px;line-height:25px;color:#000;display:flex;align-items:center;justify-content:center;margin:0 20px}.navbar-form .btn-primary:hover{color:#f00201;background-color:#28609000;border-color:#f00201}.tupaki-heding{display:flex;align-items:center;justify-content:space-between;width:100%;margin:0 auto}.tupaki-heding .heding{width:30%}.flex-list{width:70%}.navbar-brand>img{display:block;width:95%}.navbar-right{padding:7px;margin:0 auto;display:flex;align-items:center;justify-content:center;padding:0}.list-inline a .fa-2x{font-size:17px;background:#f00201;color:#fff;border-radius:7px;width:30px;height:30px;display:flex;align-items:center;justify-content:center;margin:0 auto}.list-inline a{margin:5px 6px}.navbar-form{padding:10px 6px}.list-inline{padding-left:0;list-style:none;display:flex;align-items:center;justify-content:center;flex-wrap:wrap;width:100%;margin:0 auto;max-width:calc(100% - 50px)}.telugu{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:18px;line-height:25px;color:#fff;background:#f00201;border:0;width:115px;height:42px;border-radius:30px}.sidenav{height:100%;width:0;position:fixed;z-index:1;top:86px;right:0;background-color:#111;overflow-x:hidden;transition:.5s;padding-top:15px}.sidenav a{padding:0 8px 8px 32px;text-decoration:none;font-size:25px;color:#818181;display:block;transition:.3s;text-align:left}.sidenav a:hover{color:#f1f1f1}.sidenav .closebtn{position:absolute;top:0;right:0;font-size:36px;margin-left:50px}.side-svg svg{color:#f00201}.dropdown-btn{padding:6px 8px 6px 16px;text-decoration:none;font-size:20px;color:#fff;display:block;border:none;background:0 0;width:100%;text-align:left;cursor:pointer;outline:0}.dropdown-container{display:block;background-color:#262626;padding-left:8px;overflow:auto;height:auto;margin-bottom:54px}.fa-caret-down{float:right;padding-right:8px}.navbar-fixed-top,header .navbar-fixed-bottom{position:relative}header .navbar-default{background-color:#f00201;border-color:#f00201}header .navbar-default .navbar-nav>li:hover{color:#fff}header .navbar-default .navbar-nav>li>a{font-family:Roboto,sans-serif;font-style:normal;font-weight:500;font-size:18px;line-height:200.68%;padding:0 10px;text-transform:uppercase;color:#fff}.collapse.in{text-align:center}header .navbar-default .navbar-nav>li>a:hover{color:#fff}header .navbar-default .navbar-nav>.active>a,header .navbar-default .navbar-nav>.active>a:focus,header .navbar-default .navbar-nav>.active>a:hover{color:#fff;background-color:transparent}header .navbar-default .navbar-nav>li:hover{border-color:#89caee}header .navbar-default .navbar-nav>li:nth-child(8){border-right:0}header .navbar-default .topbar{background:#d6d6d6;padding:10px 0}header .navbar-default .topbar ul{list-style:none;margin:0;width:100%;margin:0 auto}header .navbar-default .topbar ul li{display:inline-block;position:relative;padding-left:10px;padding-right:10px;transition:all .4s}header .navbar-default .topbar ul li:before{content:"";height:60%;width:2px;background:gray;position:absolute;left:-3px;top:5px;transition:all .4s}header .navbar-default .topbar ul li:first-child:before{display:none}header .navbar-default .topbar ul li:nth-child(6):after{content:""}header .navbar-default .topbar a{color:#58585a;font-family:Roboto,sans-serif;font-weight:400;font-size:18px;line-height:27px;text-align:center;text-transform:capitalize;color:#000}header .navbar-default .topbar a span{content:'|';padding-left:10px}header .navbar-default .topbar-logo .navbar-row{display:flex;align-items:center;justify-content:space-between;width:100%;margin:0 auto}header .navbar-default .topbar a:hover{color:#f00201;text-decoration:none}header .navbar-default .topbar a.active{color:#f00201}header .navbar-default .topbar-logo{background:#fff;padding:10px 10px}header .navbar-default .topbar-logo .navbar-brand{padding:5px;height:auto}header button.btn-primary{background-color:#58585a00;border-color:#58585a;border:0;text-transform:uppercase;border-radius:0;color:#b7b7b7}header .navbar-form input{width:277px!important;height:38px;background:#f0f0f1;box-shadow:none;font-size:12px;margin-right:10px;border:0}header .navbar{border:0;margin-bottom:0}header .navbar .navbar-nav{display:flex;margin:0 auto;align-items:center;justify-content:center;float:none;overflow:auto;white-space:nowrap;width:100%;overflow:auto}header .navbar .navbar-collapse{text-align:center}.navbar-fixed-top .navbar-collapse,header .navbar-fixed-bottom .navbar-collapse{max-height:60px}header .navbar-form input{width:277px!important;height:38px;background:#f0f0f1;box-shadow:none;font-size:12px;margin-right:10px}header .navbar-form button.btn-primary{width:31px;height:31px;padding:0}.navbar-right .input-group-btn .btn-primary .fa.fa-search{font-size:20px;color:#979797;display:flex;align-items:center;justify-content:center;margin:0 auto}.navbar-right .side-svg{font-size:30px;cursor:pointer;display:flex;align-items:center;justify-content:center;margin:0 auto}header .navbar-form button.btn-primary img{margin-top:-5px}header .second_menu{display:none}.about{position:fixed;z-index:10;bottom:10px;right:10px;width:40px;height:40px;display:flex;justify-content:flex-end;align-items:flex-end;transition:all .2s ease}.about .bg_links{width:40px;height:40px;border-radius:100%;display:flex;justify-content:center;align-items:center;background-color:rgba(0,0,0,.2);border-radius:100%;backdrop-filter:blur(5px);position:absolute}.about .logo{width:40px;height:40px;z-index:9;background-image:url(https://rafaelalucas91.github.io/assets/codepen/logo_white.svg);background-size:50%;background-repeat:no-repeat;background-position:10px 7px;opacity:.9;transition:all 1s .2s ease;bottom:0;right:0}.about .social{opacity:0;right:0;bottom:0}.about .social .icon{width:100%;height:100%;background-size:20px;background-repeat:no-repeat;background-position:center;background-color:transparent;display:flex;transition:all .2s ease,background-color .4s ease;opacity:0;border-radius:100%}.about .social.portfolio{transition:all .8s ease}.about .social.portfolio .icon{background-image:url(https://rafaelalucas91.github.io/assets/codepen/link.svg)}.about .social.dribbble{transition:all .3s ease}.about .social.dribbble .icon{background-image:url(https://rafaelalucas91.github.io/assets/codepen/dribbble.svg)}.about .social.linkedin{transition:all .8s ease}.about .social.linkedin .icon{background-image:url(https://rafaelalucas91.github.io/assets/codepen/linkedin.svg)}.about:hover{width:105px;height:105px;transition:all .6s cubic-bezier(.64,.01,.07,1.65)}.about:hover .logo{opacity:1;transition:all .6s ease}.about:hover .social{opacity:1}.about:hover .social .icon{opacity:.9}.about:hover .social:hover{background-size:28px}.about:hover .social:hover .icon{background-size:65%;opacity:1}.about:hover .social.portfolio{right:0;bottom:calc(100% - 40px);transition:all .3s 0s cubic-bezier(.64,.01,.07,1.65)}.about:hover .social.portfolio .icon:hover{background-color:#698fb7}.about:hover .social.dribbble{bottom:45%;right:45%;transition:all .3s .15s cubic-bezier(.64,.01,.07,1.65)}.about:hover .social.dribbble .icon:hover{background-color:#ea4c89}.about:hover .social.linkedin{bottom:0;right:calc(100% - 40px);transition:all .3s .25s cubic-bezier(.64,.01,.07,1.65)}.about:hover .social.linkedin .icon:hover{background-color:#0077b5}.profile img{border-radius:100%}.profile{text-align:left;width:100%;overflow:hidden;padding:26px 10px;margin-top:40px}.entertainment-telugu.spacing .indrani .indrani-scroll{margin-bottom:4px}.profile p{font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:25px;color:#000}.bg-overlay{background-color:rgba(0,0,0,.7);position:relative;top:0;width:100%;height:100%;padding:100px}.ads-slider{padding:5px 0;position:relative}.ads-slider .swiper-button-next,.ads-slider .swiper-button-prev{top:45%;width:30px;height:30px;margin-top:calc(-1 * var(--swiper-navigation-size)/ 2);z-index:10;cursor:pointer;display:flex;align-items:center;justify-content:center;color:#ff3131;background:#fff;border-radius:100%}.ads-slider .swiper-button-next:after,.ads-slider .swiper-button-prev:after{font-size:15px;font-weight:bolder}.swiper-container{width:100%;padding-top:50px;padding-bottom:50px}.carousel-control-next:focus,.carousel-control-next:hover,.carousel-control-prev:focus,.carousel-control-prev:hover{color:#333;text-decoration:none;outline:0;opacity:.9}.carousel-control-prev{left:0}.carousel-control-next{right:0}.carousel-control-next,.carousel-control-prev{position:absolute;top:10px;z-index:1;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:end;width:90%;color:#333;text-align:center;opacity:.5;transition:opacity .15s ease}.entertainment-telugu.spacing #carousel .carousel-control-next{top:1px;opacity:1}.entertainment-telugu.spacing #carousel .carousel-control-prev{top:1px;opacity:1}.carousel-control-prev-icon{background-image:url(/theme_teal/images/arrow-left.svg)!important;background-color:#333;padding:12px;opacity:1}.carousel-control-next-icon{background-image:url(/theme_teal/images/arrow-right.svg)!important;background-color:#f00201;padding:12px;opacity:1}.carousel-control-next-icon,.carousel-control-prev-icon{display:inline-block;width:20px;height:20px}.sr-only{position:absolute;width:1px;height:1px;padding:0;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}.poll .swiper-button-next,.poll .swiper-button-prev{position:absolute;top:10px;z-index:1;display:-ms-flexbox;display:flex;-ms-flex-align:center;align-items:center;-ms-flex-pack:center;justify-content:end;width:90%;color:#333;text-align:center;opacity:.5;transition:opacity .15s ease}.poll .card-text-content{padding:0 10px;position:relative;bottom:0;background:rgb(240 2 1 / 88%);color:#fff}.main .container .glider-contain .glider .card-image{margin-right:.5rem;background:#fff;border:none;outline:0;box-shadow:0 3px 6px rgba(0,0,0,.16),0 3px 6px rgba(0,0,0,.23);border-radius:2px}.main .container .glider-contain .glider .card-image img{display:block;position:relative;left:0;bottom:0;width:100%;height:auto;object-fit:cover}.main .container .glider-contain .glider-next,.main .container .glider-contain .glider-prev{font-size:1.5rem;background:#454545;color:#fff;margin-top:1rem;width:3rem;height:3rem;line-height:3rem;border-radius:50%}.main .container .glider-contain .glider-next .fas,.main .container .glider-contain .glider-prev .fas{margin-left:1rem}@media only screen and (max-width:768px){.main .glider-contain .glider-next,.main .glider-contain .glider-prev{display:none}}@media only screen and (min-width:769px){.main .glider-contain .dots{display:none}}.card{border-radius:3px;margin:0 auto;transition:box-shadow .25s;transform:scale(.94)}.card img{display:block;max-width:100%;height:auto;background-color:#eee}.website-wrapper.reviews .live-tabs.photo-gallery .card-text-content:hover{position:absolute;bottom:0;background:rgb(255 1 0 / 100%);color:#fff;width:100%;height:90px;background-color:rgba(255,0,0,.8);display:flex;align-items:center;justify-content:center;top:auto}.ads-slider .swiper-container .card-text-content{position:absolute;bottom:0;background:rgb(255 1 0 / 100%);color:#fff;width:100%;height:90px;background-color:rgba(255,0,0,.8);display:flex;align-items:center;justify-content:center}.card-text-content h3{font-size:20px;margin:0}.accordion{width:100%;padding:1.2rem 0;border-radius:0;background:#111}.accordion__heading{margin-bottom:1rem;padding:0 1.4rem}.accordion__item:not(:last-child){border-bottom:1px solid #d3d3d3}.accordion__btn{display:flex;justify-content:space-between;width:100%;padding:1.2rem 1.4rem;background:#262626;border:none;outline:0;color:#fff;font-size:1.2rem;text-align:left;cursor:pointer;transition:.1s}aside>ul .accordion__icon i{position:relative;top:0;font-size:16px!important}.accordion__btn .accordion__caption{font-size:17px}.header .navbar .menu-item.has-collapsible span.accordion__icon i::after{dispaly:none}.fa-lightbulb{padding-right:1rem}.accordion__icon{border-radius:50%;transform:rotate(0);transition:.3s ease-in-out;opacity:.9}.accordion__item--active .accordion__icon{transform:rotate(135deg)}.accordion__content{font-weight:300;max-height:0;opacity:0;overflow:hidden;color:#fff;transform:translateX(16px);transition:max-height .5s ease,opacity .5s,transform .5s}.accordion__content p{padding:1rem 1.8rem}.accordion__item--active .accordion__content{opacity:1;transform:translateX(0);max-height:100vh;text-align:left;padding:10px 15px}.accordion__content ul li{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:14px;line-height:261.68%;color:#fff}.website-wrapper{display:flex;justify-content:space-between;align-items:start;position:relative;padding:10px 0;background:#d6d6d6}.plus-minus-toggle{cursor:pointer;height:21px;position:relative;width:21px}.plus-minus-toggle:after,.plus-minus-toggle:before{background:#000;content:'';height:5px;left:0;position:absolute;top:0;width:21px;transition:transform .5s ease}.plus-minus-toggle:after{transform-origin:center}.plus-minus-toggle.collapsed:after{transform:rotate(90deg)}.plus-minus-toggle.collapsed:before{transform:rotate(180deg)}.live-ads{position:relative;margin:5px 0;display:flex;align-items:center;margin:0 auto;padding:0 40px}.live-news{width:100%;margin:0 auto;display:flex;background:#333;align-items:center;justify-content:center}.ad-ons img{width:100%;width:300px;height:400px}.ad-ons{height:auto;display:flex;align-items:start;justify-content:center;margin:0 auto 10px;width:100%}.indrani h3{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:22px;line-height:10px;text-transform:uppercase;padding:7px;color:#f00201;margin-top:0;margin-bottom:20px;text-align:center}.indrani .indrani-scroll .poll #carousel .entertainment-flexs{display:flex;text-align:center}.indrani .indrani-scroll .poll #carousel .entertainment-flexs img{width:78px;height:104px}.indrani .indrani-scroll .poll #carousel .entertainment-flexs .entertainment-scroll:hover{background:#ebebeb00}.indrani .indrani-scroll .poll #carousel .carousel-control-next{top:25px;opacity:1}.indrani .indrani-scroll .poll #carousel .carousel-control-prev{top:25px;opacity:1}#carousel .carousel-control-next-icon,.carousel-control-prev-icon{border-radius:10px}#carousel .carousel-control-next .css-i6dzq1{background-color:#f00201;border-radius:50%}#carousel .carousel-control-prev .css-i6dzq1{background-color:#f00201;border-radius:50%}.live-news .live{background:#141414;height:40px;display:flex;width:145px;position:relative;top:0;margin:0;align-items:center;padding:0 10px;font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:16px;line-height:22px;text-align:center;text-transform:uppercase;color:#fff;z-index:9}.marquee{position:absolute;display:flex;align-items:center;width:100%}.marquee a{color:#fff;text-decoration:none;font-size:16px;width:100%;white-space:normal;font-family:Roboto,sans-serif;font-weight:700}.marquee div{display:flex;align-items:center;justify-content:center;margin:0 auto;background:#f00201}.marquee span{display:flex;align-items:center}.marquee span .css-i6dzq1{width:20;height:20}.live-news .live:after{position:relative;content:'';width:0;height:0;border-top:20px solid transparent;border-bottom:20px solid transparent;float:left;border-right:20px solid #f00201;left:22px;top:0}@keyframes no-transform{100%{transform:none}}.scrollbox{display:flex;align-items:center;padding:0 0;overflow:hidden}.scrollbox--primary{background-color:#f00201;color:#fff;width:98%}.live-news .main{margin-right:30px;overflow:hidden}.live-news ol>li{display:table-cell;height:30px;position:relative;padding:0;margin:0;text-align:center;border:1px solid transparent}.live-news ol>li>div{position:relative;height:100%;width:100%;margin-right:50px;font-family:Roboto,sans-serif;font-style:normal;font-weight:100;font-size:18px;text-align:center;color:#fff;line-height:25px}.live-news ol>li:hover{background-color:#f00201;cursor:pointer;color:#fff}.live-news ol{display:table;width:100%;padding:0;margin:0;position:relative}.live-news ol>li>div:after{content:'';border-width:14px;display:block;z-index:2;top:0;border:solid #fff;border-width:0 4px 4px 0;display:flex;align-items:center;justify-content:center;padding:13px;-webkit-transform:rotate(135deg);float:left;margin:0 auto}.scrollbox--secondary{background-color:#2f722f;color:#fff}.scrollbox--reverse__item{animation-direction:reverse}.scrollbox:hover__item{animation-play-state:paused}.scrollbox__item{flex:1 0 auto;width:auto;margin:0 0;font-size:1.5rem;transform:translateX(50%);animation:no-transform 15s linear infinite}#features{height:500px;position:relative;-webkit-transition:width 1s,height 1s;transition:width 1s,height 1s}#features img{width:120px;height:600px}.btn1{color:#9e9e9e;background:rgba(245,245,245,.2);width:15px;height:15px;border-radius:50%;padding:5px;text-align:center;font-size:12px;position:absolute;right:5px;top:5px;cursor:pointer}.live-tabs{position:relative;width:70%;display:flex;flex-direction:column;margin:0 auto;justify-content:center;overflow:hidden}.live-tabs a.aads{display:none}.tabs-wrapper{box-shadow:2px 1px 20px #ddd;padding:17px 0;height:auto;width:100%;background:#fff}.tab-content{width:100%}.top-news{width:100%;position:relative;margin-bottom:10px}.politics-business.top-news .politics img{border-radius:10px}.tab-content-flex:nth-child(0){display:flex}.content-flex{width:50%;display:flex;flex-direction:column;margin-right:20px}.content-flex .entertainment-content p{font-size:20px;padding-top:10px;font-weight:600;width:auto;color:#000}.content-flex .entertainment-content{padding:10px 10px}.politics-business.top-news hr{margin-top:15px;margin-bottom:15px}.content-flex p{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:20px;line-height:27px;color:#f00201}.content-flex:nth-child(2){display:flex;flex-direction:row}.politics-flex h3{margin:0;font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:12px;line-height:30px;text-transform:uppercase;color:#f00201}.politics-flex p{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:16px;line-height:25px;color:#000}.politics-business .content-flex{width:100%;display:flex;flex-direction:row;margin:0 auto;justify-content:space-between;align-items:center}.politics-business .content-flex .politics-flex{margin-left:10px}.politics-business .content-flex p{width:auto;-webkit-line-clamp:3}.politics-business{position:absolute;width:45%;top:18px;right:0}ul{list-style-type:none;padding-left:0}.nav-tabs{display:flex;border-bottom:0 solid #ddd;align-items:start;justify-content:start;margin:0 10px}.tab-content .content-flex h1{margin:0 10px;padding-top:15px;width:195px;position:relative}.tab-content .content-flex img{margin:0 0 0 10px;border-radius:10px}.politics-business.top-news .content-flex img{margin:0}.tab-content .content-flex h1:after{content:"";width:180px;height:2px;background:#f00201;position:absolute;bottom:0;left:0}.tab-content .content-flex hr{margin-left:12px;width:40%}.nav-tabs li{border:2px solid #000;width:185px;height:50px;font-family:Roboto,sans-serif;font-weight:700;font-size:18px}.tab{padding:.5rem 1.5rem;cursor:pointer;border-radius:4px;margin-right:.5rem;transition:all .3s ease 0s;color:#333;width:185px;height:50px;background:#fff;border-radius:5px;text-align:center;display:flex;justify-content:center;align-items:center}.tab.is-active{color:#fff;background:#000;border-radius:5px}.content-flex h1{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:22px;line-height:33px;text-transform:uppercase;color:#f00201;margin:0;padding-top:20px}.content-flex hr{margin:0;margin-top:0;margin-bottom:10px;border:0;border-top:0 solid #f00201;width:30%;right:0}.view-all{position:absolute;bottom:20px;right:25px}.view-all a{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:18px;line-height:25px;color:#000;display:flex;align-items:center}.view-all a img{padding-right:10px}.tab-panel{display:none}.tab-panel p{line-height:1.6}.tab-panel.is-active{display:flex;width:100%;align-items:self-start}.latest-news-entertainment{position:relative;display:flex;margin:10px auto 10px;width:100%;align-items:start;height:100%}.entertainment-scroll{display:flex;align-items:center;justify-content:start;line-height:22px;padding:0 10px;margin:0 auto;width:100%}.latest-news-entertainment.indrani-scroll .entertainment-scroll{padding:0}#fade-quote-carousell .entertainment-scroll{padding:13px 0;flex-direction:column}.entertainment-scroll img{width:25%;border-radius:5px}.entertainment-scroll p{margin:0 10px 0;font-style:normal;font-weight:200;font-size:16px;line-height:23px;color:#000;padding:10px 0;font-family:Roboto,sans-serif;width:100%;height:58px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;text-overflow:ellipsis}.latest-news-entertainment.indrani-scroll .entertainment-scroll p{width:auto}.entertainment-telugu.spacing .entertainment-scroll p{font-family:Ramabhadra;font-weight:500;font-size:18px}.entertainment-telugu.spacing h2{background:#000}.entertainment-telugu h2{background:#f00201;font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:22px;line-height:1.4;text-align:center;text-transform:uppercase;margin:0 auto 0;color:#fff;padding:5px;width:100%}.todays-poll{width:100%}.todays-poll h2{background:#000;font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:16px;padding:10px;text-transform:uppercase;text-align:center;color:#fff;margin:10px 0}.entertainment-telugu #features img{width:100%;height:auto}.entertainment-telugu{background:#fff;margin:0 auto;position:relative;width:34%;display:flex;flex-direction:column;justify-content:space-between}.entertainment-telugu.trending .entertainment-scroll img{width:auto}.andhra-content.political-news .andhra-pradesh h4{width:100%;height:auto;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;text-overflow:ellipsis}.entertainment-telugu.spacing a.movie-ads-run img{width:100%}.latest-news-entertainment .entertainment-telugu.spacing hr{margin-top:5px;margin-bottom:5px;border:0;border-top:1px solid #d6d6d6;width:100%}.entertainment-telugu.spacing{margin:0 10px;overflow:hidden}.latest-news-entertainment.indrani-scroll .entertainment-telugu.spacing{overflow:hidden;height:1073px}.entertainment-telugu.spacing .movie-ads-run{margin-bottom:10px}.entertainment-telugu .live-ads #features{width:auto;height:100%;position:relative;padding:5px;-webkit-transition:width 1s,height 1s;transition:width 1s,height 1s}form{display:flex;flex-wrap:wrap;flex-direction:column;margin:20px auto}label{display:block;cursor:pointer;font-weight:500;position:relative;overflow:hidden;margin-bottom:10px;width:100%}label input{position:absolute;left:-9999px}label input:checked+span{background-color:#d6d6e5}label input:checked+span:before{box-shadow:inset 0 0 0 .4375em #00005c}label span{display:block;align-items:center;padding:.375em .75em .375em .375em;border-radius:0;transition:.25s ease;background-color:#f3f3f3;text-align:center;font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:25px;color:#000}.submit{font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:14px;line-height:19px;color:#fff;background:#f00201;border-radius:51px;padding:7px 30px;border:0;display:flex;margin:11px auto 0;align-items:center}label span:hover{background-color:#d6d6e5}label span:before{display:flex;flex-shrink:0;content:"";background-color:#fff;width:1.5em;height:1.5em;border-radius:0;margin-right:.375em;transition:.25s ease;box-shadow:inset 0 0 0 .125em #00005c}label span:before{display:none}.entertainment-telugu .view-all a{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:18px;line-height:25px;color:#000;text-align:center;display:flex;align-items:center;justify-content:center;padding:8px}.entertainment-telugu .view-all{background:#c4c4c4;width:100%;position:relative;bottom:0;right:0}.entertainment-telugu .entertainment-flex{height:900px;overflow:auto}.latest-news-entertainment.indrani-scroll .entertainment-telugu .entertainment-flex{height:991px;overflow:auto}.tabs-all .btn{border:none;background:0 0;border-radius:3px;font-family:Roboto,sans-serif;font-style:normal;font-weight:800;font-size:16px;line-height:35px;color:#000;padding:5px 10px 5px 10px;text-decoration:none;margin:5px}.tabs-all .active{background:0 0;box-shadow:none;text-decoration:none;color:#f00201}#parent{display:flex;flex-wrap:wrap;background:#fff;padding:10px 0 10px}#parent .politics-flex p{font-family:Roboto,sans-serif;font-style:normal;font-weight:200;font-size:15px;color:#000;line-height:19px;width:auto;height:auto;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;text-overflow:ellipsis}.tabs-all .box{padding:0 0 0;height:auto;margin:0 auto;text-align:center;border-radius:3px;color:#000;max-width:300px}.tabs-all .box .content-flex img{border-radius:5px}.reelss.russiaukraine .swiper-button-next:after,.reelss.russiaukraine .swiper-button-prev:after{font-weight:bolder}.reelss.russiaukraine .swiper-button-next,.reelss.russiaukraine .swiper-button-prev{top:50%}.reelss.russiaukraine .swiper-button-next,.reelss.russiaukraine .swiper-button-prev{width:40px!important;height:40px!important}.entertainment-scroll:hover{background:#ebebeb}.latest-news-entertainment hr{margin-top:5px;margin-bottom:5px;border:0;border-top:1px solid #eee}.entertainment-scroll p:hover{color:#f00201}#parent .box hr{margin-top:15px;margin-bottom:0}#parent .box h3{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:15px;line-height:25px;text-transform:uppercase;color:#f00201}.tabs-all .box h3{text-align:left;font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:18px;line-height:25px;text-transform:uppercase;color:#f00201;margin:0;text-align:left}.tabs-all .content-flex{width:100%;display:flex;align-items:center;justify-content:center;flex-direction:row}.tabs-all .politics-flex{text-align:left;margin-left:10px}.tabs-all .spacer{clear:both;height:20px}.tabs-all{width:100%;position:relative;margin:10px 0}.reelss.thaja-varthalu{margin:10px auto 10px}.btn:active:focus,.btn:focus{outline:0 auto -webkit-focus-ring-color!important;outline-offset:-2px}.btn:active{box-shadow:inset 0 3px 5px rgb(0 0 0 / 0%)}.andhra-content{margin:10px 0;position:relative;background:#fff;width:100%;padding:0 0 20px}.andhra-content hr{margin-top:5px;margin-bottom:10px;border:0;border-top:2px solid #878686}.andhra-content .heding h2{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;line-height:33px;margin:0;text-transform:uppercase;font-size:22px;color:#f00201;padding:15px 10px 0!important}.andhra-content .heding hr{border-top:2px solid #545454}.andhra-pradesh{display:flex;align-items:start;justify-content:center;margin:0 auto;width:98%;background:#fff}.andhra-content.office .andhra-pradesh{width:100%}.andhra-pradesh .politics-business hr{margin-top:13px;margin-bottom:13px;border:0;border-top:2px solid #eee}.district .andhra-pradesh .content-flex{width:50%;display:flex;flex-direction:column;margin-right:20px}.andhra-pradesh .politics-business{position:relative;width:45%;top:0}.andhra-content.office .andhra-pradesh .politics-business{margin:0 10px}.andhra-pradesh .content-flex .district p{padding-left:5px;font-size:15px}.andhra-district .andhra-pradesh .district-min p{padding-left:0;padding-top:10px;font-size:18px;font-weight:100;width:100%;color:#f00201;font-family:Roboto,sans-serif}.andhra-district .andhra-pradesh .district .politics-business .content-flex p{padding-left:6px;font-size:15px;width:100%;line-height:20px;-webkit-line-clamp:3;padding:5px 0 20px;height:65px}.andhra-district .andhra-pradesh .district .politics-business .content-flex p:hover{color:#f00201}.andhra-district .andhra-pradesh .district .politics-business.five-cols .content-flex p{-webkit-line-clamp:2;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;text-overflow:ellipsis;width:100%;height:40px}.office .andhra-pradesh .content-flex p.active,.office .andhra-pradesh .content-flex p:hover{color:#f00201}.related.entertainment-sec .andhra-pradesh .district .politics-business .politics{width:100%}.related.entertainment-sec .andhra-pradesh .district .politics-business .politics img{width:100%}.andhra-district .andhra-pradesh .district-min{width:40%;display:flex;flex-direction:column;margin-right:0;margin-left:0}.andhra-district .andhra-pradesh .district-min img{width:100%;border-radius:10px}.andhra-district .andhra-pradesh .content-flex{width:100%}.district .politics-business{width:50%!important;margin-left:10px}.district .politics-business.five-cols{width:39%!important}.andhra-pradesh .district .politics-business{position:relative;top:0;width:100%}.andhra-pradesh .district{display:flex;width:60%}.andhra-district .andhra-pradesh .district .content-flex{width:100%;display:flex;margin-right:20px;align-items:center;max-width:300px;flex-direction:row}.andhra-district .andhra-pradesh .district .content-flex img{width:100%;border-radius:5px}.andhra-pradesh .politics-business .politics-flex{width:80%}.andhra-pradesh .politics-business .politics-flex p{width:100%}.reels{width:100%;display:flex;margin:0 auto;position:relative}.reelss hr{border:0;border-top:2px solid #a29d9d;width:100%;margin:0 0}.reelss .heding h2{font-family:Roboto,sans-serif;font-size:22px;margin:0;padding:15px 10px 5px!important}.reelss .swiper-button-next,.reelss .swiper-button-prev{top:55%;font-weight:700;width:40px!important;height:40px!important}.reelss .h-40{height:2.5rem}.w-40{width:2.5rem}.loco_cat.loco_section .container{width:1170px;margin:0;padding:0}.loco_cat.loco_section .swiper-slide{flex-shrink:0;width:100%;height:100%;position:relative;transition-property:transform}.loco_listing__carousel{margin-left:-15px;margin-right:-15px;padding-left:15px;padding-right:15px}.loco_listing__card{border-radius:.5rem}.loco_listing__card_verify{color:var(--linkColor)}.loco_listing__card_cta{left:0;right:0;top:calc(100% - 1.25rem);text-align:right}.loco_listing__card_cta_tel{transition:all .2s ease}.loco_listing__card_cta_number{visibility:hidden;opacity:0;position:absolute;z-index:-1;width:0}.loco_listing__card_cta_tel.active{padding-right:1rem}.loco_listing__card_cta_tel.active .loco_listing__card_cta_number{visibility:visible;opacity:1;position:static;z-index:1;width:auto}.loco_listing_card_v2 div.card-text{white-space:nowrap;overflow:auto}.loco_listing_card_v2 div.card-footer{white-space:nowrap;overflow:auto}.loco_listing_card_v2__cat{max-width:18px}.loco_listing_card_v2 .card-text>a>i{font-size:1.125rem;color:var(--secondary)}.swiper-pagination-bullet-active{background:var(--primary)}.loco_carousel__pagination{bottom:0!important}.loco_single_carousel__slide{max-height:28.125rem}.loco_single_carousel__slide a img{height:auto;width:100%}.loco_single_carousel_btns{z-index:3;left:0;right:0;top:50%;transform:translateY(-50%)}.loco_listing_list_view{display:flex;align-items:center;flex-direction:row}.loco_listing_list_view .loco_listing__pos{flex-basis:14.375rem}.loco_listing_list_view .loco_listing__pos>a{display:block;height:10.625rem}.loco_listing_list_view .loco_listing__pos>a img{height:100%;-o-object-fit:cover;object-fit:cover}.loco_listing_card_v2.loco_listing_list_view>a{max-width:40%;height:11.4375rem}.loco_listing_card_v2.loco_listing_list_view>a>img{height:100%;-o-object-fit:cover;object-fit:cover}.loco_listing_list_view .loco_listing__card_cta{top:15px;left:auto}.loco_listing__carousel_slide{max-width:370px}.loco_list_wrapper{width:60%}.loco_searchpage.loco_searchpage__v2 .loco_searchpage__col{width:55%}.loco_searchpage.loco_searchpage__v2 .loco_searchpage__map{width:45%}.loco_searchpage__col{width:50%}.loco_searchpage__map{top:66px;right:0;bottom:0;z-index:2}.my_posts{margin-bottom:30px}.youtube-player{position:relative;width:640px;height:400px;margin:auto;cursor:pointer}.youtube-player.pristine:hover{-webkit-filter:brightness(75%)}.youtube-player img{width:100%}.youtube-player.pristine::before{content:'';position:absolute}.youtube-player.pristine::after{content:'';position:absolute}.youtube-player.pristine:hover::before{opacity:1;top:50%;left:50%;margin-top:0;margin-left:0;height:0;width:0;border-left:35px solid #f21d16;border-top:20px solid transparent;border-bottom:20px solid transparent;transition:opacity .2s ease}.youtube-player.pristine:hover::after{opacity:.6;top:50%;left:50%;margin-top:-15px;margin-left:-25px;height:70px;width:70px;border:2px solid #f21d16;transition:opacity .2s ease;border-radius:100%;background:#3333336e}.carousel__btn_prev{background:#fff;color:#f21d16!important;border-radius:50%;font-size:20px;width:40px}.carousel__btn_next{background:#fff;color:#f21d16!important;border-radius:50%;font-size:20px;width:40px;float:right}.loco_section__carobtn{position:absolute;width:100%;z-index:9;top:50%}.loco_cat.loco_section .loco_section__title{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:24px;line-height:33px;text-transform:uppercase;color:#f00201}.loco_section__heading hr{width:10%;border:1px solid #f21d16;right:0;text-align:right;margin:0}.reelss .loco_cat.loco_section .swiper-slide{flex-shrink:0;width:100%;height:100%;position:relative;transition-property:transform}.reelss .loco_cat.loco_section .swiper-slide:hover svg{display:block;position:absolute;margin:0;display:flex;align-items:center;justify-content:center}.reelss .loco_cat.loco_section .swiper-slide:hover .shadow-svg{background:#333333a8;position:absolute;top:0;margin:0;height:100%;width:100%;display:flex;align-items:center;justify-content:center}.reelss .loco_cat.loco_section .swiper-slide img{width:100%}.reelss .loco_cat.loco_section .swiper-containernn .swiper-slide img{width:100%;border-radius:5px}.reelss .loco_cat.loco_section .swiper-containernn-recent .swiper-slide img{width:100%;border-radius:5px}.reelss.stories .loco_cat.loco_section .swiper-slide img{width:97%;border:15px solid #d6d6d6}.reelss .loco_cat.loco_section .swiper-slide svg{display:none}.reelss .loco_cat.loco_section .swiper-slide .svg--position{position:relative;display:flex;align-items:center;justify-content:center;margin:0 auto}.reelss .loco_cat.loco_section .swiper-slide h4{font-family:Roboto,sans-serif;font-style:normal;font-weight:200;font-size:15px;line-height:20px;color:#000;text-align:left;width:100%;height:auto;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;text-overflow:ellipsis}.reelss .loco_cat.loco_section .swiper-slide h4:hover{color:#f00201;font-weight:100}.reelss .loco_cat.loco_section .swiper-slide.swiper-slide-active h4{color:#f00201}.video-gallery{display:flex;align-items:center;justify-content:center;margin:0 auto}.video-flex{display:block}.video-flex h4{font-size:15px;font-weight:600}.video-flex h4.active,.video-flex h4:hover{color:#f00201}.video-flex h4.active:hover,.video-flex h4:hover{color:#f00201;font-weight:600}.video-flex .svg--position{display:flex;align-items:center;justify-content:center;margin:0 10px 0 0}.video-stories hr{margin:0 0 20px;width:100%}.video-stories h2{margin:0}.video-flex .svg--position svg{position:absolute}.reelss .loco_cat.loco_section .swiper-slide .svg--position svg{position:absolute;display:flex;align-items:center;justify-content:center;margin:0 auto}.reelss .loco_cat.loco_section .swiper-slide .svg--position .svg{display:none}.reelss.recently-viewed .heding h2{padding:15px 10px 5px!important}.reelss.video-stories .heding h2{padding:15px 10px 5px!important}.reelss .loco_cat.loco_section .swiper-slide .svg--position:hover .svg{position:absolute;display:flex;align-items:center;justify-content:center;margin:0 auto;width:20%}.video-flex .svg--position .svg{position:absolute;display:flex;align-items:center;justify-content:center;margin:0 auto;width:20%}.video-flex .content{margin:0 10px}.video-icon-btn .video-flex .svg--position .svg img{width:25%}.reelss.stories .loco_cat.loco_section .swiper-slide:hover h2{border:0 solid #d6d6d6;background:#00000000;padding:25px}.reelss.stories .loco_cat.loco_section .swiper-slide:hover .shadow-svg{border:15px solid #d6d6d6;width:97%}.reelss .loco_cat.loco_section .swiper-slide:hover h2{display:block;font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:15px;line-height:21px;text-align:center;color:#fff;background:#00000054;position:absolute;top:0;margin:0;height:100%;width:100%;display:flex;align-items:end;padding:0 10px;padding-bottom:16px;justify-content:center}.reelss.thaja-varthalu hr{border:0;border-top:2px solid #a29d9d;width:100%;margin:0 0 20px}.reelss.thaja-varthalu h2{margin-top:0;margin-bottom:0}.reelss .swiper-containern .swiper-slide svg{display:none}.reelss .swiper-containern .swiper-slide:hover svg{display:block}.reelss .loco_cat.loco_section .swiper-slide h2{display:none}.reelss .swiper-containerns .swiper-slide{min-height:75vh}.reelss .swiper-containerns .swiper-slide:hover h2{display:block;font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:14px;line-height:19px;text-align:center;color:#fff;background:#333333a8;padding:420px 50px 30px;position:relative;bottom:0;margin:0;width:100%}.reelss.stories .swiper-button-prev{left:25px!important;right:auto}.reelss.stories .swiper-button-next{right:25px!important;left:auto}.reelss.thaja-varthalu .swiper-button-next,.reelss.thaja-varthalu .swiper-button-prev{top:45%}.reelss.recently-viewed .swiper-button-next,.reelss.recently-viewed .swiper-button-prev{top:50%}.reelss.video-stories .swiper-button-next,.reelss.video-stories .swiper-button-prev{top:52%}.office hr{width:100%;margin:0 0 15px}.office a{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:16px;line-height:25px;color:#000;display:flex;align-items:center;justify-content:center}.office a img{padding-right:10px}.andhra-content.office .andhra-pradesh .politics-business{margin:0 10px;border-right:1px solid #33333330;width:33%}.andhra-content.office .andhra-pradesh .politics-business:last-child{border-right:0 solid #33333330}.andhra-content.office .andhra-pradesh .politics-business .politics img{width:100px;height:60px;border-radius:5px}.andhra-content.office{margin:10px 0}.andhra-content.office .politics-business .content-flex{height:70px}.reelss.video-stories{margin:15px 0 10px}.reelss.recently-viewed{margin:10px 0 15px}.reelss.recently-viewed .heding h2{margin:0}.reelss.recently-viewed hr{border:0;border-top:2px solid #a29d9d;width:100%;margin:0 0 20px}.reelss.recently-viewed .loco_cat.loco_section .container{width:100%}.office .politics-business hr{width:90%;margin:10px 0 15px}.reelss .swiper-containerns .swiper-slide h2{display:none}.reelss .swiper-containernn .swiper-slide{min-height:0}.reelss .swiper-containernn-recent .swiper-slide{min-height:0}.reelss .swiper-containernnm .swiper-slide{min-height:0}.reelss .swiper-containernn .swiper-slide{min-height:0}.reelss .swiper-containernn-recent .swiper-slide{min-height:0}.reelss.thaja-varthalu .swiper-containernn .swiper-slide span{align-items:center;font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:13px;line-height:174.08%;color:#333;text-align:left;display:flex;margin:0 auto;width:100%}.reelss.thaja-varthalu .swiper-containernn-recent .swiper-slide span{align-items:center;font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:13px;line-height:174.08%;color:#333;text-align:left;display:flex;margin:0 auto;width:100%}.reelss.thaja-varthalu .swiper-containernn .swiper-slide span svg{display:block;text-align:left;margin-right:10px}.reelss.thaja-varthalu .swiper-containernn-recent .swiper-slide span svg{display:block;text-align:left;margin-right:10px}.reelss.thaja-varthalu .loco_cat.loco_section .swiper-slide:hover svg{position:relative;margin-right:10px}.reelss .swiper-containernn .swiper-slide h3{font-family:Roboto,sans-serif;font-style:normal;font-size:15px;line-height:20px;color:#333;text-align:left;width:100%;height:auto;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;text-overflow:ellipsis}.reelss .swiper-containernn-recent .swiper-slide h3{font-family:Roboto,sans-serif;font-style:normal;font-size:15px;line-height:20px;color:#333;text-align:left;width:100%;height:auto;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;text-overflow:ellipsis}.reelss .swiper-containernn .swiper-slide.swiper-slide-active span{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:13px;line-height:174.08%;color:#f00201}.reelss .swiper-containernn-recent .swiper-slide.swiper-slide-active span{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:13px;line-height:174.08%;color:#f00201}.reelss .swiper-containernn .swiper-slide.swiper-slide-active h3{font-family:Roboto,sans-serif;font-style:normal;font-weight:200;font-size:15px;line-height:20px;color:#f00201;text-align:left}.reelss .swiper-containernn-recent .swiper-slide.swiper-slide-active h3{font-family:Roboto,sans-serif;font-style:normal;font-weight:200;font-size:15px;line-height:20px;color:#f00201;text-align:left}.reelss .swiper-containernnm .swiper-slide .content{margin-left:10px}.reelss .swiper-containernn .swiper-slide .content h3{margin-bottom:5px;margin-top:10px}.reelss .swiper-containernn-recent .swiper-slide .content h3{margin-bottom:5px;margin-top:10px}.reelss .swiper-containernnm .swiper-slide .content h3{margin-bottom:5px;margin-top:10px}.reelss.thaja-varthalu .swiper-containernn{margin:0 0 20px;width:100%;padding:0 10px}.reelss.thaja-varthalu .swiper-containernn .content h3{width:100%}.reelss.thaja-varthalu .swiper-containernn-recent{margin:0 0 20px;width:100%;padding:0 10px}.reelss.thaja-varthalu .swiper-containernn-recent .content h3{width:100%}.reelss{width:100%;position:relative;margin:10px auto;background:#fff;overflow:hidden}.swiper-slide.loco_cat__carousel_slide.swiper-slide-active h3{font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:15px;line-height:20px;color:#f00201}.swiper-slide.loco_cat__carousel_slide h3{font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:15px;line-height:20px;color:#333}.press-release{background:#fff;width:100%}.press-release .content-flex img{border-radius:5px}.press-release .heding h2{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:24px;line-height:33px;text-transform:uppercase;padding:15px 10px 0!important;color:#f00201}.press-release h4{font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:27px;color:#000}.press-release.andhra-pradesh .content-padding{padding:10px 20px}.press-release.andhra-pradesh .content-padding p{height:50px;display:flex;align-items:center}.press-release p{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:16px;line-height:22px;color:#000}.entertainment-telugu .live-ads{width:100%;position:relative;margin:2px auto;display:flex;align-items:center;padding:0;justify-content:center}.press-release .andhra-content .heding hr{border-top:2px solid #545454;text-align:center;display:flex;margin:10px auto 10px;width:50%}.press-release .content-flex hr{opacity:.2;width:100%}.press-release .content-flex .content-padding hr{margin-top:7px;margin-bottom:7px}.press-release .content-flex .heding hr{opacity:.5;width:100%;left:0;position:relative;margin-top:0;margin-bottom:20px}.press-release .content-flex{width:100%;max-width:295px;flex-direction:column;margin:0 auto}.press-release .andhra-pradesh .content-flex p{padding-left:5px;padding-top:10px}.reelss .container{max-width:1280px;margin:0 auto;height:100%}.reelss .swiper-containern{width:100%;height:100%}.reelss .swiper-containernr{width:100%;height:100%}.reelss .swiper-slide{text-align:center;font-size:18px;background:#fff;display:-webkit-box;display:-ms-flexbox;display:-webkit-flex;display:flex;-webkit-box-pack:center;-ms-flex-pack:center;-webkit-justify-content:center;justify-content:end;-webkit-box-align:center;-ms-flex-align:center;-webkit-align-items:center;align-items:center}.reelss .swiper-containern{width:100%;overflow:hidden;margin:10px 0 20px}.reelss .swiper-containernr{width:100%;overflow:hidden;margin:20px 0}.reelss .swiper-containerns{width:87vw;overflow:hidden;margin:20px auto}.reelss .loco_cat.loco_section.svg-width .swiper-slide .svg--position{margin:0 0}.reelss .swiper-containernn{width:100%;overflow:hidden;margin:0 1px}.reelss .swiper-containernn-recent{width:100%;overflow:hidden;margin:0 1px}.reelss .swiper-containernnm{width:100%;overflow:hidden;margin:0 1px}.reelss .swiper-slide{background-size:cover;background-position:50%;display:flex;align-items:center;justify-content:center;flex-direction:column}.footer-section{background:#fff;position:relative;padding:10px 0 0}.footer-section .row{display:flex;margin:0 auto;justify-content:center;align-items:start}.photo-grid{display:flex;flex-wrap:wrap;align-items:center;margin:0 auto}.photo-grid li{width:60px;margin:0 8px 0 0}.footer-cta{border-bottom:1px solid #373636}.single-cta i{color:#ff5e14;font-size:30px;float:left;margin-top:8px}.cta-text{padding-left:15px;display:inline-block}.cta-text h4{color:#fff;font-size:20px;font-weight:600;margin-bottom:2px}.cta-text span{color:#757575;font-size:15px}.footer-content{position:relative;z-index:2}.footer-pattern img{position:absolute;top:0;left:0;height:330px;background-size:cover;background-position:100% 100%}.footer-logo{display:flex;align-items:center;margin:0 auto;justify-content:center;padding:20px 0}.footer-logo img{max-width:200px}.footer-text p{margin-bottom:14px;font-size:14px;color:#7e7e7e;line-height:28px}.footer-social-icon span{color:#fff;display:block;font-size:20px;font-weight:700;font-family:Roboto,sans-serif;margin-bottom:20px}.footer-social-icon a{color:#fff;font-size:16px;margin-right:15px}.footer-social-icon i{height:40px;width:40px;text-align:center;line-height:38px;border-radius:50%}.facebook-bg{background:#3b5998}.twitter-bg{background:#55acee}.google-bg{background:#dd4b39}.footer-widget-heading h3{font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:24px;line-height:200.68%;color:#000;margin-bottom:5px;position:relative;margin-top:0}.copyright-text.download img{width:55%}.footer-ul{display:flex;align-items:center;justify-content:start;width:100%;margin:0 auto;max-width:1000px;padding-bottom:10px}.copyright-text.download{width:60%;display:flex;align-items:center}.footer-menu{width:40%;display:flex;align-items:center}.footer-menu h3{width:65%;margin:0;text-transform:capitalize;font-size:20px}.footer-widget{max-width:230px;display:flex}.footer-menu .list-inline a{margin:5px 4px}.copyright-area .footer-menu{width:100%;display:flex;align-items:center}.container-footer{width:100%;display:block;margin:0 40px}.footer-widget ul li{margin-bottom:5px;padding:0}.footer-menu ul{margin-bottom:0;display:flex;align-items:start;justify-content:start;max-width:calc(100% - 0px)}.text-lg-left{width:50%}.d-lg-block.text-right{width:50%}.footer-widget ul li a:hover{color:#ff5e14}.footer-widget ul li a{color:#000!important;text-transform:capitalize;font-size:18px;font-family:Roboto,sans-serif}.subscribe-form{position:relative;overflow:hidden}.subscribe-form input{width:100%;padding:14px 28px;background:#2e2e2e;border:1px solid #2e2e2e;color:#fff}.subscribe-form button{position:absolute;right:0;background:#ff5e14;padding:13px 20px;border:1px solid #ff5e14;top:0}.subscribe-form button i{color:#fff;font-size:22px;transform:rotate(-6deg)}.copyright-area{background:#000;padding:10px 0}.copyright-text.download p{margin:0 20px;font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:25px;text-align:left;text-transform:uppercase;color:#000}.copyright-text p{margin:0;font-size:14px;color:#fff}.copyright-area .copyright-text p{color:#fff}.copyright-text p a{color:#ff5e14}.footer-menu li{display:inline-block;padding:0 10px}.footer-menu li:hover a{color:#ff5e14}.footer-menu li a{font-size:14px;color:#fff}.swiper-button-next,.swiper-button-prev{right:10px;left:auto;background:#fff!important;border-radius:50%;width:45px!important;height:45px!important}.swiper-button-prev{left:10px!important;right:auto}.swiper-button-next{right:10px!important;left:auto}.swiper-button-next,.swiper-button-prev{position:absolute;top:50%;width:40px;height:40px;margin-top:calc(-1 * var(--swiper-navigation-size)/ 2);z-index:10;cursor:pointer;display:flex;align-items:center;justify-content:center;color:#f21d16!important;background:#fff!important}.swiper-button-next:after,.swiper-button-prev:after{font-family:swiper-icons;font-size:25px!important}.reelss.russiaukraine{background:linear-gradient(180deg,#ff4040 0,#430e0e 151.7%);padding:10px}.reelss.russiaukraine .swiper-containernn .swiper-slide.swiper-slide-active h3{color:#fff;text-align:left}.reelss.russiaukraine .swiper-containernn-recent .swiper-slide.swiper-slide-active h3{color:#fff;text-align:left}.reelss.russiaukraine .swiper-containernn .swiper-slide h3{color:#fff;text-align:left}.reelss.russiaukraine .swiper-containernn-recent .swiper-slide h3{color:#fff;text-align:left}.reelss.russiaukraine .swiper-slide{background:0 0}.reelss.russiaukraine .heding h2{color:#fff;padding:15px 0 5px!important;font-size:22px}.reelss.russiaukraine .heding hr{border:0;border-top:2px solid #000!important;width:60%;margin:0 0 15px}.reelss.russiaukraine .heding hr{border-top:2px solid #fff}.row{display:flex;align-items:center;justify-content:center}.reelss .loco_cat.loco_section .col-md-2 a img{padding-right:10px}.reelss .loco_cat.loco_section .col-md-2 a{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:16px;line-height:25px;color:#000;display:flex;align-items:center;justify-content:center;margin:15px 0 0 20px}.reelss.russiaukraine .flex-list{display:flex;background:#8d2222;margin-top:10px;overflow:auto;width:100%}.reelss.russiaukraine .flex-list li a{font-size:15px;color:#fff;padding:0 12px}.reelss.russiaukraine .flex-list li a:hover{text-decoration:none}.emoji{width:60px;position:relative;top:5px}section.bell{width:400px;height:80px;text-align:center;display:flex;align-items:center;justify-content:center;margin:0 auto}.section.bell{text-align:left;margin-left:20px;font-size:15px;display:block;transform:translate(0,5px)}.bell div{width:100%;margin:0 0 0 20px;height:30px;background-color:red}.bell .ico{width:40px;float:left;margin:-2px -15px}.bell .div{color:snow;font-size:20px;display:inline-block}.politics-flex p{font-size:14px}.politics-flex span{font-size:12px}.content-flex p{margin:0;font-family:Roboto,sans-serif;font-style:normal;font-weight:100;font-size:16px;line-height:25px;width:225px;height:auto;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;text-overflow:ellipsis}.entertainment-telugu h2{font-size:22px}.heding h2{font-size:20px;margin:0}.press-release .heding h2{font-size:20px;text-align:center}.press-release h4{font-size:16px}.custom-select{position:relative;margin-top:10px;margin-right:10px}.custom-select select{display:none}.select-selected{background-color:#fff;border:1px solid #f3f3f3!important;border-radius:5px;color:#000!important;width:100%}.andhra-content.andhra-district .select-distict-icon{display:flex;justify-content:space-between;align-items:center;margin:0 auto;width:100%}.andhra-district .andhra-pradesh .five-cols .content-flex p{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:12px;line-height:16px;color:#000}.andhra-pradesh .politics-business.five-cols hr{margin-top:5px;margin-bottom:5px}.select-selected:after{position:absolute;content:"";top:calc(100% - 17px);right:5px;width:0;height:0;border:6px solid transparent;border-color:#f21d16 transparent transparent transparent}.select-selected.select-arrow-active:after{border-color:transparent transparent #f21d16 transparent;top:5px}.select-items div,.select-selected{color:#000;padding:4px 20px 4px 7px;border:1px solid #f3f3f3;cursor:pointer;user-select:none}.select-items{position:absolute;background-color:#fff;top:100%;left:0;right:0;z-index:99}.select-hide{display:none}.same-as-selected,.select-items div:hover{background-color:rgba(0,0,0,.1)}.tabs-all .btn{padding:0 5px 0 5px;font-family:Roboto,sans-serif;line-height:28px}.tabs-all .btn a{color:#333}.political-news .content-flex{width:68%;display:flex;flex-direction:column;margin-right:10px;padding:10px}.political-news .entertainment-telugu .entertainment-flex{height:auto;overflow:hidden}.political-news .entertainment-flex{height:auto;overflow:auto}.political-news h2{font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:30px;line-height:44px;margin:0;color:#000}.political-news span{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:14px;line-height:27px;color:#77787b}.live-tabs.photo-gallery .tab-content .content-flex img{margin:0}.political-news p{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:18px;line-height:27px;text-align:justify;color:#000;margin-top:20px;width:auto;display:block;height:auto}.political-news .share{display:flex;align-items:center;justify-content:start;margin:10px 0}.political-news .share .list-inline{margin-left:10px;width:auto}.political-news .tag{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:14px;line-height:19px;color:grey}.follow{border:1px solid #bcbcbc;height:80px;display:flex;align-items:center;justify-content:center;margin:0 auto;width:100%;flex-direction:column;margin:10px 0}.follow p{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:15px;line-height:106.68%;text-align:center;margin:10px 0;color:#000}.follow-red{border:1px solid #f00201;margin-top:15px}.follow-red span.red{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:16px;text-align:justify;color:#f00201}.follow-red p{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:14px;color:#000;text-align:center;padding:5px;margin:0}.tags{font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:16px;line-height:25px;color:#000}.tags span{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:15px;line-height:25px;color:#f00201}.slider-tags{position:relative}.slider-tags .swiper-containernn{overflow:hidden}.slider-tags .swiper-containernn-recent{overflow:hidden}.slider-tags .swiper-containernnn{overflow:hidden}.slider-tags .swiper-containernnn .swiper-slide img{width:100%}.slider-tags .swiper-containernnn .swiper-button-prev{background:#fff!important}.slider-tags .swiper-containernnn .swiper-button-next{background:#fff!important}.slider-tags .svg--position p{background:#fff;border:1px solid #d6d6d6;font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:16px;line-height:22px;color:#f00201;padding:5px 40px}.slider-tags .swiper-button-prev{top:60%;left:0!important;right:auto;background:#fff0!important}.slider-tags .swiper-button-next{top:60%;left:auto;right:0!important;background:#fff0!important}.entertainment-telugu.trending h2{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:24px;line-height:33px;text-transform:uppercase;color:#fff;text-align:left}.entertainment-telugu.trending .share-content p{font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:15px;line-height:19px;color:#000;text-align:left;padding:0;margin:0 10px;display:-webkit-box}.entertainment-telugu.trending hr{margin-top:5px;margin-bottom:10px;border:0;border-top:2px solid #eee}.entertainment-telugu.trending .entertainment-scroll{display:flex;align-items:center;justify-content:start;line-height:22px;padding:0 0;margin:15px auto}.entertainment-telugu.trending .share-content svg{margin:0 10px 0}.entertainment-telugu.trending .share-content span{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:12px;line-height:174.08%;color:#666;margin:0 10px 0}.entertainment-telugu.trending .news-latest .share-content p{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:16px;line-height:22px;color:#000;padding:0 2px;margin:0 5px}.entertainment-telugu.trending .entertainment-flex.news-latest .entertainment-scroll{padding:0}.related{display:flex;width:100%;position:relative;margin:15px auto;overflow:hidden}.related .articles{background:#fff;display:flex;width:70%}.related .live-ads{margin:0;width:30%;padding:0 6px;align-items:start}.related #features{bottom:0;right:0;width:500px;height:auto}.related #features img{width:100%;height:auto;display:flex;align-items:center;justify-content:center;margin:0 auto}.related .view-all{position:relative;bottom:0;right:0}.related .andhra-content .heding h2{padding:0 10px 10px!important}.related .andhra-pradesh .district{display:flex;width:100%;padding:5px}.articles .heding h2{color:#000}.articles .andhra-district .andhra-pradesh .district .content-flex{display:block}.articles .andhra-district .andhra-pradesh .content-flex .Astrology{display:flex}.articles .andhra-district .andhra-pradesh .district .content-flex h3{margin-top:0;margin-bottom:10px;font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:16px;line-height:25px;text-transform:uppercase;color:#f00201}.articles .andhra-district .andhra-pradesh .content-flex p{padding-left:5px;font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:14px;line-height:19px;color:#000}.articles .andhra-district .andhra-pradesh .content-flex span{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:12px;line-height:174.08%;color:#666}.articles .andhra-pradesh .district .politics-business .politics{width:35%}.related .andhra-pradesh .politics-business hr{width:100%;margin-left:0}.entertainment-sec .andhra-pradesh .politics-business .politics-flex{width:100%;display:flex;margin:5px auto;position:relative}.entertainment-sec .andhra-pradesh .politics-business .politics-flex svg{position:absolute;top:15px;right:0}.related.entertainment-sec .entertainment-bg .andhra-pradesh .district{display:flex;width:100%;padding:20px 5px;margin:0 auto;justify-content:center}.related.entertainment-sec .district .politics-business{width:49%!important;margin:0 auto}.entertainment-sec .andhra-pradesh .district .content-flex{display:block;margin-bottom:20px}.entertainment-bg h2{margin:0;background:#f00201;text-align:center;font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:24px;line-height:33px;text-align:center;color:#fff;padding:5px 0}.sub-flex ul{display:flex}.sub-flex ul li{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:20px;line-height:33px;text-align:center;color:#000;padding-right:5px;display:flex;align-items:center}.sub-flex ul li span{color:#f00201}.social-icons .share{display:flex;margin-bottom:10px}.social-icons .share .list-inline{margin-left:0;max-width:none}.social-icons .list-inline a{margin:5px 1px}.social-icons .share b{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:20px;line-height:33px;color:#000}.related .entertainment-bg .andhra-pradesh .district{display:flex;width:100%;padding:20px 5px}.entertainment-sec .entertainment-bg .andhra-pradesh .district .content-flex{display:flex;flex-direction:column;margin:0 auto;justify-content:left;align-items:start}.related.entertainment-sec .entertainment-bg{width:67%;margin-right:10px}.related.entertainment-sec .social-icons{width:30%}.related.entertainment-sec .entertainment-scroll{padding:0 5px;margin:0 auto;width:100%;justify-content:start;align-items:center;display:flex}.photo-gallery .related.entertainment-sec .entertainment-scroll{padding:5px 5px}.reviews .photo-gallery .related.entertainment-sec .entertainment-scroll:hover{background:#666}.reviews .photo-gallery .related.entertainment-sec .news-latest .entertainment-scroll:hover{background:#f3f3f3}.reviews .photo-gallery .related.entertainment-sec .news-latest .entertainment-scroll:hover .share-content p{color:#f00201}.reviews .photo-gallery .related.entertainment-sec .entertainment-scroll:hover .share-content h3{color:#fff;font-size:30px}.reviews .photo-gallery .related.entertainment-sec .entertainment-scroll:hover .share-content span{color:#fff}.reviews .photo-gallery .related.entertainment-sec .entertainment-scroll:hover .share-content p{color:#fff}.related.entertainment-sec .entertainment-scroll .share-content p{margin:0;padding:0;width:auto;height:auto;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;text-overflow:ellipsis;font-size:15px;line-height:25px;font-weight:600}.related.entertainment-sec .entertainment-scroll img{width:auto;height:auto}.entertainment-flex.news-latest .entertainment-scroll img{width:75px;height:45px}.related.entertainment-sec .entertainment-flex.news-latest .entertainment-scroll{margin:10px auto 0}.related.entertainment-sec .entertainment-flex.news-latest hr{width:100%;margin-top:5px;margin-bottom:5px}.related.entertainment-sec .entertainment-scroll .share-content{width:100%;margin-left:10px}.related.entertainment-sec .entertainment-scroll .share-content a:hover{text-decoration:none;color:#fff}.related.entertainment-sec .social-icons .related-posts{background:#fff;padding-bottom:20px}.related-posts hr{width:65%;margin-left:0}.related-posts.movie-review .news-latest hr{width:100%;margin-left:0}.related-posts h2{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:24px;line-height:33px;text-transform:uppercase;color:#f00201}.social-icons .related-posts hr{width:100%;margin-left:0}.related-posts p{font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:14px;line-height:19px;color:#000;width:100%;padding:10px 0 0}.related-posts svg{margin:0 10px 0}.related-posts span{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:12px;line-height:174.08%;color:#666;margin:0 10px 0}.most-read h2{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:22px;line-height:40px;text-align:left;text-transform:uppercase;color:#fff;background:#f00201;margin:0;padding:0 10px}.social-icons .live-ads{margin:0;width:100%;padding:0 0;align-items:start}.pagination{display:flex;float:right}.pagination a{color:#000;float:left;padding:8px 16px;text-decoration:none;transition:background-color .3s;border:0 solid #ddd;background:#f00201;color:#fff;margin-left:10px}.pagination a.active{background-color:#4caf50;color:#fff;border:1px solid #4caf50}.about-section{padding:20px}.about-section p{font-family:Roboto;font-style:normal;font-weight:400;font-size:18px;line-height:27px;text-align:justify;color:#000}#ads3{display:flex;align-items:center;justify-content:center;margin:0 auto}.back-button{font-family:Roboto,sans-serif;font-style:normal;font-weight:600;font-size:16px;line-height:15px;text-align:center;color:#fff;display:flex;align-items:center;justify-content:center;margin:0 auto;background:#f00201;padding:10px}.contact-section{display:flex;align-items:center;justify-content:center;margin:0 auto;width:100%;background:#ebebeb}.form-container{width:80%;margin:45px auto 0}.contact.andhra-content{padding:0 0 0;background:#ebebeb}.contact-section .form-container .form-control{height:50px}.contact-section .submit{width:100%;border-radius:0;text-align:center;align-items:center;justify-content:center;height:40px;display:flex;margin:0 auto;background:linear-gradient(180deg,#f00201 0,#850000 100%);box-shadow:4px 4px 25px rgb(0 0 0 / 25%);border:0}.live-tabs.photo-gallery .nav-tabs li{border:2px solid #000;width:100px;height:40px;font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:16px;line-height:22px;color:#000}.live-tabs.photo-gallery .nav-tabs li.tab.is-active{color:#fff}.live-tabs.photo-gallery .tab-panel.is-active{display:flex;width:100%;align-items:center;flex-wrap:wrap;margin:0 auto;justify-content:end}.live-tabs.photo-gallery .andhra-district .andhra-pradesh .content-flex{width:100%;display:flex;flex-direction:column;max-width:180px;margin:0 auto}.live-tabs.photo-gallery .andhra-content{padding:0 0 0}.live-tabs.photo-gallery ul.pagination-items{list-style:none;float:right;margin:20px 5px}.live-tabs.photo-gallery .card-text-content:hover{background:#333333a8;position:absolute;top:0;margin:0;height:100%;width:100%;display:flex;align-items:end;justify-content:center}.live-tabs.photo-gallery .content-flex:hover .card-text-content{height:100%;background:#333333a8}.live-tabs.photo-gallery .content-flex:hover h3{position:absolute;bottom:0;margin:0;height:100%;width:100%;display:flex;align-items:center;justify-content:center;height:90px;color:#fff;background-color:rgba(255,0,0,.6)}.live-tabs.photo-gallery .card-text-content h3 a{color:#fff}.live-tabs.photo-gallery .card-text-content h3{font-size:20px;margin:0;text-align:center;position:absolute;bottom:0;margin:0;height:100%;width:100%;display:flex;align-items:center;justify-content:center;height:90px;color:#fff;background-color:rgba(255,0,0,.6)}.latest .andhra-content{background:#fff0}.latest .andhra-pradesh{background:#fff0}.latest .political-news .content-flex{background:#fff;width:66%;margin-right:20px}.latest .slider-tags .svg--position p{padding:5px 35px;text-align:left;width:100%;margin-top:30px;margin-bottom:10px}.latest .entertainment-telugu.trending .entertainment-scroll{margin:12px auto;padding:10px}.review h2{margin:0;background:#f00201;text-align:center;font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:24px;line-height:33px;text-align:center;color:#fff;padding:5px 0}.share-content h3{font-family:Roboto,sans-serif;font-style:normal;font-weight:800;font-size:36px;line-height:49px;margin:0;padding:0;color:#fff}.reviews .andhra-pradesh{background:#666}.reviews .entertainment-scroll.one{background:#666}.reviews .entertainment-scroll{background:#fff;border:0 solid #bcbcbc;padding:20px}.share-content span{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:12px;line-height:174.08%;color:#666}.share-content p{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:14px;line-height:19px;color:#000}.share-content:hover p{color:#f00201}.reviews .share-content .back-button{background:linear-gradient(180deg,#f00201 0,#850000 100%);border:1px solid rgba(102,102,102,.53);box-shadow:1px 1px 13px rgb(0 0 0 / 25%);display:flex;align-items:center;justify-content:center;margin:0 auto 10px;width:35%;float:left;line-height:10px}.carousel-control-prev,.political-news .carousel-control-next{width:auto}.political-news .carousel-control-next-icon{background-image:url(/theme_teal/images/arrow-right.svg)!important;background-color:#fff;padding:12px;opacity:1;top:50%}.political-news .carousel-control-prev-icon{background-image:url(/theme_teal/images/arrow-left.svg)!important;background-color:#fff;padding:12px;opacity:1;top:50%;opacity:1}.political-news .carousel-control-next,.political-news .carousel-control-prev{top:50%;opacity:1}.political-news #carousel{display:flex;align-items:center;justify-content:center;width:100%}.reviews .share-content{margin-left:15px}.reelss .loco_cat.loco_section .swiper-slide:hover .shadow-vector{position:relative;display:flex;bottom:60px;background:0 0;width:100%}.reelss .loco_cat.loco_section .swiper-slide .shadow-vector img{display:none}.reelss .loco_cat.loco_section .swiper-slide:hover .shadow-vector img{width:25%;border:0 solid #d6d6d6;display:flex;align-items:center;justify-content:space-between;margin:0 auto 58%}.reviews .entertainment-scroll.one .share-content span{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:16px;line-height:31px;color:#fff}.reviews .entertainment-scroll.one .share-content p{font-weight:500;font-size:16px;line-height:31px;color:#cdcdcd;margin:0;padding:5px 0}.reviews .entertainment-scroll.one .entertainment-scroll{padding:20px}.reviews .entertainment-scroll.one .share-content h3{color:#fff;font-size:30px}.reviews .entertainment-scroll .share-content p{color:#595959;padding:5px 0;margin:0}.reviews .movie-review .entertainment-scroll .share-content p{margin:0 10px 0}.reviews .entertainment-scroll .share-content span{color:#000;font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:16px;line-height:31px}.reviews .entertainment-scroll .share-content h3{color:#000;font-size:30px}.movie-review .entertainment-scroll .share-content span{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:12px;line-height:174.08%;color:#666}.reviews .movie-review .entertainment-scroll{background:#fff;border:0 solid #bcbcbc;padding:0}.reviews .movie-review .share-content{margin-left:0}.constent-review .share{display:flex;justify-content:center;align-items:center}.related.entertainment-sec .entertainment-scroll .share-content .share .list-inline{padding-left:0;justify-content:start}.constent-review .list-inline{padding-left:10px;justify-content:start}.constent-review .about-section.reviews h3{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:20px;line-height:27px;color:#f00201}.constent-review .about-section.reviews p{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:16px;line-height:22px;text-align:justify;color:#000}.indrani-slider .reviews .share-content{margin-left:15px;position:relative;width:100%;display:grid}.indrani-slider .ads-slider{padding:5px 10px;position:relative;width:100%;overflow:hidden}.indrani-slider .reviews .entertainment-scroll{background:#fff;border:0 solid #bcbcbc;padding:0;margin:0 auto 15px}.indrani-slider .card .img-wrapper{padding:5px}.indrani-slider .card .img-wrapper p{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:9px;line-height:12px;text-align:center;color:#000}.indrani-slider .swiper-button-prev:after{font-family:swiper-icons;font-size:15px!important}.indrani-slider .swiper-button-prev{left:-10px!important;right:auto;color:#f21d16!important;background:#fff0!important;width:30px!important;height:30px!important}.indrani-slider .swiper-button-next:after{font-family:swiper-icons;font-size:15px!important}.indrani-slider .swiper-button-next{right:-10px!important;left:auto;color:#f21d16!important;background:#fff0!important;width:30px!important;height:30px!important}.navbar-row .navbar-right img{display:block;max-width:calc(100% - 0px);height:90px}.ads-slider .card-text-content h3{font-size:20px;text-align:center;font-family:Roboto,sans-serif;font-weight:400;width:252px;height:auto;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;text-overflow:ellipsis}.andhra-content .heding.news-heding.mobile h2{display:none}.andhra-content .heding.news-heding.mobile hr{display:none}@media only screen and (max-width:767px) and (min-width:320px){.pagination{display:flex;float:right;position:absolute;bottom:0;right:0;margin:0}.live-tabs .top-news .tabs-wrapper .nav-tabs{display:flex;border-bottom:0 solid #ddd;align-items:start;justify-content:center;margin:0 auto;width:90%}.press-release h4{font-size:14px}.reelss.video-stories .heding h2{padding:15px 0 5px!important}.reelss.recently-viewed .heding h2{padding:15px 0 5px!important}.ott-bg{margin:0 0}.reelss-ul{display:flex;align-items:center;width:95%;justify-content:space-between;margin:10px auto}.andhra-district .andhra-pradesh .district-min{width:100%}.andhra-pradesh .district .politics-business{margin-left:0}.constent-review .list-inline{padding-left:10px;justify-content:start;display:flex}.political-news .share .list-inline{display:flex}.reelss .loco_cat.loco_section .swiper-slide h4{width:100%}.latest-news-entertainment.indrani-scroll .entertainment-telugu .entertainment-flex{height:auto;overflow:hidden;margin:0}.ott .andhra-pradesh .politics-business{position:relative;width:100%;top:0;margin-bottom:20px}.politics-business.ott-bg{padding:10px}.latest .political-news .content-flex{width:100%}.tab-content .content-flex hr{margin-left:0;width:40%}.political-news .content-flex{width:100%}.photo-gallery img{width:auto}.list-inline{max-width:none}.reelss.thaja-varthalu{padding:0 10px;display:none}.andhra-content.office{padding:0 0;display:block}.reelss.video-stories .reelss-ul a{display:none}.footer-menu{display:block;width:100%}.footer-menu h3{width:100%;text-align:center;font-size:20px;margin:0}.list-inline a .fa-2x{font-size:15px;width:22px;height:22px}.copyright-text.download p{font-size:13px;margin:0 5px}.copyright-text.download{width:100%;display:block;text-align:center}.reelss-ul img{padding-right:10px;width:30%}.entertainment-telugu h2{font-size:16px;padding:5px;margin-bottom:10px}.profile{margin-top:30px}.profile p{font-size:18px;line-height:25px;text-align:center}.tupaki-heding{display:block}.telugu{font-size:18px;width:100px;height:31px;position:absolute;top:93px}.navbar-right .side-svg{top:5px;right:0;cursor:pointer;position:absolute}.navbar-default .navbar-toggle{border-color:#ddd;display:none}form{display:none}header .navbar .navbar-nav{width:100%;justify-content:start}header .navbar-default .navbar-nav>li{border-right:0}header .navbar-default .navbar-nav>li>a{padding:20px 0;font-size:14px}header .navbar-default .topbar ul{padding:0;display:block}header .navbar-default .topbar ul li{display:flex;text-align:center;padding:0 10px 0 5px;border-bottom:0 solid #a4a4a4}.tab-content .content-flex h1:after{content:"";width:120px;height:2px;background:#f00201;position:absolute;bottom:0;left:0}header .navbar-default .topbar ul li:after{content:" "}header .navbar-default .topbar .pull-right{margin-top:-24px}header .navbar-default .topbar{padding:0 0;position:relative}header .second_menu{display:none}header button.btn-primary{display:none}.collapse{display:block}header .navbar-fixed-bottom .navbar-collapse,header .navbar-fixed-top .navbar-collapse{max-height:none;padding:0;display:block}header .navbar-header{text-align:center}header .navbar-toggle{float:none;border:0;margin-right:0}header .toggle-products{font-size:16px;color:#fff;text-transform:uppercase;line-height:0}header .navbar-default .navbar-toggle:focus,header .navbar-default .navbar-toggle:hover{background:0 0}header .mobile_search .form-control{border-radius:0;border:0;height:35px}header .mobile_search button.btn-primary{background-color:#58585a;border-color:#58585a;border:0;text-transform:uppercase;border-radius:0;padding:7px}.topbar .row{display:flex;width:100%;position:relative;margin:0}.tabbar-fluid{width:100%}#search{border:0;width:90%;position:absolute;top:5px;display:flex;float:right;left:45px}.tabs-all-ul{width:100%;overflow:auto;white-space:nowrap}.telugu{font-size:14px;height:20px;position:absolute;top:12px;left:3%;width:60px;display:flex;align-items:center;justify-content:center}.swiper-container{width:100%;padding-top:0;padding-bottom:50px}.navbar-right{margin-right:0;margin-top:0;justify-content:space-between;width:100%}.side-svg svg{color:#f00201;font-size:20px!important;padding:8px 0}.dropdown-container{overflow:auto;height:auto;margin-bottom:30px}.sidenav{right:0;top:50px;padding-top:0;z-index:9;overflow-x:hidden;height:100%}.accordion{display:block}.tab-content .content-flex h1{display:none}}@media only screen and (max-width:768px) and (min-width:320px){.list-inline{max-width:none}.live-tabs.photo-gallery .andhra-district .andhra-pradesh .content-flex{max-width:130px;margin:0 auto}.navbar-default .navbar-toggle{display:none}header .navbar .navbar-collapse{display:block}.navbar-default .navbar-form{border-color:#e7e7e700}.list-inline a{margin:5px 3px}.navbar-form{padding:10px 15px}header .navbar-default .topbar ul{overflow:auto;display:flex;justify-content:start}.tab-panel.is-active{display:block}.content-flex{width:100%}.politics-business{width:100%;top:0;padding:0}.latest-news-entertainment.indrani-scroll .entertainment-telugu.spacing{justify-content:start;height:950px}.view-all{bottom:-3px}.latest-news-entertainment{display:block}.entertainment-telugu{width:100%;height:auto}.entertainment-telugu.spacing a{display:flex;align-items:center;justify-content:center;margin:10px auto;width:10%}.entertainment-telugu.spacing{margin:0 0}.tabs-all-ul{display:flex;width:100%;overflow:auto;white-space:nowrap;background:#f00201}.tabs-all-ul::-webkit-scrollbar{width:5px;height:0;display:block}.tabs-all .btn{color:#fff}.tabs-all .active{color:#000}.tabs-all{margin:0 0}.tupaki-heding{display:block}.loco_cat.loco_section .container{width:100%}.reelss.russiaukraine .flex-list{width:100%;display:flex;overflow:auto;margin:0 auto;white-space:nowrap}.andhra-pradesh{display:block}.andhra-district .andhra-pradesh .content-flex{width:100%}.andhra-pradesh .district{display:flex;width:100%}.district .politics-business{width:100%!important;margin-left:10px}.andhra-district .andhra-pradesh .district .content-flex{width:100%;display:flex;margin:0;max-width:none}.district .politics-business.five-cols{width:75%!important}.andhra-pradesh .politics-business .politics-flex{width:100%}.andhra-content.office .andhra-pradesh .politics-business{width:100%}section.bell{width:300px}.bell .div{font-size:16px}#ads3{width:100%}}@media only screen and (min-width:768px) and (max-width:959px){.live-tabs.photo-gallery .andhra-district .andhra-pradesh .content-flex{max-width:130px;margin:0 auto}header .navbar-default .topbar a{font-size:12px}header .navbar-default .navbar-nav>li>a{font-size:14px;color:#fff;text-transform:uppercase;line-height:0;padding:10px 10px;line-height:0}header .collapse.in{display:block!important}header .navbar .navbar-nav{display:block;float:none;vertical-align:top}header .navbar .navbar-collapse{text-align:center}header .navbar-header{text-align:center}header .navbar-right button{padding:5px 20px;margin:0;font-size:20px;float:right}header .navbar-brand>img{height:auto}header .navbar-toggle{float:none;border:0}.navbar-default .navbar-toggle:hover,header .navbar-default .navbar-toggle:focus{background:0 0}header .navbar-default .navbar-toggle .icon-bar{background-color:#fff}header .input-group-btn button{padding:13px 20px}.navbar-fixed-top .navbar-collapse,header .navbar-fixed-bottom .navbar-collapse{max-height:none;padding:0}}@media only screen and (min-width:960px) and (max-width:1199px){.list-inline{max-width:calc(100% - 4px)}header .navbar-default .topbar a{font-size:12px}header .navbar-default .navbar-nav>li>a{font-size:16px;color:#fff;text-transform:uppercase;line-height:2;padding:0 8px}header .collapse.in{display:grid;width:100%;overflow:auto}header .navbar .navbar-nav{display:flex;float:none;vertical-align:top;justify-content:start}header .navbar .navbar-collapse{text-align:center}header .navbar-header{text-align:center}header .navbar-right button{padding:0 20px;margin:0;font-size:15px;float:right}.content-flex p{font-size:14px}header .navbar-brand>img{height:auto}header .navbar-toggle{float:none;border:0}.navbar-default .navbar-toggle:hover,header .navbar-default .navbar-toggle:focus{background:0 0}header .navbar-default .navbar-toggle .icon-bar{background-color:#fff}header .input-group-btn button{padding:13px 20px}header .navbar-fixed-bottom .navbar-collapse,header .navbar-fixed-top .navbar-collapse{max-height:none;padding:0}.navbar-right{margin-right:0}.live-ads{padding:0 0}.live-tabs{width:75%}.tabs-all .box{max-width:250px}.tupaki-heding .heding{width:10%}.flex-list{width:83%}.reelss.russiaukraine .flex-list li a{padding:0 5px}.andhra-district .andhra-pradesh .content-flex{width:35%}.andhra-pradesh .district{width:65%}.andhra-pradesh .district .politics-business .politics{width:55%}.press-release .content-flex{max-width:250px}}@media screen and (max-width:767px){.politics-business .content-flex .politics-flex{margin-left:10px;width:80%}.indrani h3{text-align:center;margin-bottom:0}.latest-news-entertainment .entertainment-telugu.spacing .indrani hr{width:20%;margin-top:0;margin-bottom:15px;border-top:2px solid #f00201;display:block}.indrani-scroll{display:inline-block;align-items:center;justify-content:center;margin:0 auto;width:100%}.latest-news-entertainment .entertainment-telugu.spacing .indrani .indrani-scroll hr{display:none}.live-tabs a.aads{display:block}.reelss .loco_cat.loco_section .swiper-slide{margin:0 0 0 2px}.reelss.video-stories.video-icon-btn .loco_cat.loco_section .swiper-slide{margin:0;align-items:start}.related.entertainment-sec .entertainment-scroll .share-content .share .list-inline{display:flex}.andhra-content.office img{width:100%;height:auto}.andhra-content.office .heding h2{padding:10px 0 0 0!important}.andhra-content.office .reelss-ul a{display:none}.andhra-content.office .politics-business .politics{width:auto}.andhra-content.ott .reelss-ul{width:100%}.andhra-content.office .politics-business .politics-flex{margin-left:0;width:auto}.reelss .swiper-containernr{margin:0 0 10px}.reelss.stories .swiper-button-next,.reelss.stories .swiper-button-prev{display:none}.reelss.stories .loco_cat.loco_section .swiper-slide:hover .shadow-svg{border:6px solid #d6d6d6;width:97%}.reelss .loco_cat.loco_section .swiper-slide:hover .shadow-vector{bottom:10px}.reelss.stories .loco_cat.loco_section .swiper-slide:hover h2{padding:0}.reelss.stories .loco_cat.loco_section .swiper-slide img{border:5px solid #d6d6d6}.reelss .swiper-containernn .swiper-slide h3{font-weight:100}.reelss .swiper-containernn-recent .swiper-slide h3{font-weight:100}.tabs-all .spacer{clear:both;height:10px}.tabs-all .box{max-width:none;width:100%;padding:0 10px 0}.andhra-content{margin:0 0}.ad-ons img{padding:11px;display:flex;align-items:center;justify-content:center;margin:0 auto}.indrani{height:160px}.live-tabs a{margin:8px 25px}.live-tabs .pagination a{margin:8px 10px;width:100%}.tabs-all .btn a{color:#fff;margin:8px 0}.andhra-district .andhra-pradesh .district-min p{font-weight:600}.reelss .swiper-button-next,.reelss .swiper-button-prev{display:none}.latest-news-entertainment hr{margin-top:0;margin-bottom:0}.latest-news-entertainment hr{margin-top:5px;margin-bottom:5px}.live-tabs a.carousel-control-prev{margin:8px 2px}.live-tabs a.carousel-control-next{margin:8px 2px}.entertainment-telugu.spacing a.movie-ads-run img{width:300px}.live-tabs a img{display:flex;align-items:center;justify-content:center;margin:0 auto;text-align:center;width:100%}::-webkit-scrollbar{width:5px;height:0;display:none}::-webkit-scrollbar-track-piece{background:#888}#parent .box .content-flex .politics img{width:100%;border-radius:5px}.reelss.russiaukraine .heding hr{margin:0 20px 5px;width:140%}.tabs-all-ul::-webkit-scrollbar{width:5px;height:0;display:block}.tabs-all-ul::-webkit-scrollbar-track-piece{background:#fff}}@media only screen and (max-width:767px){.reelss .swiper-containern{margin:0 2px 10px!important}.reelss .loco_cat.loco_section .swiper-slide:hover h2{font-size:12px;line-height:15px}.reelss hr{margin:0 0 10px}.reelss .swiper-button-next:after,.reelss .swiper-button-prev:after{font-family:swiper-icons;font-size:15px!important}.reelss .swiper-button-next,.reelss .swiper-button-prev{width:30px!important;height:30px!important}.ads-slider .swiper-button-next,.ads-slider .swiper-button-prev{display:none}.tabs-wrapper{padding:10px 0}.live-news .live:after{left:16px;display:block;border-top:14px solid transparent;border-bottom:14px solid transparent}.ads-slider{padding:0 0}.website-wrapper{padding:0 0}.ads-slider .card-text-content h3{font-size:13px}.live-tabs.photo-gallery .card-text-content h3{font-size:12px;height:60px}.andhra-content.andhra-district .tab-panel .card-text-content h3{height:50px}.topbar .container-fluid{padding:0}header .navbar-default .navbar-nav>li>a{padding:0 10px;font-size:16px}header .navbar-default .topbar a{font-size:14px}header .navbar-default .topbar-logo .navbar-row{display:block}header .navbar-default .topbar-logo .navbar-brand{padding:0;height:auto;width:100%;display:flex;align-items:center;justify-content:center}.ads-slider .swiper-container .card-text-content{height:45px}.navbar-row .navbar-right img{display:none;max-width:100%;height:auto}header .navbar-default .topbar-logo{background:#fff;padding:10px 0 10px}.navbar-brand>img{width:auto;height:25px}.video-gallery{display:block}.list-inline{display:none}.list-inline a{margin:5px 1px}header .navbar-header{text-align:right}.live-news .live{font-size:12px;padding:0 0 0 10px;width:150px;height:30px}.website-wrapper{flex-direction:column}.live-ads{width:100%;display:none;margin:0 auto 20px}.live-tabs .nav-tabs li{height:30px;font-size:13px}.latest-news-entertainment .entertainment-scroll{display:flex}.latest-news-entertainment .entertainment-scroll img{border-radius:5px}#features{height:auto}.marquee a{white-space:pre;font-size:12px}.marquee span .css-i6dzq1{width:20px}.live-tabs{width:100%}.marquee div{background:#f0020100}.live-news{background:#f00201;display:none}.tab-panel.is-active{display:block;padding:0 10px}.tab-panel.is-active .content-flex img{border-radius:5px;margin:0}.politics-flex h3{font-size:13px;line-height:17px}.latest-news-entertainment .entertainment-scroll p{font-size:15px;font-weight:600;padding:5px 0;margin:0 6px 0;height:55px}.latest-news-entertainment.indrani-scroll .entertainment-scroll p{margin:0 10px 0;display:flex;align-items:center;justify-content:center}.indrani .indrani-scroll .poll #carousel .carousel-control-prev{top:25px;opacity:1}.andhra-content.office .politics-business .content-flex{justify-content:start}.tabs-all .content-flex{justify-content:start}.reelss.russiaukraine .swiper-containernn .swiper-slide h3{width:auto}.reelss.russiaukraine .swiper-containernn-recent .swiper-slide h3{width:auto}.andhra-district .andhra-pradesh .district .politics-business.five-cols .content-flex p{display:block}#parent .politics-flex p{width:225px}.reelss.video-stories hr{margin:0 0 10px}.reelss.video-stories .swiper-containernnm .swiper-slide .content{margin-left:0}.politics-business .content-flex .politics-flex p{line-height:18px;font-size:15px;font-weight:600;padding:0 10px}.office .andhra-pradesh .content-flex p{width:auto}.office .politics-business hr{width:100%}.politics-business.top-news .content-flex .politics-flex p{padding:0 0}.politics-business .content-flex .politics-flex span{font-size:10px;display:none}.politics-business.ott-bg .content-flex .politics-flex span{font-size:10px;display:block}.content-flex{width:100%;display:flex;flex-direction:column}.politics-business{width:100%;top:5px;position:relative}.politics-business .content-flex{width:100%;display:flex}.politics-business .content-flex .politics img{width:100%;height:100%;border-radius:5px}.profile form{display:block;margin:0 auto}.entertainment-telugu.spacing .entertainment-scroll p{font-weight:400;font-size:18px;display:flex;align-items:center;justify-content:center;justify-content:left}.entertainment-telugu.spacing h2{margin:10px 0 0}.latest-news-entertainment{display:block}.entertainment-telugu{width:100%;margin:0 0;height:auto}.entertainment-telugu .entertainment-flex{height:auto;overflow:auto;margin-bottom:5px}.entertainment-telugu .view-all a{width:100%;font-size:13px;padding:0;line-height:initial;margin:10px 0}.content-flex .entertainment-content p{font-size:15px;padding-top:0;line-height:17px}.tab-content .content-flex .entertainment-content{padding:5px 0}.tab-content .content-flex .entertainment-content span{font-size:12px}.politics-business.top-news hr{margin-top:10px;margin-bottom:10px}.indrani-scroll .entertainment-telugu{height:auto}.reelss.russiaukraine .flex-list{display:flex;background:#8d2222;margin:0 auto 10px;width:100%;overflow:auto}.reelss.russiaukraine .flex-list li a{margin:8px 0;padding:0 6px}.reelss .swiper-containernn{margin:0 -5px}.reelss .swiper-containernn-recent{margin:0 -5px}.reelss.russiaukraine .swiper-button-next,.reelss.russiaukraine .swiper-button-prev{display:none}.andhra-district .andhra-pradesh .content-flex{width:94%;align-items:center;justify-content:center;margin:0 auto}.andhra-district .andhra-pradesh .content-flex img{width:100%}.andhra-district .andhra-pradesh .content-flex p{padding-left:0;padding-top:10px;font-size:16px;line-height:20px;padding-bottom:10px}.andhra-pradesh .district{display:block;width:100%}.district .politics-business{width:100%!important;margin-bottom:10px}.reelss .loco_cat.loco_section .col-md-2 a img{padding-right:10px;width:30%}.reelss .row{display:flex;width:100%}.reelss .heding h2{padding:15px 10px 5px!important}.andhra-content.office .row{display:flex;width:100%}.office a img{padding-right:10px;width:33%}.andhra-content.office .andhra-pradesh .politics-business{margin:0 10px 0 10px;border-right:0 solid #33333330;width:100%;padding:10px 0 10px;border-bottom:2px solid #eee}.reelss .heding h2{font-size:16px}.reelss.video-stories .swiper-button-next,.reelss.video-stories .swiper-button-prev{display:none}.bell .div{color:snow;display:flex;word-break:break-all;position:relative;font-size:15px;align-items:center;justify-content:center;margin:0 auto}.bell div{width:100%;margin:0 0 0 20px;height:25px;background-color:red}section.bell{width:300px;height:15px}.reelss.recently-viewed .reelss-ul a{display:none}.reelss.recently-viewed .swiper-button-next,.reelss.recently-viewed .swiper-button-prev{display:none}.reelss .loco_cat.loco_section .col-md-2 a{margin:15px 0 0 0}.footer-widget{width:100px;margin:10px}.footer-ul{display:block}.footer-widget-heading h3{font-size:18px}.footer-widget ul li a{font-size:13px}.footer-widget ul li{margin-bottom:5px}.copyright-text.download a{text-align:center}.copyright-text.download img{width:50%}.district .politics-business.five-cols{width:100%!important}.entertainment-telugu.spacing{margin:0 auto 20px;overflow:hidden}.entertainment-telugu .view-all a img{padding-right:10px;width:7%;margin:0}.view-all a img{padding-right:3px;width:20%}.view-all a{font-size:12px}#ads2{display:none}.footer-section .row{display:flex;flex-wrap:wrap;justify-content:start;padding-left:10px}.text-lg-left{width:100%}.footer-menu ul{margin-bottom:20px;display:flex;align-items:center;justify-content:center;margin:0;width:100%;padding:10px;max-width:none}.reelss-ul a{margin:0}.d-lg-block.text-right{width:100%}.footer-menu li{display:inline-block;padding:0 5px}.copyright-text p{text-align:center;color:#fff}.entertainment-scroll{display:block}.row{display:block;width:100%}.loco_cat.loco_section .container{width:100%}.andhra-pradesh{display:block}.andhra-pradesh .politics-business .politics{width:42%}.press-release .content-flex{width:100%;max-width:none;margin:0 auto;padding:0 10px}.reelss.stories .swiper-containernr{margin:0 -4px 10px}.reelss.video-stories .loco_cat.loco_section .swiper-slide .svg--position{position:relative;display:flex;align-items:center;justify-content:center;margin:0 auto;width:100%}.andhra-content.andhra-district .row{display:flex;width:100%;margin:0 auto;align-items:center;justify-content:center}.andhra-content .heding h2{padding:10px 0 0 20px!important;font-size:16px;line-height:normal}.andhra-content .heding.news-heding.desk h2{display:none}.andhra-content .heding.news-heding.mobile h2{display:block;padding:10px 0 0 0!important}.andhra-content .heding.news-heding.mobile hr{display:block}.andhra-content .andhra-pradesh.press-release .heding h2{padding:10px 0 10px 0!important;font-size:16px;margin-top:10px}.press-release .content-flex .content-padding hr{margin-top:3px;margin-bottom:3px}.press-release .content-padding p{font-size:15px;width:100%}.andhra-content .andhra-pradesh.press-release img{border-radius:10px}.press-release.andhra-pradesh .content-padding{padding:0 10px}.select-selected{font-size:12px}.related.entertainment-sec .entertainment-bg{width:100%;position:relative;display:inline-block}ul.pagination-items{margin-top:10px;margin-bottom:0}.related.entertainment-sec .entertainment-scroll{padding:5px 5px}.related .articles{width:100%}.social-icons .live-ads{display:block}.reviews .share-content .back-button{width:50%}.live-tabs.photo-gallery .related.entertainment-sec .entertainment-scroll .share-content{width:100%;margin-left:10px}.photo-gallery .related.entertainment-sec .entertainment-scroll{flex-direction:column}.photo-gallery .related.entertainment-sec .entertainment-flex.news-latest .entertainment-scroll{flex-direction:row}.related #features{width:100%;height:auto;display:flex;align-items:center}.related.entertainment-sec{display:block}.sub-flex ul li{font-size:16px}.related.entertainment-sec .entertainment-bg .andhra-pradesh .district{display:block}.related.entertainment-sec .district .politics-business{width:100%!important}.entertainment-sec .entertainment-bg .andhra-pradesh .district .content-flex{margin:0 4px 0}.entertainment-sec .entertainment-bg .andhra-content.andhra-district .andhra-pradesh .district .content-flex{margin:0 auto 10px;display:flex;flex-direction:row;align-items:center;justify-content:space-between;width:100%}.related.entertainment-sec .andhra-pradesh .district .politics-business .politics{max-width:300px}.entertainment-sec .andhra-pradesh .politics-business .politics-flex{margin:0 0 0 10px}.andhra-district .andhra-pradesh .district .politics-business .content-flex p{padding:0 0 0;height:auto;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;text-overflow:ellipsis}.related.entertainment-sec .social-icons{width:100%;margin-left:2px}ul.pagination-items li{font-size:10px;padding:2px 8px;margin:0 1px}.social-icons .share b{font-size:17px}.social-icons .share{display:flex;align-items:center;justify-content:center;margin:0 auto;padding-left:10px}.live-tabs.photo-gallery ul.pagination-items{width:100%;position:relative;align-items:center;display:flex;justify-content:center}.entertainment-flex.news-latest .entertainment-scroll{display:flex}.related-posts hr{width:100%;margin-left:0;margin-top:0;margin-bottom:0}.share-content p{font-size:13px}.about-section p{font-size:16px}.about-section{padding:10px}.sub-flex ul{display:flex;padding-left:10px}.contact form.form-container{display:block}.about-section.reviews .entertainment-scroll img{width:100%}.indrani-slider .reviews .share-content{margin-left:0}.political-news h2{font-size:19px;line-height:25px;margin:0}.political-news .content-flex{width:100%}.political-news p{font-size:16px;line-height:25px}.follow p{font-size:15px;margin:2px 0}.follow{height:auto}.entertainment-telugu.trending .entertainment-flex{padding:10px 10px 0;margin-bottom:0}.related .andhra-content .heding h2{padding:0 0 5px!important}.related .andhra-pradesh .district{display:block}.select-selected:after{right:5px;top:calc(100% - 17px)}.reviews .entertainment-scroll.one .share-content h3{line-height:30px;color:#fff;font-size:23px}.reviews .entertainment-scroll.one .share-content p{padding:1px 0}.reviews .share-content{margin-left:15px;position:relative;display:inline-block}.social-icons .share .list-inline{display:flex;width:auto;margin-left:5px}.sidenav .closebtn{position:absolute;top:-13px}.live-tabs.photo-gallery .nav-tabs{overflow:auto;width:100%;margin:10px 10px}.live-tabs.photo-gallery .nav-tabs li.tab.is-active{color:#fff;margin-bottom:3px}}@media only screen and (max-width:1600px){.header .header .logo img{width:200px;height:auto}.search{font-size:10px}}@media screen and (max-width:1920px){.container-footer{width:100%;display:flex;flex-wrap:wrap;margin:0 auto;position:relative;align-items:start;justify-content:space-between;max-width:945px}.swiper-container{width:100%;padding-top:0;padding-bottom:0}}@media screen and (max-width:1500px) and (min-width:1366px){.entertainment-telugu.spacing .indrani .indrani-scroll{margin-bottom:4px}.entertainment-telugu .entertainment-flex{height:870px;overflow:auto}.latest-news-entertainment.indrani-scroll .entertainment-telugu.spacing{height:1044px}.latest-news-entertainment.indrani-scroll .entertainment-telugu .entertainment-flex{height:963px;overflow:auto}.profile{padding:26px 10px;margin-top:17px}}@media screen and (max-width:1365px) and (min-width:1200px){.indrani h3{line-height:14px;padding:7px;margin-top:0;margin-bottom:0}.profile{margin-top:40px;padding:45px 10px}.submit{margin:4px auto 0}.profile p{font-size:19px;line-height:25px}.profile label span{font-size:15px;line-height:20px}.todays-poll h2{padding:5px;margin:5px 0}.profile form{margin:10px auto}.list-inline{max-width:calc(100% - 20px)}.entertainment-telugu .entertainment-flex{height:830px;overflow:auto}.latest-news-entertainment.indrani-scroll .entertainment-telugu .entertainment-flex{height:944px;overflow:auto}.latest-news-entertainment.indrani-scroll .entertainment-telugu.spacing{height:1025px}.entertainment-telugu.spacing .indrani .indrani-scroll{margin-bottom:15px}#fade-quote-carousell .entertainment-scroll{padding:12px 0;flex-direction:column}header .navbar-default .navbar-nav>li>a{padding:0 8px}header .navbar-default .topbar a{font-size:16px}.tabs-all .box{max-width:260px}.col-md-9{width:100%}.col-md-3{width:25%}.col-md-2{width:20.666667%}.reelss.russiaukraine .flex-list li a{padding:0 6px}.press-release .content-flex{max-width:260px}.container-footer{width:100%;display:block;margin:0 0;position:relative}.list-inline a{margin:5px 8px}.list-inline a .fa-2x{width:25px;height:25px}}@media screen and (max-width:1199px) and (min-width:1023px){.entertainment-telugu .view-all{position:sticky}.list-inline{max-width:calc(100% - 4px)}.list-inline a .fa-2x{width:24px;height:24px}.live-tabs.photo-gallery ul.pagination-items{width:100%}.entertainment-telugu .entertainment-flex{height:950px;overflow:auto}}@media screen and (max-width:1022px) and (min-width:996px){.politics-business .content-flex{justify-content:center}.live-news .live:after{left:30px}header .navbar-default .navbar-nav>li>a{line-height:2}header .navbar .navbar-nav{display:flex;overflow:auto;width:100%;white-space:nowrap}.list-inline{max-width:calc(100% - 4px)}.side-svg svg{color:#f00201;width:25px}.telugu{width:80px;font-size:18px;display:flex;align-items:center;justify-content:center}header .navbar-right button{font-size:16px}.list-inline a .fa-2x{font-size:13px;width:20px;height:20px}.list-inline a{margin:5px 2px}.live-news .live{font-size:13px}.tab-panel.is-active{display:block}.content-flex{width:100%}.politics-business{position:relative;width:100%;top:0}.politics-flex h3{font-size:18px;line-height:17px}.view-all{bottom:5px}.view-all a{font-size:15px}.entertainment-telugu{width:100%}.entertainment-telugu.spacing{margin:0 5px;overflow:hidden}.tupaki-heding{display:block}.reelss.russiaukraine .flex-list{display:flex;width:45%;overflow:auto;white-space:nowrap}.andhra-pradesh{display:block}.andhra-district .andhra-pradesh .content-flex{width:100%}.andhra-pradesh .district{width:100%}.andhra-district .andhra-pradesh .district .content-flex{display:block}.politics-business .content-flex .politics-flex{margin-left:5px}.andhra-pradesh .politics-business .politics-flex{width:95%}.andhra-pradesh .politics-business{width:100%;border-right:0 solid #33333330}.andhra-content.office .andhra-pradesh .politics-business{margin:0 0 5px 5px}section.bell{width:350px}#ads3{width:100%}.footer-widget-heading h3{font-size:20px}.footer-widget{padding:10px}header .navbar-default .topbar ul{overflow:auto}.live-ads{padding:0 10px}.entertainment-telugu{height:100%}}@media screen and (max-width:995px) and (min-width:768px){.view-all{bottom:9px}.related.entertainment-sec .social-icons{width:100%;margin-left:0}.related.entertainment-sec .entertainment-bg{width:100%}.related{display:block}.related-posts hr{width:100%;margin-left:0}.list-inline{max-width:calc(100% - 0px)}.latest .political-news .content-flex{width:100%}.political-news .content-flex{width:100%}header .collapse.in{display:grid;width:100%;overflow:auto}header .navbar-default .navbar-nav>li>a{line-height:2}header .navbar .navbar-nav{display:flex;justify-content:start}.social-icons .share b{font-size:15px}.list-inline a .fa-2x{font-size:13px;width:20px;height:20px}.live-ads{padding:0 10px}.entertainment-scroll{display:flex;padding:5px 10px}.live-news .live{font-size:15px}.indrani{height:320px}.indrani-scroll .entertainment-telugu{height:100%}.tabs-all .box{max-width:none}.latest-news-entertainment.indrani-scroll .entertainment-scroll p{margin:0 0 0}.tabs-all .content-flex{justify-content:left}.andhra-district .andhra-pradesh .content-flex p{padding-left:10px}.district .politics-business{margin-left:0}.andhra-pradesh .district .politics-business .politics{width:auto}.press-release .content-flex{max-width:unset}.live-tabs.photo-gallery .andhra-district .andhra-pradesh .content-flex{max-width:240px;margin:0 auto}.live-tabs.photo-gallery ul.pagination-items{width:100%}}.listing-small-image img{max-width:100px}@media only screen and (max-width:820px){.movie-details-page-wrap{display:block!important}.left-add{display:none}.right-add{display:none}.full-width{width:95%}.entertain-block{width:100%}.latest-news-block{display:block}.telugu-block-entertainment{width:100%;margin:0!important}.tupaki-excusive{width:100%;display:block}.excusive-inside{width:100%;display:block}.content-tupaki-block{padding:0 14px 0}.news-category .box{margin:0;padding:0 22px 0}.slider-img-inside .loco_cat.loco_section .swiper-slide{height:328px}.inside-boxover{overflow:inherit!important}.reelss.stories .loco_cat.loco_section .slide-fit img{width:29%;object-fit:cover}}a:focus,a:hover{text-decoration:none}.button-link,.news-link,.no-margin{margin:0!important}.button-link,.no-padding{padding:0}.reelss.russiaukraine .flex-list li a{white-space:nowrap}.view-all-link img{padding-right:10px!important;display:none}.custom-select .select-items div a{text-decoration:none;padding:0;cursor:pointer;user-select:none;color:#000}.text-in-slides a.news-link{width:100%}.non-loaded-slider .text-in-slides a.news-link{white-space:break-spaces}.top-heading{text-decoration:none}.reelss-ul a.top-heading{margin:0}.news-link{text-decoration:none}.swiper-container .card-text-content.text-in-slides a{color:#fff}.reels-heading a.news-link{color:#fff}.press-release h4{min-height:50px}.btn-primary:focus{background-color:transparent}.ads-slider .card-text-content h3{width:100%}.office a img{padding-right:0}.bread-home{color:#000}.breadcrumbs.sub-flex a{margin:0}.ham-btn{font-size:30px;cursor:pointer}.sidenav .closebtn{z-index:9;padding:0;margin:0}.sidenav{height:fit-content}.dropdown-container{margin-bottom:0}.dropdown-container .accordion{padding:0}.accordion__btn{position:relative;padding:0}.accordion__btn i.fa{position:absolute;top:50%;left:80%;transform:translate(-50%,-80%)}.accordion.header-sub-menu{padding:0}.accordion.header-sub-menu .accordion__btn{background:0 0}.search-area{display:none}.search-area{position:fixed;width:100vw;height:100vh;background:rgba(0,0,0,.7);z-index:9999;top:0}.search-area .close-btn{display:inline-block;right:40px;position:absolute;top:40px}.search-area .form{position:absolute;top:40%;left:50%;transform:translate(-50%,-40%);width:100%}.search-area .input-group.form-btn{display:flex;justify-content:center;align-items:center}.search-area .input-group.form-btn .search-text-value{height:50px;width:50%;background:0 0;border:none;border-bottom:1px solid #fff;color:#fff}.search-area small.search-caption{text-align:center;display:block}.search-now-btn{height:50px}.marquee a{white-space:nowrap}.home-page .video-gallery-cls{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;padding:0 1px}.home-page .reelss.thaja-varthalu .swiper-wrapper .swiper-slide .content{width:100%}.home-page .latest-news .content a.news-link:hover h3{color:#f00201}.listing-page .related-posts .top-heading.most-read{margin:0}.listing-page .most-read.news-latest .entertainment-scroll,.listing-page .related-posts.news-latest .entertainment-scroll{display:grid!important;grid-template-columns:70px auto}.listing-page .related-posts.news-latest .entertainment-scroll .share-content{width:auto}.pagination .disabled{pointer-events:none;opacity:.3}.pagination{float:none!important;justify-content:center}.movie-reviews .related-posts.movie-review .generic-right img{width:75px}.movie-reviews .related-posts.movie-review .generic-right .news-link.news-list{flex:1;padding-right:5px}.details-page-wrapper .share .ind-social-cover .ind-social-ul a.ind-social-click,.details-page-wrapper .share .ind-social-cover .ind-social-ul span.ind-social-click,.gallery-details-page-wrapper .share .ind-social-cover .ind-social-ul a.ind-social-click,.gallery-details-page-wrapper .share .ind-social-cover .ind-social-ul span.ind-social-click,.movie-details-page .share .ind-social-cover .ind-social-ul a.ind-social-click,.movie-details-page .share .ind-social-cover .ind-social-ul span.ind-social-click{font-size:17px;background:#f00201!important;color:#fff;border-radius:7px!important;width:30px;height:30px;display:flex;align-items:center;justify-content:center;margin:0 auto}.details-page-wrapper .author-link.h-author-internal-block{color:#77787b}.details-page-wrapper .share .ind-social-cover .ind-social-ul li.ind-social-li,.movie-details-page .share .ind-social-cover .ind-social-ul li.ind-social-li{margin:5px 6px}.details-page-wrapper .image_wrapper.cutom-gallery{position:relative!important}.details-page-wrapper .tags-wrapper a{margin-right:5px}.details-page-wrapper .entertainment-telugu.trending .generic-right .entertainment-scroll img{min-height:75px}.movie-details-page .related.entertainment-sec .entertainment-scroll img{min-height:75px}.details-page-wrapper .details-story-wrapper div{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:18px;line-height:27px;text-align:justify;color:#000;margin-top:20px;width:auto;display:block;height:auto}.movie-details-page .constent-review .share{justify-content:flex-start}.details-page-wrapper .author-link.h-author-internal-block,.details-page-wrapper .breadcrumbs.sub-flex a{margin:0}.details-page-wrapper .hocal-draggable{margin:0!important}.details-page-wrapper .hocal-draggable .read-this-also-wrap{border:1px solid #f00201;margin-top:15px;text-align:center}.details-page-wrapper .hocal-draggable .editor-inserted-link{font-size:16px;line-height:25px;font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:14px;color:#000;margin:0}.details-page-wrapper .hocal-draggable .editor-inserted-link .read-this-also{font-family:Roboto,sans-serif;font-style:normal;font-weight:700;font-size:16px;text-align:justify;color:#f00201;margin-right:5px}.details-page-wrapper .image-caption>*{font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:14px;line-height:19px;color:grey;margin-top:0}.synopsis-body{margin:0;padding:0;width:auto;height:auto;font-family:Roboto,sans-serif;font-style:normal;font-weight:400;font-size:16px;line-height:22px;text-align:justify;color:#000;font-weight:500!important}.reviews .entertainment-scroll .share-content .less-synopsis-btn,.reviews .entertainment-scroll .share-content .more-synopsis-btn{font-size:14px;line-height:25px;color:red;cursor:pointer;font-weight:300}@media screen and (min-width:767px){.topbar-logo{min-height:110px}.details-page-wrapper .slider-tags .svg--position p{min-height:78px;width:100%;display:flex;align-items:center}.details-page-wrapper .slider-tags .swiper-slide-active .svg--position p{padding-right:10px}.details-page-wrapper .slider-tags .swiper-slide-next .svg--position p{padding-left:10px}.reviews .entertainment-scroll .share-content .less-synopsis-btn,.reviews .entertainment-scroll .share-content .more-synopsis-btn{font-size:14px;line-height:25px;color:red;cursor:pointer;font-weight:300}@media screen and (min-width:768px){.topbar-logo{min-height:110px}.details-page-wrapper .slider-tags .svg--position p{min-height:78px;width:100%;display:flex;align-items:center}.details-page-wrapper .slider-tags .swiper-slide-active .svg--position p{padding-right:10px}.details-page-wrapper .slider-tags .swiper-slide-next .svg--position p{padding-left:10px}.reviews .entertainment-scroll .share-content .less-synopsis-btn,.reviews .entertainment-scroll .share-content .more-synopsis-btn{font-size:14px;line-height:25px;color:red;cursor:pointer;font-weight:300}}@media screen and (min-width:768px){.topbar-logo{min-height:110px}@media screen and (max-width:768px){.topbar-logo{min-height:45px}.details-page-wrapper .slider-tags .svg--position p{min-height:55px;width:100%;display:flex;align-items:center}.details-page-wrapper .share .ind-social-cover .color .ind-social-cover .ind-social-ul.color-mode,.movie-details-page .share .ind-social-wrapper .ind-social-cover .ind-social-ul.color-mode{display:flex}.details-page-wrapper .share .ind-social-cover .ind-social-ul li.ind-social-li,.movie-details-page .share .ind-social-cover .ind-social-ul li.ind-social-li,.movie-details-page .social-icons.movie-reviews .related-posts .top-heading.most-read{margin:0}.details-page-wrapper .tags-wrapper a{margin:0;margin-right:5px}.details-page-wrapper .breadcrumbs.sub-flex ul li{padding:0}.details-page-wrapper .entertainment-telugu.trending #right_level_2 .top-heading{margin:0!important}.details-page-wrapper .reelss.stories .heding .top-heading{margin:0!important}}p.synopsis{display:inline-block}.no-display{display:none}.fixed-height{height:200px}.details-page-wrapper .related p.related-para{padding-top:0!important}.movie-cast .card p{text-align:center!important}.live-tabs.photo-gallery .nav-tabs li{width:auto;height:auto;display:block;padding:0}.live-tabs.photo-gallery .nav-tabs li a{display:flex;justify-content:center;align-items:center;width:100px;height:40px;color:#000}.live-tabs.photo-gallery .nav-tabs li a:hover{border:none}@media screen and (max-width:768px){.live-tabs a{margin:0}}.live-tabs.photo-gallery .ads-slider .card-text-content h3{position:inherit}.live-tabs.photo-gallery .ads-slider .card-text-content.text-in-slides a{margin:0}.non-loaded-slider{white-space:nowrap;overflow-x:auto;overflow-y:hidden;height:420px;display:block}.non-loaded-slider .img-wrapper{height:420px}.non-loaded-slider .non-loaded-slider-item{position:relative;display:inline-block;width:25%;margin:1%;margin-top:0;margin-bottom:0;margin-left:0;height:420px}.share .ind-social-ul.color-mode{margin:0}.is-active .gallery-tab-link{color:#fff!important}.image_wrapper.cutom-gallery .slides-num{position:absolute;right:15px;color:#fff;font-size:20px;top:15px}@media screen and (max-width:768px){.gallery-page .social-icons .related-posts .top-heading.most-read{margin:0}a.nav-tabs-link{margin:0}}#level_2 .politics-business .content-flex{justify-content:left}.mixin_with_button .politics-business.top-news .content-flex img{max-width:200px;max-height:120px}.tabs-all #parent .box .content-flex img{max-width:150px}.tags-section .content{width:100%}.tags-section .andhra-pradesh{justify-content:left}.tags-section .tags-desc{margin-top:10px}.tags{margin-top:25px}.author-block{display:flex}.author-img-container{width:100px;margin-right:20px}.author-img-container img{border-radius:50%}.andhra-content.author-section{padding:20px;margin-top:0}.author-name h3{margin:0}.author-desc p{margin-top:10px}@media screen and (max-width:768px){.andhra-content.author-section{margin-bottom:10px}}@media screen and (max-width:768px){.gallery-details-page-wrapper .author-name.icon-link{margin:0}.gallery-details-page-wrapper .entertainment-telugu.trending .top-heading,.reelss.stories .heding .top-heading,.share .ind-social-cover .ind-social-ul li.ind-social-li{margin:0}.home-page .top-heading{margin:0}.home-page .latest-news-entertainment #level_3_1 .entertainment-scroll img,.home-page .latest-news-entertainment #level_3_3 .entertainment-scroll img{max-width:105px}.home-page .latest-news-entertainment .entertainment-telugu.spacing #level_3_2 .entertainment-scroll a.news-list{width:100%;justify-content:flex-start}.home-page .entertainment-telugu .view-all a{padding:8px}.entertainment-telugu.spacing a.movie-ads-run{width:100%}.home-page .indrani-scroll .poll .carousel.slide .carousel-inner .entertainment-scroll a.news-link{margin:0!important;width:100%}.home-page .press-release .content-padding>a{margin:0}.home-page .press-release .content-padding h4.active{min-height:auto}.home-page .reelss-ul .heding a,.home-page .reelss.recently-viewed .reelss-ul a,.reelss.video-stories .reelss-ul a{display:block}.home-page .reelss-ul .heding a.view-all-link,.home-page .reelss.recently-viewed .reelss-ul a.view-all-link,.reelss.video-stories .reelss-ul a.view-all-link{display:none}.home-page .video-gallery-cls{grid-template-columns:1fr}#level_15 .andhra-content.office .politics-business .politics-flex{width:inherit}#level_15 .office .andhra-pradesh .content-flex p{width:100%}.live-tabs a.aads{margin:8px 25px}}@media screen and (max-width:768px) and (min-width:320px){.entertainment-telugu.spacing #level_3_2 a.linked-media{width:100%}.details-page-wrapper .image_wrapper.cutom-gallery img{max-height:453px!important}.tab-panel{padding:0 10px}.tab-panel.content-flex img{border-radius:5px;margin:0}}.page.gallery-details-page-wrapper .inline .ind-social-cover .ind-social-ul .ind-social-li{margin-right:5px}.homepage .ad-ons.movie-review-img a{width:300px}@media screen and (min-width:1024px) and (max-width:1445px){#level_1 .card img{height:420px}}@media screen and (max-width:768px){.latest-news-entertainment.indrani-scroll .entertainment-telugu.spacing{height:1010px}.latest-news-entertainment #level_4_2 .entertainment-scroll p{height:100px}.single-image img{min-height:200px}}.buzz-parent-wrapper{margin:20px 0}.all-slider-items-wrapper .image-slider-item-wrapper{float:none!important}.grid-block-for-images{display:grid!important;grid-template-columns:75px auto}.grid-block-for-images .linked-media img{width:100%}.movies-link{color:#000}.movies-link:hover{color:#f00201}.ott .politics img{border-radius:0}a.bell-ad-link{margin:8px 25px}#level_3_2_ad img{margin-bottom:5px}.footer-menu li{padding:0 5px;text-align:left}p.no-bold-words{font-weight:500!important}.cast-type{font-weight:500!important;font-style:italic!important;font-size:13px!important}.cast-name{line-height:20px!important;margin-top:5px!important}.top-news .tab-content #tabs-home3 .politics-business.top-news{display:flex;flex-direction:column;justify-content:space-around}.top-news .tab-content #tabs-home3 .politics-business.top-news hr{margin-left:0;margin-right:0}.top-news .tab-content #tabs-home3 .politics-business.top-news .content-flex{justify-content:flex-start}.top-news .tab-content #tabs-home3 .politics-business.top-news .politics-flex{margin:0 10px}.top-news .tab-content #tabs-home3 .politics-business.top-news .content-flex,.top-news .tab-content #tabs-profile3 .politics-business.top-news .content-flex{justify-content:revert}.top-news .tab-content #tabs-home3 .politics-business.top-news img,.top-news .tab-content #tabs-profile3 .politics-business.top-news img{max-width:165px!important}.single-gallery-click-zoom img{width:100%}.carousel-control-next{width:auto}.details-page-wrapper .slider-tags .swiper-button-prev,.details-page-wrapper .swiper-button-next{top:50%}.slider-tags .svg--position p{margin-top:0!important}.slider-tags .svg--position,.slider-tags .svg--position a.news-link,.slider-tags .svg--position p{height:100%!important}.slider-tags .swiper-wrapper{box-sizing:border-box!important}.slider-tags .swiper-slide{height:auto!important}.s-amp-block-heading-story{color:red}.s-amp-block-heading:before{border:2px solid red!important}@media screen and (max-width:768px){.non-loaded-slider,.non-loaded-slider .img-wrapper,.non-loaded-slider .non-loaded-slider-item{min-height:195px;height:auto!important}.non-loaded-slider .non-loaded-slider-item{width:33%}.non-loaded-slider .card-text-content h3{white-space:break-spaces}}.back-button:hover{color:#fff}::-webkit-scrollbar{width:8px}::-webkit-scrollbar-thumb:horizontal{height:8px}::-webkit-scrollbar-track{background:#ddd}::-webkit-scrollbar-thumb{background:#bbb}::-webkit-scrollbar-thumb:hover{background:#555}@media screen and (max-width:768px){::-webkit-scrollbar{width:5px}::-webkit-scrollbar-thumb:horizontal{height:5px}}}.page.photo-gallery-details-page .story_content .paira-h4 *,.photo-gallery-details-page .h-news-desc,.photo-gallery-details-page .h-news-heading{font-family:Roboto!important}.photo-gallery-details-page .h-news-heading{font-weight:600}.page.photo-gallery-details-page .story_content .paira-h4 *{font-weight:300!important}div#noPosts{height:430px!important}#parent .politics-flex p{line-height:27px}}figure.politics a.movies-link img{aspect-ratio:unset!important}figure.politics a img{aspect-ratio:5/3}div#level_19 .content h4{font-size:15px!important}@media only screen and (min-device-width :768px) and (max-device-width :822px){.latest-news-entertainment.upto-off{margin:376px 0 0!important}.reelss-ul a.view-all-link{margin-right:14px;padding-top:14px}.entertainment-telugu.spacing a.movie-ads-run img{aspect-ratio:5/3!important;margin-top:50px}.reelss-ul .view-all{margin-right:30px}.related .articles{width:100%!important}.details-page-wrapper .share .ind-social-cover .ind-social-ul li.ind-social-li{margin:5px 0}.latest-news-entertainment.upto-off{margin:376px 0 0!important}.content-flex{width:100%}.politics-business.topnews-left{padding:0 11px 0;width:100%!important;margin:595px 0 0!important}.constent-review .share{margin-top:15px}.andhra-pradesh.press-release .news-link img{width:100%;border-radius:10px}.andhra-content.ott .andhra-pradesh .politics-business{width:33%!important;margin:0 1px!important}.tabs-all-ul{display:flex;overflow:scroll}.andhra-district .andhra-pradesh .district .politics-business{width:100%}.slider-tags{margin-bottom:10px}.pagination.clearfix a{margin-left:13px}}@media only screen and (max-width:767px){.ads-slider .swiper-button-next,.ads-slider .swiper-button-prev{display:flex}.reelss.stories .swiper-containernr{overflow:scroll!important}.reelss-ul a.view-all-link{font-size:15px}.andhra-content.office a.view-all-link img{display:none}.reelss.video-stories .swiper-button-next,.reelss.video-stories .swiper-button-prev{display:flex}.reelss.video-stories .reelss-ul a.view-all-link{font-size:16px}.reelss.video-stories .reelss-ul a.view-all-link img{display:none}}@media (min-device-width :844px) and (max-device-width :927px){.noPostSec{height:400px}.politics-business.top-news.topnews-left{position:inherit}.politics-flex h3{line-height:17px}.indrani{height:406px}.ad-ons img{width:100%;width:300px;height:132px}.indrani h3{font-size:15px;line-height:24px;margin-bottom:2px}.entertainment-telugu h2{font-size:21px}.tabs-all .politics-flex{text-align:left;min-width:393px}.andhra-district .andhra-pradesh .district-min{width:37%;margin-top:10px}.andhra-district .andhra-pradesh .district-min img{width:97%}.andhra-content .andhra-pradesh.press-release.press-release .content-flex{width:33%}.andhra-content .andhra-pradesh.press-release.press-release .content-flex p{font-size:14px;line-height:21px;width:188px}.andhra-content .andhra-pradesh.press-release.press-release .content-flex .content-padding h4{line-height:20px}.tabs-all-ul{display:flex;overflow:scroll}.political-news .content-flex{width:69%}.andhra-content.political-news .andhra-pradesh .entertainment-telugu.trending{width:29%}.related{display:flex!important}.related #features img{height:250px}.ind-social-cover .ind-social-ul .ind-social-li{min-width:30px!important}.color .ind-social-cover .ind-social-ul.color-mode{display:flex!important}.details-page-wrapper .share .ind-social-cover .ind-social-ul li.ind-social-li{margin:0 4px}}@media (min-width:540px) and (max-width:736px){.reelss.stories .loco_cat.loco_section .slide-fit img{width:67%!important}.footer-widget{width:159px;margin:10px}.container-footer{justify-content:start!important}div#level_19 .content h4{font-size:13px!important;margin-left:76px}}@media only screen and (max-width:650px) and (min-width:280px){.telugu{font-size:14px;height:20px;position:absolute;top:12px;left:3%;width:60px;display:flex;align-items:center;justify-content:center}.side-svg svg{color:#f00201;font-size:20px!important;padding:8px 0}header .navbar-default .topbar ul{display:inline-flex;overflow:scroll}.reelss .swiper-containernn .swiper-wrapper .swiper-slide{width:151px!important;margin-right:20px}.story-heading{font-size:16px!important}h2.s-amp-block-heading{font-size:16px!important}.live-tabs.photo-gallery .nav-tabs li.tab.is-active{color:#fff;margin-bottom:3px}.is-active .gallery-tab-link{color:#fff!important}.navbar-toggle{position:relative;float:right;padding:2px 5px;margin-right:0;margin-top:0;margin-bottom:8px;background-color:transparent;background-image:none;border:1px solid transparent;border-radius:4px}.ads-slider .swiper-button-next,.ads-slider .swiper-button-prev{display:none}.content-flex .entertainment-content p{font-size:11px;padding-top:0;line-height:13px}.entertainment-telugu.spacing.telugu-block-entertainment{justify-content:start!important}.entertainment-telugu.spacing.telugu-block-entertainment div{margin:10px auto}.tabs-all-ul{display:flex;overflow:scroll}.andhra-district .andhra-pradesh .district-min{width:100%}.ott-bg{margin:10px 0}.andhra-pradesh .politics-business{width:100%}.bell .div{font-size:13px;margin:0}.footer-menu{width:100%}.footer-menu h3{width:13%;font-size:10px}.limitExceed-wrap{min-width:262px;padding:0}.reelss.video-stories .reelss-ul a.view-all-link{font-size:14px;margin-right:6px}.andhra-content.office .reelss-ul a{display:flex}.andhra-content.office .reelss-ul a.view-all-link{font-size:14px;margin-right:6px;margin-top:10px}.reelss.thaja-varthalu .reelss-ul a.view-all-link{display:none}.color .ind-social-cover .ind-social-ul.color-mode{display:flex!important;overflow:scroll}}@media (max-width:653px) and (min-width:650px){.sidenav{height:100%!important}.footer-widget{width:137px;margin:10px}}@media (max-width:600px) and (min-width:320px){.swiper-container{overflow:scroll}.reelss .swiper-containernn{overflow:scroll}.footer-menu{display:flex}#tabs-home3{padding:0 10px}.tab-panel .content-flex img{border-radius:5px;margin:0}}@media (max-width:322px) and (min-width:320px){.news-category .box{padding:0}}@media (max-width:743px) and (min-width:739px){.politics-business.topnews-left{margin:10px 0 0!important}.live-tabs a{margin:0}.entertainment-telugu.spacing a{display:contents!important}.reelss.stories .loco_cat.loco_section .slide-fit img{width:67%}}@media (max-width:898px) and (min-width:894px){.andhra-pradesh{display:block!important}.entertainment-telugu.trending{width:100%!important}}@media (min-device-width :810px) and (max-device-width :844px){.indrani{margin-top:50px}.andhra-pradesh .politics-business .content-flex{justify-content:space-around!important}.tabs-all .box{margin:0 10px}}.ad-popup-wrap .view-content,.full-w-h{width:100%;height:100%}.popup-flex{display:flex}.popup-flex-center{text-align:center;vertical-align:middle;align-items:center;justify-content:center}.ad-popup-wrap #modal-content{background:0 0;border:none;left:1%;right:1%;bottom:1%;top:1%;display:flex;align-items:center;justify-content:center}.ad-popup-wrap .cross-btn{display:none}.ad-popup-wrap .popup-anchor img{max-width:100%;max-height:100%;width:auto;height:auto;margin:0 auto}.ad-popup-wrap .adv-title{background:#fefefe;text-align:center;height:30px;padding-top:5px;position:absolute;width:100%;top:0;left:0}.ad-popup-wrap .adv-title .popup-custom-cross-btn{right:0;color:#fff;background:#000;padding:5px 10px;margin-top:-5px;position:absolute;cursor:pointer}.ad-popup-wrap .add-overlay{padding-top:20px}.ad-popup-wrap .adv-parent{background:rgba(0,0,0,.2);padding:20px}@media only screen and (min-width:992px){.tabs-wrapper{height:450px}}.back-button:hover{color:#fff}::-webkit-scrollbar{width:8px}::-webkit-scrollbar-thumb:horizontal{height:8px}::-webkit-scrollbar-track{background:#ddd}::-webkit-scrollbar-thumb{background:#bbb}::-webkit-scrollbar-thumb:hover{background:#555}@media screen and (max-width:768px){::-webkit-scrollbar{width:5px}.political-news .content-flex{width:100%!important}.entertainment-telugu .view-all a{padding:8px!important}.live-tabs a.aads{margin:8px 25px}.entertainment-telugu.spacing.telugu-block-entertainment div{margin:0!important}.office .andhra-pradesh .content-flex p{width:90%!important}}@media (max-width:850px) and (min-width:844px){.politics-business.topnews-left{margin:0!important}.press-release .heding h2{font-size:18px}.entertainment-telugu h2{font-size:19px!important}}@media screen and (min-width:767px) and (max-width:810px){.tab-content .content-flex a.news-link img{margin:0!important}}.container-footer{flex-wrap:wrap!important}.footer-widget{flex-basis:40%!important;max-width:max-content!important}.photo-gallery-details-page .h-news-heading{font-weight:600}.page.photo-gallery-details-page .story_content .paira-h4 *{font-weight:300!important}.overlay-rotate-device{display:none;position:fixed;z-index:9999999;background:rgba(0,0,0,.9);top:48%;text-align:center}.overlay-rotate-device .rotate-message{color:#fff;font-size:30px;padding:10px}@media screen and (min-width:320px) and (max-width:1024px) and (orientation:landscape){.overlay-rotate-device{display:block}}@media only screen and (max-width:600px){.political-news .share{display:flex!important;overflow:scroll}.press-release .content-padding h4{margin-bottom:0}.content-flex h1{text-transform:none;margin-bottom:2%;font-size:28px!important;line-height:1.2}.political-news .details-page h2{font-size:20px!important;font-weight:400;line-height:1.2}.reelss .loco_cat.loco_section .swiper-slide h4{padding-left:10px}.entertainment-telugu a.top-heading{display:block}.entertainment-telugu h2{margin-bottom:0!important}.political-news .share{display:flex!important}.press-release h4{min-height:24px}}.h-news-heading{color:#000!important}.s-amp-description{min-height:20%}a.s-amp-block-heading-story{color:#f00201}@media only screen and (min-width:600px) and (max-width:912px){.content-flex h1{font-size:29px!important}.content-flex h2{font-size:20px}.press-release .content-padding h4{margin-bottom:0}}.content-flex h1{text-transform:none;margin-bottom:4%;font-size:30px;padding-top:10px}.political-news .details-page h2{font-weight:400;font-size:21px;line-height:1.2!important}.share span{display:none!important}.share ul li.ind-social-li span{display:flex!important}.share b{display:none!important}.political-news .share{justify-content:center}@media only screen and (min-width:810px){.content-flex h1{margin-bottom:0!important}.political-news .share{justify-content:start}political-news .details-page h2{font-size:21px}}.reelss .loco_cat.loco_section .swiper-slide .svg--position svg{display:none}.title .story-heading a{color:#dc0403}.title .story-heading{padding:15px 10px 0!important}.title .story-heading hr{color:#000}.get-white-color{margin:10px 0;position:relative;background:#fff;width:100%;padding:0 0 20px}@media only screen and (max-width:600px){.non-loaded-slider .non-loaded-slider-item{height:218px;width:33%}.ads-slider .fixed-height .swiper-container .swiper-wrapper{height:108px!important;Width:33%}}@media only screen and (min-width:600px) and (max-width:930px){.non-loaded-slider .non-loaded-slider-item{height:359px;width:33%}}.story-heading{font-size:22px}h2.s-amp-block-heading{font-size:22px}.swiper-button-next,.swiper-button-prev{top:50%!important}.swiper-containernn .swiper-wrapper .swiper-slide{width:253.5px!important;margin-right:20px}.swiper-wrapper.non-loaded-slider{overflow:hidden!important}.live-tabs.photo-gallery .nav-tabs li a{display:flex;justify-content:center;align-items:center;width:100px;height:40px;color:#000}@media only screen and (max-width:820px){ul.nav.navbar-nav::-webkit-scrollbar{display:none}.tabs-all-ul::-webkit-scrollbar{display:none}.s-amp-grid-box.slider-style::-webkit-scrollbar{display:none}.articles .andhra-pradesh .district .politics-business .politics{width:75px}.swiper-button-next:after,.swiper-button-prev:after{font-size:16px!important}}@media only screen and (min-width:768px) and (max-width:820px){.articles .andhra-pradesh .district .politics-business .politics{width:100px!important}}.details-page-wrapper .content-flex p{font-family:Mallanna!important;font-weight:500!important;min-height:80px;padding:5px 40px}.single-image img{width:100%}.bell div,.entertainment-telugu h2,.header .navbar .navbar-collapse,.telugu{background:#dc0403}#parent .box h3,#tabs-home3 .content-flex .entertainment-content p,#tabs-profile3 .content-flex .entertainment-content p,.andhra-content .heding h2,.andhra-district .andhra-pradesh .district-min p,.politics-flex h3,.press-release .heding h2{color:#dc0403}a.s-amp-block-heading-story{color:#ae1817}.image_wrapper.cutom-gallery.clearfix2{display:flex;justify-content:center}.swiper-button-previous{background:#fff;border:.1px solid gray;margin-right:14px;padding:5px 11px;margin-top:10px;color:red;font-size:17px;height:32px;margin-bottom:10px}.swiper-button-next_image{background:#fff;border:.1px solid gray;margin-right:14px;padding:5px 11px;margin-top:10px;color:red;font-size:17px;height:32px;margin-bottom:10px}
     </style>
     <style>
      /* deepika tupaki changes */
@media only screen and (min-width: 992px) {
    .live-tabs.photo-gallery .andhra-content .tabs-wrapper {
        height: 100%;
    }
}

.live-tabs.photo-gallery .tab-content .content-flex img {
    margin: 0;
    min-height: 300px;
    height: 100%;
    width: 180px;
    object-fit: cover;
}

.movie-details-page span.tags-wrapper button {
    margin-right: 6px;
}

/* end */


/* from Async Body Tags */
/*Destop larg Homepage*/
/*Trending*/
.details-page-wrapper .entertainment-telugu.trending .generic-right .entertainment-scroll img {
    min-height: inherit;
}

/**/

.grid-block-for-images {
    display: grid !important;
    grid-template-columns: 75px auto;
}

.navbar-fixed-top,
header .navbar-fixed-bottom {
    position: relative;
    /* position: fixed; */
    top: 0;
    right: 0;
    left: 0;
}

header .navbar-default .topbar-logo {
    background: #fff;
    padding: 10px 27px;
    display: flex;
    flex-wrap: inherit;
    align-items: center;
    justify-content: space-between;
    max-width: 1534px;
    margin-right: auto;
    margin-left: auto;
}


article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
    display: block;
    position: relative;
    top: 0;
    right: 0;
    left: 0;
}

.website-wrapper {
    display: flex;
    justify-content: space-between;

    position: relative;
    padding: 10px 0;
    background: #d6d6d6;
    flex-wrap: inherit;
    max-width: 1534px;
    margin-right: auto;
    margin-left: auto;
}

.footer-section {
    position: relative;
    padding: 10px 0 0;
    display: block;
    top: 0;
    right: 0;
    left: 0;
}

.container-footer {
    margin: auto;
    flex-wrap: inherit;
    max-width: 1073px;
    margin-right: auto;
    margin-left: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    padding: 10px 0;
}

.copyright-area {
    display: block;
    position: relative;
    top: 0;
    right: 0;
    left: 0;
}

.container-fluid {
    flex-wrap: inherit;
    max-width: 1534px;
    justify-content: space-between;
    align-items: center;
    position: relative;
}

/*End*/


@media(min-width:280px) and (max-width:736px) {
    .entertainment-telugu .view-all a {
        background: #c4c4c4;
    }

    .reelss.video-stories {
        padding: 0 0 40px;
    }

    .politics-business.topnews-left {
        margin: 0px 0 0;
    }

    /*.andhra-content.office img{
    display: none;
}*/

    /*.view-all-link img{
    display: none !important;
}*/

    .entertainment-telugu .view-all {
        padding: 20px 0 20px;
        background: #FFF;
    }

    .entertainment-telugu .view-all a {
        font-size: 17px;
    }

    .politics-business.topnews-left {
        margin: 0px 0 0 !important;
    }

    .latest-news-entertainment.latest-news-block {
        margin: 0px 0 0 !important
    }

    .grid-block-for-images {
        display: grid !important;
        grid-template-columns: 75px auto;
    }

    .live-tabs a {
        margin: 0px 0px;
    }

    .entertainment-telugu.spacing a {
        width: auto;
    }

    .content-tupaki-block {
        padding: 0 0px 0;
    }

    .news-category .box {
        margin-left: 10px;
        padding: 0px;
    }

    #parent {
        display: block;
    }

    .reelss.stories .loco_cat.loco_section .slide-fit img {
        width: 100%;
    }

    /*Footer Youtube*/

    .home-page .video-gallery-cls {
        grid-template-columns: 1fr;
    }

    .container-footer {
        flex-wrap: wrap;
    }

    .andhra-content.office .politics-business .politics-flex {
        width: -webkit-fill-available;
    }

    /*Social icon*/
    .political-news .share {
        display: block;
    }

    .details-page-wrapper .share .ind-social-cover .ind-social-ul li.ind-social-li,
    .movie-details-page .share .ind-social-cover .ind-social-ul li.ind-social-li {
        margin: 5px 2px;
    }


    /*slider Arrow*/
    .indrani .indrani-scroll .poll #carousel .carousel-control-next {
        left: 30px;
    }

    /*box office*/
    .andhra-content.office .reelss-ul a {
        display: block;
    }

    .reelss.video-stories .reelss-ul a {
        display: block;
    }

    /*End*/

}




@media(min-width:768px) and (max-width:820px) {
    #level_4_2_ad_2 {
        min-height: 570px !important;
        display: block !important;
    }

    .left-add {
        display: none;
    }

    .right-add {
        display: none;
    }

    .full-width {
        width: 95%;
    }

    .entertain-block {
        width: 100%;
    }

    .latest-news-block {
        display: block;
    }

    .telugu-block-entertainment {
        width: 100%;
        margin: 0 !important;
    }

    .tupaki-excusive {
        width: 100%;
        display: block;
        background-color: #FFF;
    }

    .excusive-inside {
        width: 100%;
        display: block;
    }

    .content-tupaki-block {
        padding: 0 0px 0;
    }


    .news-category .box {
        margin: 0;
        padding: 0 22px 0;
    }

    .slider-img-inside .loco_cat.loco_section .swiper-slide {
        height: 328px;
    }

    .inside-boxover {
        overflow: inherit !important;
    }

    .reelss.stories .loco_cat.loco_section .slide-fit img {
        width: 71%;
        object-fit: cover;
    }

    .tab-panel.is-active.top-1 {

        width: 100%;

    }

    .tab-content .content-flex img {
        width: 100%;
    }

    /*Box Office*/
    .politics-business.news {
        width: 100%;
        top: 23px;
    }


    .andhra-content.office .andhra-pradesh .politics-business {
        width: 100%;
        float: left;
    }

    /*End*/


    /*Top10*/

    .andhra-pradesh .politics-business {
        width: 100%;
    }

    .ott-bg {
        margin: 20px 0 0;
    }

    .heding.news-heding.desk {
        display: none;
    }

    /*End*/

    /*heading*/

    .heding {
        padding: 0 20px 0;
    }

    /*movie Reviews*/
    .entertainment-telugu {
        width: 100%;
    }

    .latest-news-entertainment {
        display: block;
    }

    .latest-news-entertainment.indrani-scroll .entertainment-telugu .entertainment-flex {
        padding: 0 15px 0;
    }

    .latest-news-entertainment.indrani-scroll .entertainment-telugu.spacing {
        overflow: inherit;
    }

    .indrani .indrani-scroll .poll #carousel .carousel-control-next {
        right: 38px;
    }

    .indrani .indrani-scroll .poll #carousel .carousel-control-prev {
        left: 38px;
    }

    .tabs-all .box {
        margin: 0px 15px 0;
    }

    /*End*/

    /*innerpages entertainment*/



    .live-ads {
        display: none;
    }

    .live-tabs {
        width: 100%;
    }

    .sub-flex ul {
        padding: 0 10px 0;

    }

    .andhra-district .andhra-pradesh .district .content-flex {
        max-width: 100%;
    }


    /*Telangana*/


    .andhra-district .andhra-pradesh .district-min {
        width: 100%;
        object-fit: cover;
    }

    .andhra-pradesh .district {
        display: flex;
        width: 100%;
    }

    .andhra-pradesh {
        display: block;
    }


    /*PRESS RELEASE*/
    .press-release .heding h2 {
        text-align: justify;
    }

    .content-flex p {
        width: 100%;
    }

    /*End*/
    /*Boxoffice*/
    .andhra-content.office .andhra-pradesh {
        float: left;
    }

    /*End*/
    .politics-business.topnews-left {
        margin: 588px 0 0;
        background: #FFF;
        padding: 0 11px 0;
    }


    /*Homepage*/

    .andhra-pradesh .politics-business {
        width: 32%;
        top: 0;
        float: left;
        margin: 0;
    }

    .latest-news-entertainment.latest-news-block {
        margin: 336px 0 0;
    }

    .noru {
        width: 100%;
    }

    .entertainment-scroll p {
        width: 500px;
    }

    .indrani {
        height: 785px;
    }

    .indrani h3 {
        line-height: 30px;
    }

    .entertainment-telugu.spacing a {
        width: 100%;
    }

    .indrani .indrani-scroll .poll #carousel .entertainment-flexs img {
        width: 78px;
        height: 104px;
    }

    .slider-mini {
        margin: 305px 0 0;
    }

    .indrani .indrani-scroll .poll #carousel .carousel-control-next {
        left: 20px;
    }

    /*PhotoPlay*/
    .s-amp-content-block {
        background: #FFF;
    }

    /*End*/

}




@media(max-width:820px) {

    .politics-business.topnews-left {
        margin: 40px 0 0;
        background: #FFF;
        padding: 0 11px 0;
    }

    .latest-news-entertainment.latest-news-block {
        margin: 0px 0 0;
    }

    .most-pp {
        margin: 138px 0 0;
    }

    .home-page .video-gallery-cls {
        grid-template-columns: 1fr;
    }

}

@media(max-width:768px) {
    .politics-business.topnews-left {
        margin: 596px 0 0;
        background: #FFF;
        padding: 0 11px 0;
    }

    .latest-news-entertainment.latest-news-block {

        margin: 400px 0 0;

    }

    .latest-news-entertainment {
        margin: 4px 0 0;
    }

    .latest-news-entertainment.upto-off {
        margin: 4px 0 0;
    }

    .politics-business.topnews-left {
        margin: 596px 0 0;
    }
}

@media(max-width:844px) {
    .politics-business.topnews-left {
        margin: 596px 0 0;
    }
}

/* from async body tags */
     </style>
     <link href="https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181" rel="canonical"/>
    </meta>
   </meta>
  </meta>
 </head>
 <body>
  <a aria-label="share-to" class="cd-top" href="#0" id="top">
  </a>
  <script>
   window.scrollTopFn = function(){
    window.scrollTo(0,0);
}
var elem = document.getElementsByClassName("cd-top")[0];
if(elem){
    elem.addEventListener('click', scrollTopFn , false);
}
  </script>
  <link href="https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif?width=500&amp;height=300" itemprop="thumbnailUrl"/>
  <span itemprop="thumbnail" itemscope="" itemtype="https://schema.org/ImageObject">
   <link href="https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif?width=500&amp;height=300" itemprop="url"/>
  </span>
  <script type="application/ld+json">
   {
    "@context" : "https://schema.org",
    "@type" : "Article",
    "name" : "Tupaki",  "author" : {"@type" : "Person","name" : "Tupaki Desk","url" : "https://www.tupaki.com/tupaki-desk-24124","jobTitle" : "Editor","image" : "/images/authorplaceholder.jpg?type=1&v=2","sameAs" : []},
    "datePublished" : "2024-04-23T20:18:00+05:30",
    "dateModified" : "2024-04-23T20:18:00+05:30",
    "keywords" : "Sravanthichokkarapu,Sravanthi,Tollywoodanchor,Photoshoots,Biggbosstelugu,Chokkarapu,Actressgallery", "interactivityType":"mixed","alternativeHeadline":"Stunning Photos of Sravanthi: A Must-See! | Stunning Photos of Sravanthi: A Must-See!",
    "inLanguage" : "te",
    "headline" : "Stunning Photos of Sravanthi: A Must-See!",
    "copyrightHolder" : "tupaki",
    "contentLocation" : "",
     "image" : {
      "@context" : "https://schema.org",
      "@type" : "ImageObject",
      "contentUrl" : "https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif",
      "height": 900,
      "width" : 1500,
      "url" : "https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif"
     }, "articleSection" : "Photo Gallery",
    "articleBody" : "Sravanthi Chokkarapu is a beloved figure in the film industry, known for her captivating presence both on and off the screen. Her Instagram profile is a testament to her mastery of chic style and timeless elegance. With each post, Sravanthi effortlessly steals the hearts of her followers, showcasing her impeccable fashion sense and graceful demeanor.Hailing from Hyderabad, Sravanthi pursued her bachelor's degree at the University of Auburn. Despite her busy schedule, she gracefully balances her career with her roles as a wife and mother, earning admiration for her ability to juggle multiple responsibilities. While she shares glimpses of her professional life on social media, Sravanthi remains relatively private about her personal affairs, preferring to keep them separate from the spotlight of showbiz.Recently, Sravanthi treated her fans to a stunning series of photos from a photoshoot, and they were nothing short of mesmerizing. Clad in a radiant yellow saree paired with a high-neck blouse, adorned with a bun hairstyle and flowers delicately placed on her head, Sravanthi exuded elegance and charm. Her infectious smile only added to the allure of the stylish stills, leaving her fans enamored and eagerly anticipating her next glamorous appearance.",
    "description" : "Sravanthi Chokkarapu is a beloved figure in the film industry, known for her captivating presence both on and off the screen ",
    "url" : "https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181",
    "publisher" : {
      "@type" : "Organization",
       "name" : "Tupaki",
       "url"  : "https://www.tupaki.com",
       "sameAs" : [],
       "logo" : {
          "@context" : "https://schema.org",
          "@type" : "ImageObject",
          "contentUrl" : "https://www.tupaki.com/images/logo.png",
          "height": "60",
          "width" : "600",
          "name"  : "Tupaki - Logo",
          "url" : "https://www.tupaki.com/images/logo.png"
      }
     },
      "mainEntityOfPage": {
           "@type": "WebPage",
           "@id": "https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181"
        }
  }
  </script>
  <script type="application/ld+json">
   {
    "@context" : "https://schema.org",
    "@type" : "NewsArticle",
    "name" : "Tupaki", "author" : {"@type" : "Person","name" : "Tupaki Desk","url" : "https://www.tupaki.com/tupaki-desk-24124","jobTitle" : "Editor","image" : "/images/authorplaceholder.jpg?type=1&v=2","sameAs" : []},
    "datePublished" : "2024-04-23T20:18:00+05:30",
    "dateModified" : "2024-04-23T20:18:00+05:30",
    "keywords" : "Sravanthichokkarapu,Sravanthi,Tollywoodanchor,Photoshoots,Biggbosstelugu,Chokkarapu,Actressgallery","interactivityType":"mixed","alternativeHeadline":"Stunning Photos of Sravanthi: A Must-See! | Stunning Photos of Sravanthi: A Must-See!",
    "inLanguage" : "te",
    "headline" : "Stunning Photos of Sravanthi: A Must-See!",
    "copyrightHolder" : "tupaki",
    "contentLocation" : "",
     "image" : {
      "@context" : "https://schema.org",
      "@type" : "ImageObject",
      "contentUrl" : "https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif",
      "height": 900,
      "width" : 1500,
      "url" : "https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif"
     }, "articleSection" : "Photo Gallery",
    "articleBody" : "Sravanthi Chokkarapu is a beloved figure in the film industry, known for her captivating presence both on and off the screen. Her Instagram profile is a testament to her mastery of chic style and timeless elegance. With each post, Sravanthi effortlessly steals the hearts of her followers, showcasing her impeccable fashion sense and graceful demeanor.Hailing from Hyderabad, Sravanthi pursued her bachelor's degree at the University of Auburn. Despite her busy schedule, she gracefully balances her career with her roles as a wife and mother, earning admiration for her ability to juggle multiple responsibilities. While she shares glimpses of her professional life on social media, Sravanthi remains relatively private about her personal affairs, preferring to keep them separate from the spotlight of showbiz.Recently, Sravanthi treated her fans to a stunning series of photos from a photoshoot, and they were nothing short of mesmerizing. Clad in a radiant yellow saree paired with a high-neck blouse, adorned with a bun hairstyle and flowers delicately placed on her head, Sravanthi exuded elegance and charm. Her infectious smile only added to the allure of the stylish stills, leaving her fans enamored and eagerly anticipating her next glamorous appearance.",
    "description" : "Sravanthi Chokkarapu is a beloved figure in the film industry, known for her captivating presence both on and off the screen ",
    "url" : "https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181",
    "publisher" : {
      "@type" : "Organization",
       "name" : "Tupaki",
       "url"  : "https://www.tupaki.com",
       "sameAs" : [],
       "logo" : {
          "@context" : "https://schema.org",
          "@type" : "ImageObject",
          "contentUrl" : "https://www.tupaki.com/images/logo.png",
          "height": "60",
          "width" : "600",
          "name"  : "Tupaki - Logo",
          "url" : "https://www.tupaki.com/images/logo.png"
      }
     },
      "mainEntityOfPage": {
           "@type": "WebPage",
           "@id": "https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181"
        }
  }
  </script>
  <script type="application/ld+json">
   {
    "@context" : "https://schema.org",
    "@type" : "Organization",
    "url" : "https://www.tupaki.com",
    "name" : "Tupaki",
    "sameAs" : [], 
    "logo" : {
          "@context" : "https://schema.org",
          "@type" : "ImageObject",
          "contentUrl" : "https://www.tupaki.com/images/logo.png",
          "height": "60",
          "width" : "600",
          "name"  : "Tupaki - Logo",
          "url" : "https://www.tupaki.com/images/logo.png"
    }
  }
  </script>
  <script type="application/ld+json">
   {
    "@context" : "https://schema.org",
    "@type" : "WebSite",
    "name" : "Tupaki",
    "url" : "https://www.tupaki.com",
    "author" : {
      "@type" : "Person",
      "name" : "Tupaki"
     }
   }
  </script>
  <script type="application/ld+json">
   {
    "@context" : "https://schema.org",
    "@type" : "BreadcrumbList",
    "name" : "Tupaki - BreadcrumbList",
    "itemListElement": [{ "@type":"ListItem","position":"1","item":{ "@id":"https://www.tupaki.com","@type":"Thing","name":"Home"}},{"@type":"ListItem","position":"2","item":{"@id":"https://www.tupaki.com/photogallery","@type":"WebPage","name":"Photo Gallery"}},{"@type":"ListItem","position":"3","item":{"@id":"https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181","@type":"WebPage","name":"Stunning Photos of Sravanthi: A Must-See!"}}]
  }
  </script>
  <script type="application/ld+json">
   {
    "@context" : "https://schema.org",
    "@type" : "ItemList",
    "name" : "Tupaki - ItemList",
    "itemListElement": [{"@type":"ListItem","position":"1","name":"Home","description":"Home","url":"https://www.tupaki.com/"},{"@type":"ListItem","position":"2","name":"Entertainment","description":"Entertainment","url":"https://www.tupaki.com/entertainment"},{"@type":"ListItem","position":"3","name":"Latest News","description":"Latest News","url":"https://www.tupaki.com/latest-news"},{"@type":"ListItem","position":"4","name":"Movies Reviews","description":"Movies Reviews","url":"https://www.tupaki.com/movies-reviews"},{"@type":"ListItem","position":"5","name":"Photos","description":"Photos","url":"https://www.tupaki.com/photogallery"},{"@type":"ListItem","position":"6","name":"Poll","description":"Poll","url":"https://www.tupaki.com/daily-poll"},{"@type":"ListItem","position":"7","name":"Andhrapradesh","description":"Andhrapradesh","url":"https://www.tupaki.com/andhrapradesh"},{"@type":"ListItem","position":"8","name":"Telangana","description":"Telangana","url":"https://www.tupaki.com/telangana"},{"@type":"ListItem","position":"9","name":"Life Style","description":"Life Style","url":"https://www.tupaki.com/lifestyle"},{"@type":"ListItem","position":"10","name":"Sports","description":"Sports","url":"https://www.tupaki.com/sports"}]
  }
  </script>
  <script type="application/ld+json">
   {
    "@context" : "https://schema.org",
    "@type" : "WebPage",
    "name" : "Stunning Photos of Sravanthi: A Must-See!",
    "description" : "Sravanthi Chokkarapu is a beloved figure in the film industry, known for her captivating presence both on and off the screen",
    "url" : "https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181",
    "author" : {
      "@type" : "Person",
      "name" : "Tupaki"
     },
    "publisher" : {
      "@type" : "Organization",
       "name" : "Tupaki",
       "url"  : "https://www.tupaki.com",
       "sameAs" : [],
       "logo" : {
          "@context" : "https://schema.org",
          "@type" : "ImageObject",
          "contentUrl" : "https://www.tupaki.com/images/logo.png",
          "height": "60",
          "width" : "600",
          "name"  : "Tupaki - Logo",
          "url" : "https://www.tupaki.com/images/logo.png"
      }
     }
   }
  </script>
  <script type="application/ld+json">
   {
    "@context" : "https://schema.org",
    "@type" : "ImageGallery",
    "name" : "Tupaki",
    "description" : "Sravanthi Chokkarapu is a beloved figure in the film industry, known for her captivating presence both on and off the screen ",
    "headline" : "Stunning Photos of Sravanthi: A Must-See!",
    "url" : "https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181",
    "primaryImageOfPage" : {
      "@context" : "https://schema.org",
      "@type" : "ImageObject",
      "contentUrl" : "https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif"
      },
    "associatedMedia": [{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364263-hwruvmus.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364263-hwruvmus.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364261-cjrlovqn.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364261-cjrlovqn.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364264-im0tc4s5.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364264-im0tc4s5.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364259-07ljlob0.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364259-07ljlob0.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364260-hukk4yga.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364260-hukk4yga.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364262-h9aw7plu.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364262-h9aw7plu.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364265-l32warm3.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364265-l32warm3.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364266-lvo0nds9.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364266-lvo0nds9.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364267-nbgi5rm2.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364267-nbgi5rm2.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364268-1dpmwssc.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364268-1dpmwssc.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364270-fn504zp1.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364270-fn504zp1.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364269-7xzgcvis.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364269-7xzgcvis.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364272-lf5hf7qs.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364272-lf5hf7qs.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364273-l026egmx.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364273-l026egmx.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364271-hkr8qpm1.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364271-hkr8qpm1.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364275-x5d2irzo.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364275-x5d2irzo.gif"},{"@type":"ImageObject","contentUrl":"https://content.tupaki.com/h-upload/2024/04/23/364274-pvlyq1sv.gif","thumbnailUrl":"https://content.tupaki.com/h-upload/2024/04/23/364274-pvlyq1sv.gif"}]
  }
  </script>
  <div id="fb-root">
  </div>
  <div id="content-style">
  </div>
  <div class="ui-loader-new hide">
  </div>
  <div class="hide" id="left-ad-full-screen">
  </div>
  <div class="hide" id="right-ad-full-screen">
  </div>
  <div class="hide" id="generic_ad_block_before">
  </div>
  <div class="primary-page-content-wrapper content-direction-ltr" data-categoryid="10078" data-cdnurl="" data-contentid="" data-ismobile="" data-logging-enabled="" data-newsid="1357181" data-partner="tupaki" data-path="/photogallery/sravanthichokkarapuphotoshoots-1357181" data-query-partner="tupaki" data-query-root="www.tupaki.com" data-query-sessionid="RDWEBRFGMBZX1KWO5FDPZXA5XGEE7DTNFZXY1" data-registration-mode="undefined" data-root="https://www.tupaki.com" data-sessionid="RDWEBRFGMBZX1KWO5FDPZXA5XGEE7DTNFZXY1" data-userid="" has-ga-store-key="1" id="content">
   <div class="before_content_mask">
   </div>
   <div class="page details-page-wrapper photo-gallery-details-page" id="top">
    <header>
     <nav class="navbar navbar-default navbar-fixed-top" role="navigation">
      <div class="topbar-logo">
       <div class="navbar-row">
        <div class="navbar-logo">
         <a class="navbar-brand" href="/">
          <img alt="Tupaki" class="custom-logo h-logo-img" src="/images/logo.png?v=#{env.partnerData.externalResourcesVersion}"/>
         </a>
        </div>
        <div class="navbar-right text-right">
         <div class="to-be-async-loaded-ad header_ad_1" id="header_ad_1">
         </div>
        </div>
        <div class="navbar-right text-right">
         <div class="" data-name="syncHtmlContent" id="header_social_icons">
          <div class="html_content_wrapper">
           <ul class="list-inline">
            <a href="https://www.facebook.com/Tupakiofficial" title="Like us!">
             <i class="fa fa-facebook fa-2x">
             </i>
            </a>
            <a href="https://www.instagram.com/tupaki_official/" title="Insta us!">
             <i class="fa fa-instagram fa-2x">
             </i>
            </a>
            <a href="https://twitter.com/tupaki_official" title="Tweet us!">
             <i class="fa fa-twitter fa-2x">
             </i>
            </a>
            <a href="#" title="Connect wih us!">
             <i class="fa fa-linkedin fa-2x">
             </i>
            </a>
            <a href="#" title="Code with us!">
             <i class="fa fa-snapchat fa-2x">
             </i>
            </a>
            <a href="https://www.youtube.com/@tupakipolitical8524?themeRefresh=1" title='Youtube"'>
             <i class="fab fa-youtube fa-2x">
             </i>
            </a>
           </ul>
          </div>
         </div>
        </div>
        <div class="navbar-right text-right">
         <div class="to-be-async-loaded-ad header_btn" id="header_btn">
         </div>
         <button class="navbar-toggle collapsed" data-target="#search" data-toggle="collapse" type="button">
          <i class="fa fa-search">
          </i>
         </button>
         <form action="/" class="navbar-form hidden-xs" method="GET" role="search">
          <div class="input-group">
           <!-- <input type="text" class="form-control" placeholder="Search"/>-->
           <span class="input-group-btn">
            <button class="btn btn-primary" type="button">
             <i class="fa fa-search">
             </i>
            </button>
           </span>
          </div>
         </form>
         <div class="sidenav" id="mySidenav">
          <a aria-label="close btn" class="closebtn" href="javascript:void(0)">
           <svg class="css-i6dzq1" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24">
            <circle cx="12" cy="12" r="10">
            </circle>
            <line x1="15" x2="9" y1="9" y2="15">
            </line>
            <line x1="9" x2="15" y1="9" y2="15">
            </line>
           </svg>
          </a>
          <div class="dropdown-container">
           <div class="accordion">
            <div class="accordion__item">
             <a class="accordion__btn" href="/">
              <span class="accordion__caption">
               Home
              </span>
             </a>
            </div>
            <div class="accordion__item">
             <a class="accordion__btn" href="/entertainment">
              <span class="accordion__caption">
               Entertainment
              </span>
             </a>
            </div>
            <div class="accordion__item">
             <a class="accordion__btn" href="/latest-news">
              <span class="accordion__caption">
               Latest News
              </span>
             </a>
            </div>
            <div class="accordion__item">
             <a class="accordion__btn" href="/movies-reviews">
              <span class="accordion__caption">
               Movies Reviews
              </span>
             </a>
            </div>
            <div class="accordion__item active">
             <a class="accordion__btn" href="/photogallery">
              <span class="accordion__caption">
               Photos
              </span>
             </a>
            </div>
            <div class="accordion__item">
             <a class="accordion__btn" href="/daily-poll">
              <span class="accordion__caption">
               Poll
              </span>
             </a>
            </div>
            <div class="accordion__item">
             <button class="accordion__btn has-sub-menu">
              <a href="/andhrapradesh">
               <span class="accordion__caption">
                Andhrapradesh
               </span>
              </a>
              <i class="fa fa-angle-down">
              </i>
             </button>
             <div class="accordion header-sub-menu hide">
              <div class="accordion__item">
               <a class="accordion__btn" href="/andhrapradesh/anantapur">
                <span class="accordion__caption">
                 Anantapuramu
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/annamayya">
                <span class="accordion__caption">
                 Annamayya
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/anakapalli">
                <span class="accordion__caption">
                 Anakapalli
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/alluri-sitharama-raju">
                <span class="accordion__caption">
                 Alluri Sitharama Raju
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/bapatla">
                <span class="accordion__caption">
                 Bapatla
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="">
                <span class="accordion__caption">
                 Dr.B.R.Ambedkar Konaseema
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/eluru">
                <span class="accordion__caption">
                 Eluru
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/kakinada">
                <span class="accordion__caption">
                 Kakinada
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/ntr">
                <span class="accordion__caption">
                 NTR
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/nandyal">
                <span class="accordion__caption">
                 Nandyal
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/parvathipuram-manyam">
                <span class="accordion__caption">
                 Parvathipuram Manyam
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/palnadu">
                <span class="accordion__caption">
                 Palnadu
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/potti-sriramulu-nellore">
                <span class="accordion__caption">
                 Sri Potti Sriramulu Nellore
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/sri-athya-sai">
                <span class="accordion__caption">
                 Sri Sathya Sai
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/tirupati">
                <span class="accordion__caption">
                 Tirupati
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/andhrapradesh/chittoor">
                <span class="accordion__caption">
                 Chittoor
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/andhrapradesh/east-godavari">
                <span class="accordion__caption">
                 East Godavari
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/andhrapradesh/guntur">
                <span class="accordion__caption">
                 Guntur
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/andhrapradesh/ysr-kadapa">
                <span class="accordion__caption">
                 YSR
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/andhrapradesh/krishna">
                <span class="accordion__caption">
                 Krishna
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/andhrapradesh/kurnool">
                <span class="accordion__caption">
                 Kurnool
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/potti-sriramulu-nellore">
                <span class="accordion__caption">
                 Nellore
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/andhrapradesh/srikakulam">
                <span class="accordion__caption">
                 Srikakulam
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/andhrapradesh/visakhapatnam">
                <span class="accordion__caption">
                 Visakhapatnam
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/andhrapradesh/vizianagaram">
                <span class="accordion__caption">
                 Vizianagaram
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/andhrapradesh/west-godavari">
                <span class="accordion__caption">
                 West Godavari
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/andhrapradesh/prakasam">
                <span class="accordion__caption">
                 Prakasam
                </span>
               </a>
              </div>
             </div>
            </div>
            <div class="accordion__item">
             <button class="accordion__btn has-sub-menu">
              <a href="/telangana">
               <span class="accordion__caption">
                Telangana
               </span>
              </a>
              <i class="fa fa-angle-down">
              </i>
             </button>
             <div class="accordion header-sub-menu hide">
              <div class="accordion__item">
               <a class="accordion__btn" href="/telangana/adilabad">
                <span class="accordion__caption">
                 Adilabad
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/telangana/hyderabad">
                <span class="accordion__caption">
                 Hyderabad
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/telangana/karimnagar">
                <span class="accordion__caption">
                 karimnagar
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/telangana/khammam">
                <span class="accordion__caption">
                 Khammam
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/telangana/mahabubnagar">
                <span class="accordion__caption">
                 Mahabubnagar
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/telangana/medak">
                <span class="accordion__caption">
                 Medak
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/telangana/nalgonda">
                <span class="accordion__caption">
                 Nalgonda
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/telangana/nizamabad">
                <span class="accordion__caption">
                 Nizamabad
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/telangana/ranga-reddy">
                <span class="accordion__caption">
                 Ranga Reddy
                </span>
               </a>
              </div>
              <div class="accordion__item">
               <a class="accordion__btn" href="/telangana/warangal-rural">
                <span class="accordion__caption">
                 Warangal Rural
                </span>
               </a>
              </div>
             </div>
            </div>
           </div>
          </div>
         </div>
         <span class="side-svg ham-btn">
          <svg class="css-i6dzq1" fill="#fff" height="40" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="40">
           <line x1="21" x2="7" y1="10" y2="10">
           </line>
           <line x1="21" x2="3" y1="6" y2="6">
           </line>
           <line x1="21" x2="3" y1="14" y2="14">
           </line>
           <line x1="21" x2="7" y1="18" y2="18">
           </line>
          </svg>
         </span>
        </div>
       </div>
      </div>
      <div class="container-fluid">
       <div class="navbar-header">
        <div class="hide" id="navbar_toggle">
        </div>
       </div>
       <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
         <li>
          <a href="/">
           Home
          </a>
         </li>
         <li>
          <a href="/entertainment">
           Entertainment
          </a>
         </li>
         <li>
          <a href="/latest-news">
           News
          </a>
         </li>
         <li>
          <a href="/movies-reviews">
           Movies Reviews
          </a>
         </li>
         <li>
          <a href="/photogallery">
           Photos
          </a>
         </li>
         <li>
          <a href="/andhrapradesh">
           Andhra Pradesh
          </a>
         </li>
         <li>
          <a href="/telangana">
           Telangana
          </a>
         </li>
         <li>
          <a href="/lifestyle">
           Life Style
          </a>
         </li>
         <li>
          <a href="/sports">
           Sports
          </a>
         </li>
        </ul>
       </div>
      </div>
      <div class="topbar">
       <div class="container-fluid">
        <div class="tabbar-fluid">
         <button aria-controls="menu-top" aria-expanded="false" class="btn btn-primary second_menu" data-target="#menu-top" data-toggle="collapse" type="button">
          <i class="fa fa-bars">
          </i>
         </button>
         <div class="collapse in" id="menu-top">
          <ul>
           <li>
            <a href="https://www.tupaki.com/tags/Puspa2">
             #Puspa2
            </a>
           </li>
           <li>
            <a href="https://www.tupaki.com/tags/AlluArjun">
             #AlluArjun
            </a>
           </li>
           <li>
            <a href="https://www.tupaki.com/tags/Pushpa2collections">
             #Pushpa2collections
            </a>
           </li>
           <li>
            <a href="https://www.tupaki.com/tags/Sandhyatheater">
             #Sandhyatheater
            </a>
           </li>
           <li>
            <a href="https://www.tupaki.com/tags/RashmikaMandana">
             #RashmikaMandana
            </a>
           </li>
           <li>
            <a href="https://www.tupaki.com/tags/RevanthReddy">
             #RevanthReddy
            </a>
           </li>
           <li>
            <a href="https://www.tupaki.com/tags/GameChanger">
             #GameChanger
            </a>
           </li>
           <li>
            <a href="https://www.tupaki.com/tags/ManchuFamily">
             #ManchuFamily
            </a>
           </li>
          </ul>
         </div>
        </div>
       </div>
      </div>
     </nav>
    </header>
    <div class="search-area" display="block">
     <div class="close-btn">
      <button class="btn btn-lg m-3 close">
       <img data-src="/images/clear-button-white.png"/>
      </button>
     </div>
     <div class="form">
      <div class="input-group form-btn">
       <input aria-describedby="button-addon2" aria-label="Search bar" class="form-control search-text-value" id="search-input-box" placeholder="Search here..." type="text"/>
       <div class="input-group-append">
        <button class="btn btn-outline-light brd-left-none border-bottom1 search-now-btn" id="button-addon2" type="button">
         <span aria-hidden="true" class="icon-search">
          <img data-src="/images/search.png"/>
         </span>
        </button>
       </div>
      </div>
      <small class="text-white pt-3 search-caption">
       Begin typing your search above and press return to search.
      </small>
     </div>
    </div>
    <div class="hide" id="ad_after_header">
    </div>
    <div class="hide" id="ad_after_header2">
    </div>
    <section class="website-wrapper py-4 py-sm-5">
     <div class="to-be-async-loaded-ad detail_wrap_ad_1" id="detail_wrap_ad_1">
     </div>
     <div class="live-ads">
      <div class="hide" id="left_sticky_ad">
      </div>
     </div>
     <div class="hide" id="detail_wrap_ad_2">
     </div>
     <div class="live-tabs">
      <section class="ads-slider py-4 py-sm-5">
       <div class="hide" id="level_1">
       </div>
      </section>
      <div class="breadcrumbs sub-flex">
       <ul>
        <li class="breadcrumb-item">
         <a class="bread-home" href="/">
          Home
         </a>
         <svg class="css-i6dzq1" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24">
          <polyline points="9 18 15 12 9 6">
          </polyline>
         </svg>
        </li>
        <li class="breadcrumb-item">
         <a class="bread-link" href="/photogallery">
          <span>
           Photo Gallery
          </span>
         </a>
        </li>
       </ul>
      </div>
      <div class="hide" id="detail_wrap_ad_3">
      </div>
      <div class="andhra-content political-news">
       <div class="andhra-pradesh">
        <div class="content-flex">
         <div class="details-page" id="post-content-wrapper">
          <div class="to-be-async-loaded-ad left_level_1" id="left_level_1">
          </div>
          <h1 class="h-news-heading">
           Stunning Photos of Sravanthi: A Must-See!
          </h1>
          <h2 class="h-news-desc">
           Sravanthi Chokkarapu is a beloved figure in the film industry, known for her captivating presence both on and off the screen
          </h2>
          <span>
           <span>
            By:
           </span>
           <a class="author-link h-author-internal-block author-name news-by-author-1357181 news-by-author icon-link" href="/tupaki-desk-24124">
            Tupaki Desk
           </a>
           <span>
            |
           </span>
          </span>
          <span class="date new-line-in-mobile margin-left-desktop">
           <span class="convert-to-localtime" data-datestring="2024-04-23 14:48:00">
            23 April 2024 2:48 PM GMT
           </span>
          </span>
          <div class="share">
           <span>
            Share:
           </span>
           <div class="SocialShares inline color small social-share-advance-wrap">
            <!-- | !{hide_social_networks}-->
            <style>
             /* link copied popup */
#modal-content{
    height: fit-content;
}

.modal_wrapper_frame #modal-content .view-content{
    text-align: center;
}
.modal_wrapper_frame #modal-content .view-content h3{
    margin-top: 10px;
}
/* end */
.link.active a{
    background:#ccc !important;
}
.ind-social-li{cursor:pointer;}

.inline .ind-social-cover .ind-social-ul .ind-social-li{
    display:inline-block;
}
.ind-social-cover{
    position: relative;
}
.ind-social-cover .ind-social-ul{
    padding:0px;
    top:0px;
}

/*====for-vertical-and-horizontal-start======*/

.ind-social-cover .ind-social-ul.ind-horizontal .ind-social-li{
    display: inline-block;
    margin-right: 7px;
    min-width: 55px;
}

.ind-social-cover .ind-social-ul.ind-vertical .ind-social-li{
    display: block;
    margin-right: 7px;
    min-width: 55px;
}

/*====for-vertical-and-horizontal-end======*/

.ind-social-cover .ind-social-ul .ind-social-li{
    list-style-type: none;
    text-align: center;
}

.ind-social-cover .ind-social-ul .ind-social-li{
    margin-bottom: 7px;
}

.ind-social-cover .ind-social-ul .ind-social-li .ind-social-click{
    text-decoration: none;
    display: inline-block;
    width:40px;
    height:40px;
    background-color: #e7e8e9;
    position: relative;
    border-radius: 50%;
    border:1px solid #e7e8e9;
    overflow: hidden;
}
.small .ind-social-cover .ind-social-ul .ind-social-li .ind-social-click{
    width:30px;
    height:30px;
}
/*=====for-size-change-start=====*/

.small .ind-social-cover .ind-social-ul .ind-social-li .ind-social-click{
    width:30px;
    height:30px;
}
.small .ind-social-cover .ind-social-ul .ind-social-li .ind-social-click svg{
    width:15px;
    height:15px;
}

.ind-social-cover .ind-social-ul.ind-large .ind-social-li .ind-social-click{
    width:50px;
    height:50px;
}
.ind-social-cover .ind-social-ul.ind-large .ind-social-li .ind-social-click svg{
    width:20px;
    height:20px;
}

/*=====for-size-change-end=====*/

.ind-social-cover .ind-social-ul .ind-social-li .ind-social-click svg{
    position: absolute;
    left:50%;
    top:50%;
    transform:translate(-50%, -50%);
    width:18px;
    height: 18px;
}

.ind-social-cover .ind-social-ul.s-hide{
    display: none;
}
.ind-social-cover .ind-social-ul.dark-mode,.ind-social-cover .ind-social-ul.color-mode{
    display:none;
}
.dark .ind-social-cover .ind-social-ul.dark-mode{
    display:inline-block;
}
.dark .ind-social-cover .ind-social-ul.color-mode,.dark .ind-social-cover .ind-social-ul.light-mode{
    display:none;
}
.color .ind-social-cover .ind-social-ul.color-mode{
    display:inline-block;
}
.color .ind-social-cover .ind-social-ul.dark-mode,.color .ind-social-cover .ind-social-ul.light-mode{
    display:none;
}

.light .ind-social-cover .ind-social-ul.light-mode{
    display:inline-block;
}
.light .ind-social-cover .ind-social-ul.dark-mode,.light .ind-social-cover .ind-social-ul.color-mode{
    display:none;
}
.ind-social-cover .ind-social-ul .ind-social-li .ind-social-click.ind-fb-bg{
    background-color: #3b5998;
}
.ind-social-cover .ind-social-ul .ind-social-li .ind-social-click.ind-twt-bg{
    background-color: #000000;
}
.ind-social-cover .ind-social-ul .ind-social-li .ind-social-click.ind-whatsapp-bg{
    background-color: #25d366;
}
.ind-social-cover .ind-social-ul .ind-social-li .ind-social-click.ind-tele-bg{
    background-color: #0088cc;
}
.ind-social-cover .ind-social-ul .ind-social-li .ind-social-click.ind-linked-bg{
    background-color: #0e76a8;
}
.ind-social-cover .ind-social-ul .ind-social-li .ind-social-click.ind-mail-bg{
    background-color: #ccaa5a;
}
.ind-social-cover .ind-social-ul .ind-social-li .ind-social-click.ind-print-bg{
    background-color: #13c5c5;
}

.ind-s-lable{
    font-size: 12px;
    display: none;
}
.dark{
    background-color: #000;
}
.dark .ind-s-lable{
    color:#fff;
}
.hide-social-label .ind-s-lable{
    display:none;
}
.small-social-icons .ind-social-cover .ind-social-ul .ind-social-li{
    min-width:40px;
    margin-right: 0px;
}
.small-social-icons .ind-social-cover .ind-social-ul .ind-social-li .ind-social-click svg{
    width: 15px;
    height: 15px;
}
.ind-social-cover .ind-social-ul{
    width:100%;
    text-align:center;
}
.small-social-icons .ind-social-cover .ind-social-ul .ind-social-li .ind-social-click{
    width: 30px;
    height: 30px;
}
.ind-social-cover .ind-social-ul .ind-social-li .ind-social-click.bg-none{
    background: transparent;
}

.ind-social-cover .ind-social-ul.ind-horizontal .ind-s-lable{
    display: block;
}

.ind-social-cover .ind-social-ul.ind-vertical .ind-s-lable{
    display: block;
}

.ind-social-ul.ind-override .ind-social-li .ind-social-click{
    border: 1px solid #000;
}

.dark .ind-social-ul.ind-override .ind-social-li .ind-social-click{
    border: 1px solid #fff;
}

@media (max-width:1024px){
    .ind-social-cover .ind-social-ul.ind-horizontal{
        position: static;
    }
    
    .ind-social-cover .ind-social-ul.ind-vertical{
        position: absolute;
        left: 0px;
    }
    .ind-social-cover .ind-social-ul{
        position: static;
    }
    .ind-social-cover .ind-social-ul .ind-social-li{
        display: inline-block;
        margin-right: 7px;
        min-width: 55px;
    }
    .ind-social-cover .ind-social-ul.ind-horizontal .ind-social-li{
        display: inline-block;
        margin-right: 7px;
        min-width: 55px;
    }
    .ind-social-cover .ind-social-ul.ind-vertical .ind-social-li{
        display: block;
        margin-right: 7px;
        min-width: 55px;
    }
    .ind-s-lable{
        display: block;
    }
    .ind-social-cover .ind-social-ul.ind-horizontal .ind-s-lable{
        display: block;
    }
    .ind-social-cover .ind-social-ul.ind-vertical .ind-s-lable{
        display: block;
    }
    
    /*=====for-size-change-on-mobile======*/
    
    .ind-social-cover .ind-social-ul.ind-large .ind-social-li .ind-social-click{
        width:30px;
        height:30px;
    }
    .ind-social-cover .ind-social-ul.ind-large .ind-social-li .ind-social-click svg{
        width:16px;
        height:16px;
    }
}

.dark .ind-override.ind-social-ul svg path{
    fill: #fff;
}

.ind-social-cover .ind-social-ul.ind-horizontal{
    position: static;
}

.ind-social-cover .ind-social-ul.ind-vertical{
    position: absolute;
}

@media (max-width: 640px){
    .ind-social-cover .ind-social-ul .ind-social-li .ind-social-click{
        width: 30px;
        height: 30px;
        margin-top:5px;
    }
    .ind-social-cover .ind-social-ul .ind-social-li{
        margin-right: 0px;
        min-width: 40px;
    }
    .ind-s-lable{
        display: none;
    }
    .author-date-space-bar{
        display: none;
    }
    .date-on-article{
        display: block;
    }
}
.social-sticky a{
    margin-bottom:0;
}
.koo a svg{
    height:30px !important;
    width:30px !important;
}
.ind-social-cover .ind-social-ul .ind-social-li .ind-social-click.ind-koo-bg{
    background-color:#fbd051;
}
@media print {
  .h-share-top-parent-wrap,.ind-social-wrapper{
    display: none;
  }
}
            </style>
            <div class="ind-social-wrapper">
             <div class="ind-social-cover">
              <!-- =======normal-mode==========-->
              <div class="ind-social-ul dark-mode">
               <span class="ind-social-li facebook">
                <a class="ind-social-click" href="https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181" target="_blank">
                 <svg enable-background="new 0 0 24 24" height="24" id="Bold" viewbox="0 0 24 24" width="24" xmlns="https://www.w3.org/2000/svg">
                  <path d="m15.997 3.985h2.191v-3.816c-.378-.052-1.678-.169-3.192-.169-3.159 0-5.323 1.987-5.323 5.639v3.361h-3.486v4.266h3.486v10.734h4.274v-10.733h3.345l.531-4.266h-3.877v-2.939c.001-1.233.333-2.077 2.051-2.077z">
                  </path>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li twitter">
                <a class="ind-social-click" href="https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181&amp;text=Stunning%20Photos%20of%20Sravanthi%3A%20A%20Must-See!" target="_blank">
                 <svg class="new-twitter-white-icon" id="Capa_1" viewbox="0 0 24 24" xmlns="https://www.w3.org/2000/svg">
                  <g>
                   <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z">
                   </path>
                  </g>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li whatsapp">
                <a class="ind-social-click custom-desktop-whatsapp" href="https://api.whatsapp.com/send?text=Stunning%20Photos%20of%20Sravanthi%3A%20A%20Must-See!%20https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181%20%0A%20%0A" target="_blank">
                 <svg id="Capa_1" viewbox="0 0 52 52" xmlns="https://www.w3.org/2000/svg">
                  <path d="M26,0C11.663,0,0,11.663,0,26c0,4.891,1.359,9.639,3.937,13.762C2.91,43.36,1.055,50.166,1.035,50.237                        c-0.096,0.352,0.007,0.728,0.27,0.981c0.263,0.253,0.643,0.343,0.989,0.237L12.6,48.285C16.637,50.717,21.26,52,26,52                        c14.337,0,26-11.663,26-26S40.337,0,26,0z M26,50c-4.519,0-8.921-1.263-12.731-3.651c-0.161-0.101-0.346-0.152-0.531-0.152                        c-0.099,0-0.198,0.015-0.294,0.044l-8.999,2.77c0.661-2.413,1.849-6.729,2.538-9.13c0.08-0.278,0.035-0.578-0.122-0.821                        C3.335,35.173,2,30.657,2,26C2,12.767,12.767,2,26,2s24,10.767,24,24S39.233,50,26,50z">
                  </path>
                  <path d="M42.985,32.126c-1.846-1.025-3.418-2.053-4.565-2.803c-0.876-0.572-1.509-0.985-1.973-1.218                        c-1.297-0.647-2.28-0.19-2.654,0.188c-0.047,0.047-0.089,0.098-0.125,0.152c-1.347,2.021-3.106,3.954-3.621,4.058                        c-0.595-0.093-3.38-1.676-6.148-3.981c-2.826-2.355-4.604-4.61-4.865-6.146C20.847,20.51,21.5,19.336,21.5,18                        c0-1.377-3.212-7.126-3.793-7.707c-0.583-0.582-1.896-0.673-3.903-0.273c-0.193,0.039-0.371,0.134-0.511,0.273                        c-0.243,0.243-5.929,6.04-3.227,13.066c2.966,7.711,10.579,16.674,20.285,18.13c1.103,0.165,2.137,0.247,3.105,0.247                        c5.71,0,9.08-2.873,10.029-8.572C43.556,32.747,43.355,32.331,42.985,32.126z M30.648,39.511                        c-10.264-1.539-16.729-11.708-18.715-16.87c-1.97-5.12,1.663-9.685,2.575-10.717c0.742-0.126,1.523-0.179,1.849-0.128                        c0.681,0.947,3.039,5.402,3.143,6.204c0,0.525-0.171,1.256-2.207,3.293C17.105,21.48,17,21.734,17,22c0,5.236,11.044,12.5,13,12.5                        c1.701,0,3.919-2.859,5.182-4.722c0.073,0.003,0.196,0.028,0.371,0.116c0.36,0.181,0.984,0.588,1.773,1.104                        c1.042,0.681,2.426,1.585,4.06,2.522C40.644,37.09,38.57,40.701,30.648,39.511z">
                  </path>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li telegram">
                <a class="ind-social-click" href="https://t.me/share/url?url=https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181&amp;text=Stunning%20Photos%20of%20Sravanthi%3A%20A%20Must-See!" target="_blank">
                 <svg enable-background="new 0 0 24 24" height="512" id="Bold" viewbox="0 0 24 24" width="512" xmlns="https://www.w3.org/2000/svg">
                  <path d="m9.417 15.181-.397 5.584c.568 0 .814-.244 1.109-.537l2.663-2.545 5.518 4.041c1.012.564 1.725.267 1.998-.931l3.622-16.972.001-.001c.321-1.496-.541-2.081-1.527-1.714l-21.29 8.151c-1.453.564-1.431 1.374-.247 1.741l5.443 1.693 12.643-7.911c.595-.394 1.136-.176.691.218z">
                  </path>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li linkedin">
                <a aria-label="Linkedin" class="ind-social-click" href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181&amp;title=Stunning Photos of Sravanthi: A Must-See!" target="_blank" title="LinkedIn">
                 <svg enable-background="new 0 0 24 24" height="512" id="Bold" viewbox="0 0 24 24" width="512" xmlns="https://www.w3.org/2000/svg">
                  <path d="m23.994 24v-.001h.006v-8.802c0-4.306-.927-7.623-5.961-7.623-2.42 0-4.044 1.328-4.707 2.587h-.07v-2.185h-4.773v16.023h4.97v-7.934c0-2.089.396-4.109 2.983-4.109 2.549 0 2.587 2.384 2.587 4.243v7.801z">
                  </path>
                  <path d="m.396 7.977h4.976v16.023h-4.976z">
                  </path>
                  <path d="m2.882 0c-1.591 0-2.882 1.291-2.882 2.882s1.291 2.909 2.882 2.909 2.882-1.318 2.882-2.909c-.001-1.591-1.292-2.882-2.882-2.882z">
                  </path>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li email">
                <span class="ind-social-click js-share-article-by-email-direct" data-domain="https://www.tupaki.com" data-href="mailto:?subject=#{encodeURIComponent('Check this out - '+title)}&amp;body=Stunning%20Photos%20of%20Sravanthi%3A%20A%20Must-See!%20%20%20https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181" data-title="Stunning Photos of Sravanthi: A Must-See!" data-url="https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181" href="javascript:void(0);" title="Share by Email">
                 <svg id="Capa_1" viewbox="0 0 230.17 230.17" xmlns="https://www.w3.org/2000/svg">
                  <path d="M230,49.585c0-0.263,0.181-0.519,0.169-0.779l-70.24,67.68l70.156,65.518c0.041-0.468-0.085-0.94-0.085-1.418V49.585z">
                  </path>
                  <path d="M149.207,126.901l-28.674,27.588c-1.451,1.396-3.325,2.096-5.2,2.096c-1.836,0-3.672-0.67-5.113-2.013l-28.596-26.647                        L11.01,195.989c1.717,0.617,3.56,1.096,5.49,1.096h197.667c2.866,0,5.554-0.873,7.891-2.175L149.207,126.901z">
                  </path>
                  <path d="M115.251,138.757L222.447,35.496c-2.427-1.443-5.252-2.411-8.28-2.411H16.5c-3.943,0-7.556,1.531-10.37,3.866                        L115.251,138.757z">
                  </path>
                  <path d="M0,52.1v128.484c0,1.475,0.339,2.897,0.707,4.256l69.738-67.156L0,52.1z">
                  </path>
                 </svg>
                </span>
               </span>
               <span class="ind-social-li link">
                <div class="forcopy" data-content="https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181" data-url="https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181">
                 <a aria-label="link" class="ind-social-click ind-link-bg bg-none" href="javascript:void(0)">
                  <svg height="425.467px" id="Capa_1" style="enable-background:new 0 0 425.466 425.467;" version="1.1" viewbox="0 0 425.466 425.467" width="425.466px" x="0px" xml:space="preserve" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink" y="0px">
                   <g>
                    <g>
                     <g>
                      <path d="M318.15,230.195l77.934-77.937c31.894-31.892,31.894-83.782-0.004-115.674l-12.66-12.66     c-31.893-31.896-83.78-31.896-115.674-0.004l-77.937,77.934c-17.588,17.588-25.457,41.264-23.646,64.311     c-23.045-1.813-46.722,6.056-64.308,23.647L23.92,267.748c-31.894,31.889-31.894,83.779,0,115.674l12.664,12.662     c31.893,31.893,83.783,31.893,115.674,0l77.935-77.936c17.592-17.59,25.459-41.266,23.647-64.309     C276.884,255.654,300.56,247.783,318.15,230.195z M202.653,290.605l-77.936,77.938c-16.705,16.703-43.889,16.703-60.59,0     l-12.666-12.666c-16.705-16.701-16.703-43.885,0-60.594l77.936-77.932c14.14-14.141,35.779-16.306,52.226-6.516l-32.302,32.307     c-7.606,7.604-7.606,19.938,0,27.541c7.605,7.607,19.937,7.607,27.541,0l32.306-32.303     C218.959,254.828,216.795,276.469,202.653,290.605z M238.382,209.169l32.299-32.306c7.608-7.602,7.608-19.935,0-27.538     c-7.604-7.61-19.936-7.61-27.541-0.004l-32.303,32.303c-9.791-16.446-7.627-38.087,6.514-52.226l77.935-77.935     c16.707-16.707,43.89-16.707,60.594,0l12.664,12.664c16.705,16.705,16.705,43.886,0,60.591l-77.936,77.937     C276.468,216.797,254.828,218.959,238.382,209.169z">
                      </path>
                     </g>
                    </g>
                   </g>
                  </svg>
                 </a>
                </div>
               </span>
              </div>
              <!-- ========dark-mode==========-->
              <div class="ind-social-ul ind-override light-mode">
               <span class="ind-social-li facebook">
                <a aria-label="facebook" class="ind-social-click bg-none" href="https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181" target="_blank">
                 <svg enable-background="new 0 0 24 24" height="24" id="Bold" viewbox="0 0 24 24" width="24" xmlns="https://www.w3.org/2000/svg">
                  <path d="m15.997 3.985h2.191v-3.816c-.378-.052-1.678-.169-3.192-.169-3.159 0-5.323 1.987-5.323 5.639v3.361h-3.486v4.266h3.486v10.734h4.274v-10.733h3.345l.531-4.266h-3.877v-2.939c.001-1.233.333-2.077 2.051-2.077z" fill="#000">
                  </path>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li twitter">
                <a aria-label="twitter" class="ind-social-click bg-none" href="https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181&amp;text=Stunning%20Photos%20of%20Sravanthi%3A%20A%20Must-See!" target="_blank">
                 <svg id="Capa_1" viewbox="0 0 24 24" xmlns="https://www.w3.org/2000/svg">
                  <g>
                   <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z">
                   </path>
                  </g>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li whatsapp">
                <a aria-label="whatsapp" class="ind-social-click bg-none" href="https://api.whatsapp.com/send?text=Stunning%20Photos%20of%20Sravanthi%3A%20A%20Must-See!%20https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181%20%0A%20%0A" target="_blank">
                 <svg id="Capa_1" viewbox="0 0 512 512" xmlns="https://www.w3.org/2000/svg">
                  <path d="M256.064,0h-0.128C114.784,0,0,114.816,0,256c0,56,18.048,107.904,48.736,150.048l-31.904,95.104l98.4-31.456                        C155.712,496.512,204,512,256.064,512C397.216,512,512,397.152,512,256S397.216,0,256.064,0z M405.024,361.504                        c-6.176,17.44-30.688,31.904-50.24,36.128c-13.376,2.848-30.848,5.12-89.664-19.264C189.888,347.2,141.44,270.752,137.664,265.792                        c-3.616-4.96-30.4-40.48-30.4-77.216s18.656-54.624,26.176-62.304c6.176-6.304,16.384-9.184,26.176-9.184                        c3.168,0,6.016,0.16,8.576,0.288c7.52,0.32,11.296,0.768,16.256,12.64c6.176,14.88,21.216,51.616,23.008,55.392                        c1.824,3.776,3.648,8.896,1.088,13.856c-2.4,5.12-4.512,7.392-8.288,11.744c-3.776,4.352-7.36,7.68-11.136,12.352                        c-3.456,4.064-7.36,8.416-3.008,15.936c4.352,7.36,19.392,31.904,41.536,51.616c28.576,25.44,51.744,33.568,60.032,37.024                        c6.176,2.56,13.536,1.952,18.048-2.848c5.728-6.176,12.8-16.416,20-26.496c5.12-7.232,11.584-8.128,18.368-5.568                        c6.912,2.4,43.488,20.48,51.008,24.224c7.52,3.776,12.48,5.568,14.304,8.736C411.2,329.152,411.2,344.032,405.024,361.504z" fill="#000">
                  </path>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li telegram">
                <a class="ind-social-click bg-none" href="https://t.me/share/url?url=https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181&amp;text=Stunning%20Photos%20of%20Sravanthi%3A%20A%20Must-See!" target="_blank">
                 <svg enable-background="new 0 0 24 24" height="512" id="Bold" viewbox="0 0 24 24" width="512" xmlns="https://www.w3.org/2000/svg">
                  <path d="m9.417 15.181-.397 5.584c.568 0 .814-.244 1.109-.537l2.663-2.545 5.518 4.041c1.012.564 1.725.267 1.998-.931l3.622-16.972.001-.001c.321-1.496-.541-2.081-1.527-1.714l-21.29 8.151c-1.453.564-1.431 1.374-.247 1.741l5.443 1.693 12.643-7.911c.595-.394 1.136-.176.691.218z" fill="#000">
                  </path>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li linkedin">
                <a aria-label="Linkedin" class="ind-social-click bg-none" href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181&amp;title=Stunning Photos of Sravanthi: A Must-See!" target="_blank" title="LinkedIn">
                 <svg enable-background="new 0 0 24 24" height="512" id="Bold" viewbox="0 0 24 24" width="512" xmlns="https://www.w3.org/2000/svg">
                  <path d="m23.994 24v-.001h.006v-8.802c0-4.306-.927-7.623-5.961-7.623-2.42 0-4.044 1.328-4.707 2.587h-.07v-2.185h-4.773v16.023h4.97v-7.934c0-2.089.396-4.109 2.983-4.109 2.549 0 2.587 2.384 2.587 4.243v7.801z" fill="#000">
                  </path>
                  <path d="m.396 7.977h4.976v16.023h-4.976z" fill="#000">
                  </path>
                  <path d="m2.882 0c-1.591 0-2.882 1.291-2.882 2.882s1.291 2.909 2.882 2.909 2.882-1.318 2.882-2.909c-.001-1.591-1.292-2.882-2.882-2.882z" fill="#000">
                  </path>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li email">
                <span class="ind-social-click bg-none js-share-article-by-email-direct" data-domain="https://www.tupaki.com" data-href="mailto:?subject=#{encodeURIComponent('Check this out - '+title)}&amp;body=Stunning%20Photos%20of%20Sravanthi%3A%20A%20Must-See!%20%20%20https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181" data-title="Stunning Photos of Sravanthi: A Must-See!" data-url="https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181" href="javascript:void(0);" title="Share by Email">
                 <svg id="Capa_1" viewbox="0 0 230.17 230.17" xmlns="https://www.w3.org/2000/svg">
                  <path d="M230,49.585c0-0.263,0.181-0.519,0.169-0.779l-70.24,67.68l70.156,65.518c0.041-0.468-0.085-0.94-0.085-1.418V49.585z" fill="#000">
                  </path>
                  <path d="M149.207,126.901l-28.674,27.588c-1.451,1.396-3.325,2.096-5.2,2.096c-1.836,0-3.672-0.67-5.113-2.013l-28.596-26.647                        L11.01,195.989c1.717,0.617,3.56,1.096,5.49,1.096h197.667c2.866,0,5.554-0.873,7.891-2.175L149.207,126.901z" fill="#000">
                  </path>
                  <path d="M115.251,138.757L222.447,35.496c-2.427-1.443-5.252-2.411-8.28-2.411H16.5c-3.943,0-7.556,1.531-10.37,3.866                        L115.251,138.757z" fill="#000">
                  </path>
                  <path d="M0,52.1v128.484c0,1.475,0.339,2.897,0.707,4.256l69.738-67.156L0,52.1z" fill="#000">
                  </path>
                 </svg>
                </span>
               </span>
               <span class="ind-social-li link">
                <div class="forcopy" data-content="https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181" data-url="https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181">
                 <a aria-label="link" class="ind-social-click ind-link-bg bg-none" href="javascript:void(0)">
                  <svg height="425.467px" id="Capa_1" style="enable-background:new 0 0 425.466 425.467;" version="1.1" viewbox="0 0 425.466 425.467" width="425.466px" x="0px" xml:space="preserve" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink" y="0px">
                   <g>
                    <g>
                     <g>
                      <path d="M318.15,230.195l77.934-77.937c31.894-31.892,31.894-83.782-0.004-115.674l-12.66-12.66     c-31.893-31.896-83.78-31.896-115.674-0.004l-77.937,77.934c-17.588,17.588-25.457,41.264-23.646,64.311     c-23.045-1.813-46.722,6.056-64.308,23.647L23.92,267.748c-31.894,31.889-31.894,83.779,0,115.674l12.664,12.662     c31.893,31.893,83.783,31.893,115.674,0l77.935-77.936c17.592-17.59,25.459-41.266,23.647-64.309     C276.884,255.654,300.56,247.783,318.15,230.195z M202.653,290.605l-77.936,77.938c-16.705,16.703-43.889,16.703-60.59,0     l-12.666-12.666c-16.705-16.701-16.703-43.885,0-60.594l77.936-77.932c14.14-14.141,35.779-16.306,52.226-6.516l-32.302,32.307     c-7.606,7.604-7.606,19.938,0,27.541c7.605,7.607,19.937,7.607,27.541,0l32.306-32.303     C218.959,254.828,216.795,276.469,202.653,290.605z M238.382,209.169l32.299-32.306c7.608-7.602,7.608-19.935,0-27.538     c-7.604-7.61-19.936-7.61-27.541-0.004l-32.303,32.303c-9.791-16.446-7.627-38.087,6.514-52.226l77.935-77.935     c16.707-16.707,43.89-16.707,60.594,0l12.664,12.664c16.705,16.705,16.705,43.886,0,60.591l-77.936,77.937     C276.468,216.797,254.828,218.959,238.382,209.169z">
                      </path>
                     </g>
                    </g>
                   </g>
                  </svg>
                 </a>
                </div>
               </span>
              </div>
              <!-- =============other-mode=======-->
              <div class="ind-social-ul color-mode">
               <span class="ind-social-li facebook">
                <a aria-label="facebook" class="ind-social-click ind-fb-bg" href="https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181" target="_blank">
                 <svg enable-background="new 0 0 24 24" height="24" id="Bold" viewbox="0 0 24 24" width="24" xmlns="https://www.w3.org/2000/svg">
                  <path d="m15.997 3.985h2.191v-3.816c-.378-.052-1.678-.169-3.192-.169-3.159 0-5.323 1.987-5.323 5.639v3.361h-3.486v4.266h3.486v10.734h4.274v-10.733h3.345l.531-4.266h-3.877v-2.939c.001-1.233.333-2.077 2.051-2.077z" fill="#fff">
                  </path>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li twitter">
                <a aria-label="Twitter" class="ind-social-click ind-twt-bg" href="https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181&amp;text=Stunning%20Photos%20of%20Sravanthi%3A%20A%20Must-See!" target="_blank">
                 <svg fill="#ffffff" id="Capa_1" viewbox="0 0 24 24" xmlns="https://www.w3.org/2000/svg">
                  <g>
                   <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z">
                   </path>
                  </g>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li whatsapp">
                <a aria-label="Whatsapp" class="ind-social-click ind-whatsapp-bg" href="https://api.whatsapp.com/send?text=Stunning%20Photos%20of%20Sravanthi%3A%20A%20Must-See!%20https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181%20%0A%20%0A" target="_blank">
                 <svg id="Capa_1" viewbox="0 0 512 512" xmlns="https://www.w3.org/2000/svg">
                  <path d="M256.064,0h-0.128C114.784,0,0,114.816,0,256c0,56,18.048,107.904,48.736,150.048l-31.904,95.104l98.4-31.456                        C155.712,496.512,204,512,256.064,512C397.216,512,512,397.152,512,256S397.216,0,256.064,0z M405.024,361.504                        c-6.176,17.44-30.688,31.904-50.24,36.128c-13.376,2.848-30.848,5.12-89.664-19.264C189.888,347.2,141.44,270.752,137.664,265.792                        c-3.616-4.96-30.4-40.48-30.4-77.216s18.656-54.624,26.176-62.304c6.176-6.304,16.384-9.184,26.176-9.184                        c3.168,0,6.016,0.16,8.576,0.288c7.52,0.32,11.296,0.768,16.256,12.64c6.176,14.88,21.216,51.616,23.008,55.392                        c1.824,3.776,3.648,8.896,1.088,13.856c-2.4,5.12-4.512,7.392-8.288,11.744c-3.776,4.352-7.36,7.68-11.136,12.352                        c-3.456,4.064-7.36,8.416-3.008,15.936c4.352,7.36,19.392,31.904,41.536,51.616c28.576,25.44,51.744,33.568,60.032,37.024                        c6.176,2.56,13.536,1.952,18.048-2.848c5.728-6.176,12.8-16.416,20-26.496c5.12-7.232,11.584-8.128,18.368-5.568                        c6.912,2.4,43.488,20.48,51.008,24.224c7.52,3.776,12.48,5.568,14.304,8.736C411.2,329.152,411.2,344.032,405.024,361.504z" fill="#fff">
                  </path>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li telegram">
                <a aria-label="Telegram" class="ind-social-click ind-tele-bg" href="https://t.me/share/url?url=https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181&amp;text=Stunning%20Photos%20of%20Sravanthi%3A%20A%20Must-See!" target="_blank">
                 <svg enable-background="new 0 0 24 24" height="512" id="Bold" viewbox="0 0 24 24" width="512" xmlns="https://www.w3.org/2000/svg">
                  <path d="m9.417 15.181-.397 5.584c.568 0 .814-.244 1.109-.537l2.663-2.545 5.518 4.041c1.012.564 1.725.267 1.998-.931l3.622-16.972.001-.001c.321-1.496-.541-2.081-1.527-1.714l-21.29 8.151c-1.453.564-1.431 1.374-.247 1.741l5.443 1.693 12.643-7.911c.595-.394 1.136-.176.691.218z" fill="#fff">
                  </path>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li linkedin">
                <a aria-label="LinkedIn" class="ind-social-click ind-linked-bg" href="https://www.linkedin.com/shareArticle?mini=true&amp;url=https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181&amp;title=Stunning Photos of Sravanthi: A Must-See!" target="_blank" title="LinkedIn">
                 <svg enable-background="new 0 0 24 24" height="512" id="Bold" viewbox="0 0 24 24" width="512" xmlns="https://www.w3.org/2000/svg">
                  <path d="m23.994 24v-.001h.006v-8.802c0-4.306-.927-7.623-5.961-7.623-2.42 0-4.044 1.328-4.707 2.587h-.07v-2.185h-4.773v16.023h4.97v-7.934c0-2.089.396-4.109 2.983-4.109 2.549 0 2.587 2.384 2.587 4.243v7.801z" fill="#fff">
                  </path>
                  <path d="m.396 7.977h4.976v16.023h-4.976z" fill="#fff">
                  </path>
                  <path d="m2.882 0c-1.591 0-2.882 1.291-2.882 2.882s1.291 2.909 2.882 2.909 2.882-1.318 2.882-2.909c-.001-1.591-1.292-2.882-2.882-2.882z" fill="#fff">
                  </path>
                 </svg>
                </a>
               </span>
               <span class="ind-social-li email">
                <span class="ind-social-click ind-mail-bg js-share-article-by-email-direct" data-domain="https://www.tupaki.com" data-href="mailto:?subject=#{encodeURIComponent('Check this out - '+title)}&amp;body=Stunning%20Photos%20of%20Sravanthi%3A%20A%20Must-See!%20%20%20https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181" data-title="Stunning Photos of Sravanthi: A Must-See!" data-url="https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181" href="javascript:void(0);" title="Share by Email">
                 <svg id="Capa_1" viewbox="0 0 230.17 230.17" xmlns="https://www.w3.org/2000/svg">
                  <path d="M230,49.585c0-0.263,0.181-0.519,0.169-0.779l-70.24,67.68l70.156,65.518c0.041-0.468-0.085-0.94-0.085-1.418V49.585z" fill="#fff">
                  </path>
                  <path d="M149.207,126.901l-28.674,27.588c-1.451,1.396-3.325,2.096-5.2,2.096c-1.836,0-3.672-0.67-5.113-2.013l-28.596-26.647                        L11.01,195.989c1.717,0.617,3.56,1.096,5.49,1.096h197.667c2.866,0,5.554-0.873,7.891-2.175L149.207,126.901z" fill="#fff">
                  </path>
                  <path d="M115.251,138.757L222.447,35.496c-2.427-1.443-5.252-2.411-8.28-2.411H16.5c-3.943,0-7.556,1.531-10.37,3.866                        L115.251,138.757z" fill="#fff">
                  </path>
                  <path d="M0,52.1v128.484c0,1.475,0.339,2.897,0.707,4.256l69.738-67.156L0,52.1z" fill="#fff">
                  </path>
                 </svg>
                </span>
               </span>
               <span class="ind-social-li link">
                <div class="forcopy" data-content="https%3A%2F%2Fwww.tupaki.com%2Fphotogallery%2Fsravanthichokkarapuphotoshoots-1357181" data-url="https://www.tupaki.com/photogallery/sravanthichokkarapuphotoshoots-1357181">
                 <a aria-label="social-link" class="ind-social-click ind-link-bg bg-none" href="javascript:void(0);">
                  <svg height="425.467px" id="Capa_1" style="enable-background:new 0 0 425.466 425.467;" version="1.1" viewbox="0 0 425.466 425.467" width="425.466px" x="0px" xml:space="preserve" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink" y="0px">
                   <g>
                    <g>
                     <g>
                      <path d="M318.15,230.195l77.934-77.937c31.894-31.892,31.894-83.782-0.004-115.674l-12.66-12.66     c-31.893-31.896-83.78-31.896-115.674-0.004l-77.937,77.934c-17.588,17.588-25.457,41.264-23.646,64.311     c-23.045-1.813-46.722,6.056-64.308,23.647L23.92,267.748c-31.894,31.889-31.894,83.779,0,115.674l12.664,12.662     c31.893,31.893,83.783,31.893,115.674,0l77.935-77.936c17.592-17.59,25.459-41.266,23.647-64.309     C276.884,255.654,300.56,247.783,318.15,230.195z M202.653,290.605l-77.936,77.938c-16.705,16.703-43.889,16.703-60.59,0     l-12.666-12.666c-16.705-16.701-16.703-43.885,0-60.594l77.936-77.932c14.14-14.141,35.779-16.306,52.226-6.516l-32.302,32.307     c-7.606,7.604-7.606,19.938,0,27.541c7.605,7.607,19.937,7.607,27.541,0l32.306-32.303     C218.959,254.828,216.795,276.469,202.653,290.605z M238.382,209.169l32.299-32.306c7.608-7.602,7.608-19.935,0-27.538     c-7.604-7.61-19.936-7.61-27.541-0.004l-32.303,32.303c-9.791-16.446-7.627-38.087,6.514-52.226l77.935-77.935     c16.707-16.707,43.89-16.707,60.594,0l12.664,12.664c16.705,16.705,16.705,43.886,0,60.591l-77.936,77.937     C276.468,216.797,254.828,218.959,238.382,209.169z">
                      </path>
                     </g>
                    </g>
                   </g>
                  </svg>
                 </a>
                </div>
               </span>
              </div>
             </div>
            </div>
            <script>
             var hasInitedTheCopy=false;
window.initCopyLink = window.initCopyLink || function(){

    if(hasInitedTheCopy){
        return;
    }
    hasInitedTheCopy=true;
    $("body").on("click",".link",function(){
        copyLink($(this)[0]);
        
        Utils.showModalForView();
        var style = "<style>.modal_wrapper_frame{overflow:auto;}#modal-content .view-content{background:#f2f2f2 !important;padding:20px!important;text-align:center!important;} .copy-message  {font-size:20px;} #modal-content{background: transparent!important;border: 0px!important;}</style>";
        var html = "<h3 class='link-copied align-center'>Link copied</h3>";
        
        var styleElement = document.createElement("style");
        styleElement.innerHTML = style;
        document.head.appendChild(styleElement);
        
        var viewContent = document.querySelector("#modal-content .view-content");
        viewContent.style.background = "#f2f2f2";
        viewContent.style.padding = "20px";
        viewContent.style.textAlign = "center";
        
        var copyMessage = document.createElement("div");
        copyMessage.className = "copy-message";
        copyMessage.style.fontSize = "20px";
        copyMessage.innerHTML = "Link copied";
        viewContent.appendChild(copyMessage);
        
        setTimeout(function () {
            var modalWrapperFrame = document.querySelector(".modal_wrapper_frame");
            if (modalWrapperFrame) {
                modalWrapperFrame.style.display = "none";
            }
        }, 2000);
        
    });
}
document.addEventListener("RESOURCES_LOADED", function(e) {
    window.initCopyLink();
});
if(window.themeResourceLoaded){
    window.initCopyLink();
}
//- document.getElementsByClassName("link")[0].addEventListener('click',copyLink);
var isCopying=false;
function copyLink(elem){
    if(isCopying){
        return;
    }
    isCopying = true;
    setTimeout(function(){isCopying=false;},1000);
    var value = decodeURIComponent(elem.querySelectorAll(".forcopy")[0].getAttribute('data-content'));
    window.isCustomCopyHandler=true;
    elem.classList.add("active");
    console.log(value);
    //- it does not work when window.isSecureContext= false , that's why won't work on local or on staging site,
    //-  but it will work on production
    if (!navigator.clipboard) {
        var aux = document.getElementById("copyTextInput");
        console.log('Copying to clipboard is about to start!')
        // Avoid scrolling to bottom
        aux.value = value;
        aux.focus();
        aux.select();
        document.execCommand("copy");
    } else {
        navigator.clipboard.writeText(value).then(function() {
        console.log('Async: Copying to clipboard was successful!');
    }, function(err) {
        console.error('Async: Could not copy text: ', err);
    });
    }
    
    setTimeout(function(){window.isCustomCopyHandler=false;},1000);
}
            </script>
           </div>
          </div>
          <script>
           window.infiniteScrollUrls = ["/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-2","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-3","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-4","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-5","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-6","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-7","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-8","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-9","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-10","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-11","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-12","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-13","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-14","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-15","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-16","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-17","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-18","/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-19"];
          </script>
          <div class="image_wrapper cutom-gallery clearfix2 count 18 1">
           <span class="slides-num">
            1 / 18
           </span>
           <a aria-label="Previous slide" class="swiper-button-previous" href="/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-18">
            Previous
           </a>
           <a aria-label="Next slide" class="swiper-button-next_image" href="/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-2">
            Next
           </a>
          </div>
          <div class="image_wrapper cutom-gallery clearfix 18 1">
           <span class="slides-num">
            1 / 18
           </span>
           <a class="single-gallery-click-zoom" data-href="https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif">
            <img alt="Stunning Photos of Sravanthi: A Must-See!" data-class="h-custom-image" fetchpriority="high" src="https://content.tupaki.com/h-upload/2024/04/23/364258-f2dhwusu.gif" title="Stunning Photos of Sravanthi: A Must-See!"/>
           </a>
          </div>
          <div class="image_wrapper cutom-gallery clearfix2 count 18 1">
           <span class="slides-num">
            1 / 18
           </span>
           <a aria-label="Previous slide" class="swiper-button-previous" href="/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-18">
            Previous
           </a>
           <a aria-label="Next slide" class="swiper-button-next_image" href="/photogallery/sravanthichokkarapuphotoshoots-1357181/gallery-page-2">
            Next
           </a>
          </div>
          <div class="story-wrapper clearfix">
           <div class="relative-position">
            <div class="detail-text-box story_content details-content-story pd-0 details-story-wrapper">
             <div class="paira-h4">
              <p>
               Sravanthi Chokkarapu is a beloved figure in the film industry, known for her captivating presence both on and off the screen. Her Instagram profile is a testament to her mastery of chic style and timeless elegance. With each post, Sravanthi effortlessly steals the hearts of her followers, showcasing her impeccable fashion sense and graceful demeanor.
              </p>
              <p>
               Hailing from Hyderabad, Sravanthi pursued her bachelor's degree at the University of Auburn. Despite her busy schedule, she gracefully balances her career with her roles as a wife and mother, earning admiration for her ability to juggle multiple responsibilities. While she shares glimpses of her professional life on social media, Sravanthi remains relatively private about her personal affairs, preferring to keep them separate from the spotlight of showbiz.
              </p>
              <div class="hide inside-post-ad-before-before" id="inside_post_content_ad_1_before_before">
              </div>
              <div class="hide inside-post-ad-before" id="inside_post_content_ad_1_before">
              </div>
              <div class="hide inside-post-ad-1 inside-post-ad ads_common_inside_post" id="inside_post_content_ad_1">
              </div>
              <div class="hide inside-post-ad-after" id="inside_post_content_ad_1_after">
              </div>
              <p>
               Recently, Sravanthi treated her fans to a stunning series of photos from a photoshoot, and they were nothing short of mesmerizing. Clad in a radiant yellow saree paired with a high-neck blouse, adorned with a bun hairstyle and flowers delicately placed on her head, Sravanthi exuded elegance and charm. Her infectious smile only added to the allure of the stylish stills, leaving her fans enamored and eagerly anticipating her next glamorous appearance.
              </p>
             </div>
            </div>
           </div>
          </div>
          <div class="to-be-async-loaded-ad follow_block" id="follow_block">
          </div>
          <div class="to-be-async-loaded-ad news_buzz_updates" id="news_buzz_updates">
          </div>
          <div class="hide" id="ad_before_tags">
          </div>
          <div class="tags">
           Tags:
           <span class="tags-wrapper">
            <a href="https://www.tupaki.com/tags/sravanthichokkarapu">
             <button class="span-btn">
              Sravanthichokkarapu
             </button>
            </a>
            <a href="https://www.tupaki.com/tags/sravanthi">
             <button class="span-btn">
              Sravanthi
             </button>
            </a>
            <a href="https://www.tupaki.com/tags/tollywoodanchor">
             <button class="span-btn">
              Tollywoodanchor
             </button>
            </a>
            <a href="https://www.tupaki.com/tags/photoshoots">
             <button class="span-btn">
              Photoshoots
             </button>
            </a>
            <a href="https://www.tupaki.com/tags/biggbosstelugu">
             <button class="span-btn">
              Biggbosstelugu
             </button>
            </a>
            <a href="https://www.tupaki.com/tags/chokkarapu">
             <button class="span-btn">
              Chokkarapu
             </button>
            </a>
            <a href="https://www.tupaki.com/tags/actressgallery">
             <button class="span-btn">
              Actressgallery
             </button>
            </a>
           </span>
          </div>
          <div class="to-be-async-loaded-ad ad_after_tags" id="ad_after_tags">
          </div>
          <div class="" data-name="relatedPost" id="related_post">
          </div>
          <div class="to-be-async-loaded-ad detail_1" id="detail_1">
          </div>
          <div class="hide" id="detail_2">
          </div>
         </div>
        </div>
        <div class="entertainment-telugu trending">
         <div class="to-be-async-loaded-ad right_level_1" id="right_level_1">
         </div>
         <div class="" data-name="verticalListWithImages" id="right_level_2">
         </div>
         <div class="to-be-async-loaded-ad right_level_3" id="right_level_3">
         </div>
         <div class="hide" id="right_level_4">
         </div>
         <div class="to-be-async-loaded-ad right_level_5" id="right_level_5">
         </div>
         <div class="to-be-async-loaded-ad right_level_5" id="right_level_5">
         </div>
         <div class="hide" id="right_level_7">
         </div>
         <div class="" data-name="verticalListWithImages" id="trending_news">
         </div>
        </div>
       </div>
      </div>
      <div class="related">
       <div class="articles">
        <div class="" data-name="gridTwo" id="detail_wrap_1">
        </div>
       </div>
       <div class="live-ads to-be-async-loaded-ad detail_wrap_ad_4" id="detail_wrap_ad_4">
       </div>
      </div>
      <section class="ads-slider py-4 py-sm-5">
       <div class="" data-name="newsWithTextInBottom" id="photo_stories">
       </div>
       <div class="hide" id="detail_wrap_ad_5">
       </div>
      </section>
     </div>
     <div class="hide" id="detail_wrap_ad_6">
     </div>
     <div class="live-ads">
      <div class="hide" id="right_sticky_ad">
      </div>
     </div>
     <div class="hide" id="detail_wrap_ad_7">
     </div>
    </section>
    <div class="hide" id="detail_wrap_2">
    </div>
    <div class="to-be-async-loaded-ad footer_1" id="footer_1">
    </div>
   </div>
   <div class="after_content_mask">
   </div>
  </div>
  <div class="hide" id="generic_ad_block">
  </div>
  <input class="hide" id="copyTextInput"/>
  <!-- +stickySocialShare()-->
  <div class="primary-page-content-wrapper content-direction-ltr" data-categoryid="10078" data-cdnurl="" data-contentid="" data-ismobile="" data-logging-enabled="" data-newsid="1357181" data-partner="tupaki" data-path="/photogallery/sravanthichokkarapuphotoshoots-1357181" data-query-partner="tupaki" data-query-root="www.tupaki.com" data-query-sessionid="RDWEBRFGMBZX1KWO5FDPZXA5XGEE7DTNFZXY1" data-registration-mode="undefined" data-root="https://www.tupaki.com" data-sessionid="RDWEBRFGMBZX1KWO5FDPZXA5XGEE7DTNFZXY1" data-userid="" has-ga-store-key="1" id="body-bottom-content">
   <script override-script="true">
    window.allScriptsTemplate = [{"id":"14594","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"header_ad_1","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"14594","overriden":true,"asyncHtmlMixin":true,"merged-in-sync":false},{"id":"11922","end_point":"","link":"/latest-news","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","viewAllInHeading":"true","astroClass":"Astrology","headingLater":"true","hrTagForContent":"true","viewAll":"true","pClass":"related-para","forceUseCoverImage":"true","mixin_params":"undefined","displayHeading":"","chartId":"null","content_type":"CATEGORY_NEWS","newsCount":"4","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"Latest  News","widgetId":"null","mixinName":"gridTwo","element_id":"detail_wrap_1","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"10075","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11922","merged-in-sync":false},{"id":"11923","end_point":"","link":"/entertainment/tollywood","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"CATEGORY_NEWS","newsCount":"10","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"newsWithTextInBottom","element_id":"error_level_1","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"10117","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11923","merged-in-sync":false},{"id":"11924","end_point":"","link":"/trending","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"CATEGORY_NEWS","newsCount":"8","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"TRENDING","widgetId":"null","mixinName":"verticalListWithImages","element_id":"error_level_2","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"10294","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11924","merged-in-sync":false},{"id":"11925","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3Cfooter%20class%3D%22footer-section%22%3E%20%20%20%20%3Cdiv%20class%3D%22container-footer%22%3E%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-widget%22%3E%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-widget-heading%22%3E%20%20%20%20%20%20%20%20%20%20%3Ch3%3E%3Ca%20href%3D%22%2Fentertainment%22%3EEntertainment%3C%2Fa%3E%3C%2Fh3%3E%20%20%20%20%20%20%20%20%20%20%3Cul%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fmovies-reviews%22%20target%3D%22_blank%22%3EMovie%20Reviews%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fpress-notes%22%20target%3D%22_blank%22%3EPress%20Release%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fmovies-schedules%22%20target%3D%22_blank%22%3EMovie%20Schedules%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fgossips%22%20target%3D%22_blank%22%3EGossips%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fstreaming-apps%22%20%3EOTT%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%3C%2Ful%3E%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-widget%22%3E%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-widget-heading%22%3E%20%20%20%20%20%20%20%20%20%20%3Ch3%3E%3Ca%20href%3D%22%2Flatest-news%22%3ELatest%20News%3C%2Fa%3E%3C%2Fh3%3E%20%20%20%20%20%20%20%20%20%20%3Cul%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Ftop-news%22%3ETop%20News%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Ftrending%22%3ETrending%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fandhrapradesh%22%3EAndhra%20Pradesh%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Ftelangana%22%3ETelangana%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fnri%22%3ENRI%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%3C%2Ful%3E%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-widget%22%3E%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-widget-heading%22%3E%20%20%20%20%20%20%20%20%20%20%3Ch3%3E%3Ca%20href%3D%22%2Fphotogallery%22%3EPhotos%3C%2Fa%3E%3C%2Fh3%3E%20%20%20%20%20%20%20%20%20%20%3Cul%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fphotogallery%22%3ELatest%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fphotogallery%2Factress%22%3EActress%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fphotogallery%2Fevents%22%3EEvents%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fphotogallery%2Fmovies%22%3EMovies%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fphotogallery%2Factor%22%3EActors%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%3C%2Ful%3E%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-widget%22%3E%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-widget-heading%22%3E%20%20%20%20%20%20%20%20%20%20%3Ch3%3E%3Ca%20href%3D%22%2Flifestyle%22%3ELife%20Style%3C%2Fa%3E%3C%2Fh3%3E%20%20%20%20%20%20%20%20%20%20%3Cul%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fhealth%22%3EHealth%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fastrology%22%3EAstrology%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Ftravel%22%3ETravel%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Feducation%22%3EEducation%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Ffood%22%3EFood%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%3C%2Ful%3E%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-widget%22%3E%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-widget-heading%22%3E%20%20%20%20%20%20%20%20%20%20%3Ch3%3E%3Ca%20href%3D%22%2Fsports%22%3ESports%3C%2Fa%3E%3C%2Fh3%3E%20%20%20%20%20%20%20%20%20%20%3Cul%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fautomobiles%22%3EAutomobiles%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fgadgets%22%3EGadgets%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fbusiness%22%3EBusiness%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Freal-estate%22%3EReal%20Estate%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Finsurance%22%3EInsurance%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%3C%2Ful%3E%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-widget%22%3E%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-widget-heading%22%3E%20%20%20%20%20%20%20%20%20%20%3Ch3%3E%3Ca%20href%3D%22https%3A%2F%2Fenglish.tupaki.com%2Fcinema-videos%22%20target%3D%22_blank%22%3ETupaki%20Cinema%3C%2Fa%3E%20%20%20%3C%2Fh3%3E%20%20%20%20%20%20%20%20%20%20%3Cul%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22https%3A%2F%2Fenglish.tupaki.com%2Fpolitical-videos%22%20target%3D%22_blank%22%3ETupaki%20Political%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Ftupakiexclusive%22%3ETupaki%20Excusive%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fspecial-articles%22%3ESpecial%20Articles%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fjobs%22%3EJobs%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fphoto-story%22%3EPhoto%20Stories%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%3C%2Ful%3E%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-widget%22%3E%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-widget-heading%22%20id%3D%22footer-tags%22%3E%3C%2Fdiv%3E%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3Cdiv%20class%3D%22container-footer%22%3E%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-ul%22%3E%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22copyright-text%20download%22%3E%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2F%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cimg%20src%3D%22%2Ftheme_teal%2Fimages%2Flogo.png%22%20class%3D%22img-fluid%22%20alt%3D%22logo%22%3E%20%20%20%20%20%20%20%20%20%20%3C%2Fa%3E%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-menu%22%3E%20%20%20%20%20%20%20%20%20%20%3Ch3%3E%20%3C%2Fh3%3E%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22list-inline%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22https%3A%2F%2Fwww.facebook.com%2FTupakiofficial%22%20target%3D%22_blank%22%20title%3D%22Like%20us!%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ci%20class%3D%22fa%20fa-facebook%20fa-2x%22%3E%3C%2Fi%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22https%3A%2F%2Fwww.instagram.com%2Ftupaki_official%2F%22%20target%3D%22_blank%22%20title%3D%22Insta%20us!%22%20%20target%3D%22_blank%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ci%20class%3D%22fa%20fa-instagram%20fa-2x%22%3E%3C%2Fi%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22https%3A%2F%2Ftwitter.com%2Ftupaki_official%22%20title%3D%22Tweet%20us!%22%20%20target%3D%22_blank%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ci%20class%3D%22fa%20fa-twitter%20fa-2x%22%3E%3C%2Fi%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%23%22%20%20target%3D%22_blank%22%20title%3D%22Connect%20wih%20us!%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ci%20class%3D%22fa%20fa-linkedin%20fa-2x%22%3E%3C%2Fi%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%23%22%20%20%20target%3D%22_blank%22%20title%3D%22Code%20with%20us!%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ci%20class%3D%22fa%20fa-snapchat%20fa-2x%22%3E%3C%2Fi%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22https%3A%2F%2Fwww.youtube.com%2F%40tupakipolitical8524%3FthemeRefresh%3D1%22%20target%3D%22_blank%22%20title%3D%22Mail%20us!%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ci%20class%3D%22fa%20fa-youtube%20fa-2x%22%3E%3C%2Fi%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3Cdiv%20class%3D%22copyright-area%22%3E%20%20%20%20%20%20%3Cdiv%20class%3D%22container-fluid%22%3E%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22row%22%3E%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22col-xl-4%20col-lg-4%20col-xs-12%20d-none%20d-lg-block%20text-right%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22footer-menu%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cul%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%20%2Fabout-us%22%3EAbout%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%3Ca%20href%3D%22%2Fterms-condition%22%3ETerms%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fadvertise%22%3EAdvertise%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fprivacy-policy%22%3EPrivacy%C2%A0Policy%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Ca%20href%3D%22%2Fcontactus%22%3EContact%20%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fli%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Ful%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22col-xl-4%20col-lg-4%20col-xs-12%20text-center%20text-lg-left%22%3E%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22copyright-text%22%20style%3D%22%20%20%20%20%20%20color%3A%20white%3B%20%20%22%3E%20%20%20%20%20%20%20%20%20%20%20%20Powered%20by%20%3Ca%20href%3D%22https%3A%2F%2Fwww.hocalwire.com%22%20style%3D%22%20%20%20%20%20%20color%3A%20white%3B%20%20%22%3EHocalwire%3C%2Fa%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22col-xl-4%20col-lg-4%20col-xs-12%20d-none%20d-lg-block%20text-right%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22copyright-text%22%3E%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cp%3E%C2%A9%20Copyright%202024.%20All%20rights%20reserved.%3C%2Fp%3E%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%20%20%3C%2Fdiv%3E%20%20%20%20%3C%2Fdiv%3E%20%20%3C%2Ffooter%3E%20%20%20%20%3Cstyle%3E%20%20.container-footer%20a%7B%20%20%20%20%20%20color%3Ablack%3B%20%20%7D%20%20.container-footer%20%7B%20%20%20%20%20%20display%3A%20flex%3B%20%20margin%3A%20auto%3B%20%20%7D%20%20%3C%2Fstyle%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"footer_1","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11925","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"11926","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"DESKTOP || MOBILE","widgetId":"null","mixinName":"","element_id":"gallery_right_level_1","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11926","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"11927","end_point":"","link":"/trending","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","figureTag":"true","shareClass":"true","classesWithFlex":"news-latest","extraClassHeading":"most-read","mixin_params":"undefined","displayHeading":"","chartId":"null","content_type":"CATEGORY_NEWS","newsCount":"8","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"Trending","widgetId":"null","mixinName":"verticalListWithImages","element_id":"gallery_right_level_2","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"10294","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11927","merged-in-sync":false},{"id":"11929","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"DESKTOP || MOBILE","widgetId":"null","mixinName":"","element_id":"gallery_right_level_3","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11929","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"14592","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3C!--%20%2F71872138%2FHP_skyscrapper_left_telugu%20--%3E%20%20%3Cdiv%20id%3D'div-gpt-ad-1702919989426-0'%20style%3D'min-width%3A%20120px%3B%20min-height%3A%20600px%3B'%3E%20%20%20%20%3Cscript%3E%20%20%20%20%20%20googletag.cmd.push(function()%20%7B%20googletag.display('div-gpt-ad-1702919989426-0')%3B%20%7D)%3B%20%20%20%20%3C%2Fscript%3E%20%20%3C%2Fdiv%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"level_1_left","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"14592","overriden":true,"asyncHtmlMixin":true,"merged-in-sync":false},{"id":"14593","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3C!--%20%2F71872138%2FHP_skyscrapper_right_telugu%20--%3E%20%20%3Cdiv%20id%3D'div-gpt-ad-1702920079488-0'%20style%3D'min-width%3A%20120px%3B%20min-height%3A%20600px%3B'%3E%20%20%20%20%3Cscript%3E%20%20%20%20%20%20googletag.cmd.push(function()%20%7B%20googletag.display('div-gpt-ad-1702920079488-0')%3B%20%7D)%3B%20%20%20%20%3C%2Fscript%3E%20%20%3C%2Fdiv%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"level_1_right","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"14593","overriden":true,"asyncHtmlMixin":true,"merged-in-sync":false},{"id":"11933","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"DESKTOP || MOBILE","widgetId":"null","mixinName":"","element_id":"movie_right_level_1","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11933","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"11934","end_point":"","link":"/trending","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","figureTag":"true","shareClass":"true","classesWithFlex":"generic-right","extraClassHeading":"most-read","mixin_params":"undefined","displayHeading":"","chartId":"null","content_type":"CATEGORY_NEWS","newsCount":"8","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"Trending","widgetId":"null","mixinName":"verticalListWithImages","element_id":"movie_right_level_2","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"10294","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11934","merged-in-sync":false},{"id":"11935","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"DESKTOP || MOBILE","widgetId":"null","mixinName":"","element_id":"movie_right_level_3","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11935","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"11936","end_point":"","link":"/photo-story","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","shadowVector":"true","headingWithHeding":"true","videoExtraClass":"stories","sliderClass":"swiper-containernr","hrTag":"true","getWhiteColor":"true","mixin_params":"undefined","displayHeading":"","chartId":"null","content_type":"CATEGORY_NEWS","newsCount":"10","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"Photo Stories","widgetId":"null","mixinName":"newsWithTextInBottom","element_id":"photo_stories","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"10192","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11936","merged-in-sync":false},{"id":"11937","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"Tel-Article-RHS-1 || Tel-Mob-Art-Above article","widgetId":"null","mixinName":"","element_id":"right_level_1","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11937","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"11938","end_point":"","link":"/trending","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","figureTag":"true","shareClass":"true","classesWithFlex":"generic-right","mixin_params":"undefined","displayHeading":"","chartId":"null","content_type":"CATEGORY_NEWS","newsCount":"8","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"Trending","widgetId":"null","mixinName":"verticalListWithImages","element_id":"right_level_2","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"10294","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11938","merged-in-sync":false},{"id":"11939","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"Tel-Article-RHS-2","widgetId":"null","mixinName":"","element_id":"right_level_3","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11939","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"11940","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3Cul%20class%3D%22nav-tabs%22%3E%20%20%09%09%09%09%09%3Cli%20class%3D%22nav-item%20tab%20is-active%22%20data-role%3D%22tab%22%20data-target%3D%22%23tabs-home3%22%3E%3Ca%20href%3D'%2Fphotogallery'%20class%3D'gallery-tab-link'%20%3ELatest%3C%2Fa%3E%20%20%09%09%09%09%09%3C%2Fli%3E%20%20%09%09%09%09%09%3Cli%20class%3D%22nav-item%20tab%22%20data-role%3D%22tab%22%20data-target%3D%22%23tabs-profile3%22%3E%3Ca%20href%3D'%2Fphotogallery%2Factor'%20class%3D'gallery-tab-link'%20%3EActor%3C%2Fa%3E%20%20%09%09%09%09%09%3C%2Fli%3E%20%20%09%09%09%09%09%3Cli%20class%3D%22nav-item%20tab%22%20data-role%3D%22tab%22%20data-target%3D%22%23tabs-profile4%22%3E%3Ca%20href%3D'%2Fphotogallery%2Factress'%20class%3D'gallery-tab-link'%20%3EActress%3C%2Fa%3E%20%20%09%09%09%09%09%3C%2Fli%3E%20%20%09%09%09%09%09%3Cli%20class%3D%22nav-item%20tab%22%20data-role%3D%22tab%22%20data-target%3D%22%23tabs-profile5%22%3E%3Ca%20href%3D'%2Fphotogallery%2Fmovies'%20class%3D'gallery-tab-link'%20%3EMovies%3C%2Fa%3E%20%20%09%09%09%09%09%3C%2Fli%3E%20%20%09%09%09%09%09%3Cli%20class%3D%22nav-item%20tab%22%20data-role%3D%22tab%22%20data-target%3D%22%23tabs-profile6%22%3E%3Ca%20href%3D'%2Fphotogallery%2Fevents'%20class%3D'gallery-tab-link'%20%3EEvents%3C%2Fa%3E%20%20%09%09%09%09%09%3C%2Fli%3E%20%20%09%09%09%09%20%20%3C%2Ful%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"gallery_tabs","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11940","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"11955","end_point":"com.rdes.engine.news.RDNewsEngine#getTrendingNews","link":"/most-popular","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","extraClassHeading":"most-read","figureTag":"true","shareClass":"true","forceUseCoverImage":"true","mixin_params":"undefined","displayHeading":"","chartId":"null","content_type":"CATEGORY_NEWS","newsCount":"10","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"MOST READ","widgetId":"null","mixinName":"verticalListWithImages","element_id":"trending_news","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"10175","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11955","merged-in-sync":false},{"id":"11956","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3Cbutton%20id%3D%22pmLink%22%3EPrivacy%20Manager%3C%2Fbutton%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"detail_wrap_ad_4","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"11956","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"14548","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"inside_post_content_ad_1","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"14548","overriden":true,"asyncHtmlMixin":true,"merged-in-sync":false},{"id":"14551","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"inside_post_content_ad_2","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"14551","overriden":true,"asyncHtmlMixin":true,"merged-in-sync":false},{"id":"14552","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"inside_post_content_ad_3","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"14552","overriden":true,"asyncHtmlMixin":true,"merged-in-sync":false},{"id":"14553","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"inside_post_content_ad_4","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"14553","overriden":true,"asyncHtmlMixin":true,"merged-in-sync":false},{"id":"12182","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"left_level_1","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"12182","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"12183","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"left_level_2","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"12183","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"12184","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"left_level_3","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"12184","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"12185","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"left_level_4","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"12185","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"12255","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3Ca%20href%3D%22https%3A%2F%2Fenglish.tupaki.com%22%3E%3Cbutton%20class%3D'telugu'%3E%20English%3C%2Fbutton%3E%3C%2Fa%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"header_btn","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"12255","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"12387","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3Cdiv%20class%3D%22follow%22%20style%3D%22%20%20%20%20%20%20height%3A%20100px%3B%20%20%22%3E%20%20%09%09%09%09%09%20%20%09%09%09%09%09%09%3Cp%3EClick%20to%20follow%20%20%3Ca%20href%3D%22https%3A%2F%2Fwww.facebook.com%2FTupakiofficial%22%20target%3D%22_blank%22%3ETupaki%20Facebook%20page%3C%2Fa%3E%2C%C2%A0%3Ca%20href%3D%22https%3A%2F%2Fwww.instagram.com%2Ftupaki_official%2F%22%20target%3D%22_blank%22%3EInstagram%3C%2Fa%3E%C2%A0and%20%20%3Ca%20href%3D%22https%3A%2F%2Ftwitter.com%2Ftupaki_official%22%20target%3D%22_blank%22%3E%20Twitter%20%3C%2Fa%3E%20%3C%2Fp%3E%20%20%09%09%09%09%09%3C%2Fdiv%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"follow_block","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"12387","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"12404","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","tagsInFooter":"true","footerTagCount":"5","mixin_params":"undefined","displayHeading":"","chartId":"null","content_type":"OTHER","newsCount":"5","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"#Tags","widgetId":"null","mixinName":"trendingTagsForHeading","element_id":"footer-tags","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"12404","merged-in-sync":false},{"id":"12439","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3Cdiv%20id%3D%22taboola-below-article-thumbnails%22%3E%3C%2Fdiv%3E%20%20%3Cscript%20type%3D%22text%2Fjavascript%22%3E%20%20%20%20window._taboola%20%3D%20window._taboola%20%7C%7C%20%5B%5D%3B%20%20%20%20_taboola.push(%7B%20%20%20%20%20%20mode%3A%20'alternating-thumbnails-a'%2C%20%20%20%20%20%20container%3A%20'taboola-below-article-thumbnails'%2C%20%20%20%20%20%20placement%3A%20'Below%20Article%20Thumbnails'%2C%20%20%20%20%20%20target_type%3A%20'mix'%20%20%20%20%7D)%3B%20%20%3C%2Fscript%3E%20%20%20%20%3Cscript%20type%3D%22text%2Fjavascript%22%3E%20%20%20%20window._taboola%20%3D%20window._taboola%20%7C%7C%20%5B%5D%3B%20%20%20%20_taboola.push(%7Bflush%3A%20true%7D)%3B%20%20%3C%2Fscript%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"detail_1","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"12439","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"12481","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3Cdiv%20id%3D'desk_demo_fill4'%20class%3D'ad_unit_wrapper%20track-click'%20data-label%3D'demobanner'%20data-category%3D'banner_ad'%20%20style%3D'text-align%3Acenter%3B'%3E%3Ca%20href%3D'https%3A%2F%2Fwww.hocalwire.com%2F'%20target%3D'_blank'%3E%3Cimg%20src%3D'http%3A%2F%2Ftpweb1.vocalwire.com%2Fcontent%2Fservlet%2FRDESController%3Fcommand%3Drdm.Picture%26app%3Drdes%26partner%3Dtupaki%26sessionId%3DRDWEBRFGMBZX1KWO5FDPZXA5XGEE7DTNFZXY1%26type%3D7%26uid%3D24015WA4eG2Iad6z0XkAMdeNTgJto2aLoN3z05468320'%20alt%3D''%20style%3D'width%3Aauto%3Bheight%3Aauto%3B'%2F%3E%3C%2Fa%3E%3C%2Fdiv%3E%20%20%20%20%20%20%20%3Cdiv%20id%3D'mob_demo_fill4'%20class%3D'ad_unit_wrapper%20track-click'%20data-label%3D'mobilebanner'%20data-category%3D'banner_ad'%20%20style%3D'text-align%3Acenter%3B'%3E%3Ca%20href%3D'https%3A%2F%2Fwww.hocalwire.com%2F'%20target%3D'_blank'%3E%3Cimg%20src%3D'http%3A%2F%2Ftpweb1.vocalwire.com%2Fcontent%2Fservlet%2FRDESController%3Fcommand%3Drdm.Picture%26app%3Drdes%26partner%3Dtupaki%26sessionId%3DRDWEBRFGMBZX1KWO5FDPZXA5XGEE7DTNFZXY1%26type%3D7%26uid%3D24015r63T06DU8FGSRnxo6G1JXg9MDD3tCxZg7232878'%20alt%3D''%20style%3D'width%3Aauto%3Bheight%3Aauto%3B'%2F%3E%3C%2Fa%3E%3C%2Fdiv%3E%20%20%20%20%20%20%3Cstyle%3E%20%20%23mob_demo_fill4%7B%20%20display%3Anone%3B%20%20%7D%20%20%40media(max-width%3A500px)%20%20%7B%20%20%23mob_demo_fill4%7B%20%20display%3Ablock%3B%20%20%7D%20%20%23desk_demo_fill4%7B%20%20display%3Anone%3B%20%20%7D%20%20%7D%20%20%3C%2Fstyle%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"filler_ad_4","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"12481","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"12482","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3Cdiv%20id%3D'desk_demo_fill5'%20class%3D'ad_unit_wrapper%20track-click'%20data-label%3D'demobanner'%20data-category%3D'banner_ad'%20%20style%3D'text-align%3Acenter%3B'%3E%3Ca%20href%3D'https%3A%2F%2Fwww.hocalwire.com%2F'%20target%3D'_blank'%3E%3Cimg%20src%3D'http%3A%2F%2Ftpweb1.vocalwire.com%2Fcontent%2Fservlet%2FRDESController%3Fcommand%3Drdm.Picture%26app%3Drdes%26partner%3Dtupaki%26sessionId%3DRDWEBRFGMBZX1KWO5FDPZXA5XGEE7DTNFZXY1%26type%3D7%26uid%3D24015WA4eG2Iad6z0XkAMdeNTgJto2aLoN3z05468320'%20alt%3D''%20style%3D'width%3Aauto%3Bheight%3Aauto%3B'%2F%3E%3C%2Fa%3E%3C%2Fdiv%3E%20%20%20%20%20%20%20%3Cdiv%20id%3D'mob_demo_fill5'%20class%3D'ad_unit_wrapper%20track-click'%20data-label%3D'mobilebanner'%20data-category%3D'banner_ad'%20%20style%3D'text-align%3Acenter%3B'%3E%3Ca%20href%3D'https%3A%2F%2Fwww.hocalwire.com%2F'%20target%3D'_blank'%3E%3Cimg%20src%3D'http%3A%2F%2Ftpweb1.vocalwire.com%2Fcontent%2Fservlet%2FRDESController%3Fcommand%3Drdm.Picture%26app%3Drdes%26partner%3Dtupaki%26sessionId%3DRDWEBRFGMBZX1KWO5FDPZXA5XGEE7DTNFZXY1%26type%3D7%26uid%3D24015r63T06DU8FGSRnxo6G1JXg9MDD3tCxZg7232878'%20alt%3D''%20style%3D'width%3Aauto%3Bheight%3Aauto%3B'%2F%3E%3C%2Fa%3E%3C%2Fdiv%3E%20%20%20%20%20%20%3Cstyle%3E%20%20%23mob_demo_fill5%7B%20%20display%3Anone%3B%20%20%7D%20%20%40media(max-width%3A500px)%20%20%7B%20%20%23mob_demo_fill5%7B%20%20display%3Ablock%3B%20%20%7D%20%20%23desk_demo_fill5%7B%20%20display%3Anone%3B%20%20%7D%20%20%7D%20%20%3C%2Fstyle%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"filler_ad_5","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"12482","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"12483","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3Cdiv%20id%3D'desk_demo_fill6'%20class%3D'ad_unit_wrapper%20track-click'%20data-label%3D'demobanner'%20data-category%3D'banner_ad'%20%20style%3D'text-align%3Acenter%3B'%3E%3Ca%20href%3D'https%3A%2F%2Fwww.hocalwire.com%2F'%20target%3D'_blank'%3E%3Cimg%20src%3D'http%3A%2F%2Ftpweb1.vocalwire.com%2Fcontent%2Fservlet%2FRDESController%3Fcommand%3Drdm.Picture%26app%3Drdes%26partner%3Dtupaki%26sessionId%3DRDWEBRFGMBZX1KWO5FDPZXA5XGEE7DTNFZXY1%26type%3D7%26uid%3D24015WA4eG2Iad6z0XkAMdeNTgJto2aLoN3z05468320'%20alt%3D''%20style%3D'width%3Aauto%3Bheight%3Aauto%3B'%2F%3E%3C%2Fa%3E%3C%2Fdiv%3E%20%20%20%20%20%20%20%3Cdiv%20id%3D'mob_demo_fill6'%20class%3D'ad_unit_wrapper%20track-click'%20data-label%3D'mobilebanner'%20data-category%3D'banner_ad'%20%20style%3D'text-align%3Acenter%3B'%3E%3Ca%20href%3D'https%3A%2F%2Fwww.hocalwire.com%2F'%20target%3D'_blank'%3E%3Cimg%20src%3D'http%3A%2F%2Ftpweb1.vocalwire.com%2Fcontent%2Fservlet%2FRDESController%3Fcommand%3Drdm.Picture%26app%3Drdes%26partner%3Dtupaki%26sessionId%3DRDWEBRFGMBZX1KWO5FDPZXA5XGEE7DTNFZXY1%26type%3D7%26uid%3D24015r63T06DU8FGSRnxo6G1JXg9MDD3tCxZg7232878'%20alt%3D''%20style%3D'width%3Aauto%3Bheight%3Aauto%3B'%2F%3E%3C%2Fa%3E%3C%2Fdiv%3E%20%20%20%20%20%20%3Cstyle%3E%20%20%23mob_demo_fill6%7B%20%20display%3Anone%3B%20%20%7D%20%20%40media(max-width%3A500px)%20%20%7B%20%20%23mob_demo_fill6%7B%20%20display%3Ablock%3B%20%20%7D%20%20%23desk_demo_fill6%7B%20%20display%3Anone%3B%20%20%7D%20%20%7D%20%20%3C%2Fstyle%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"filler_ad_6","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"12483","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"14333","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3Cscript%3E%20%20%C2%A0%C2%A0%C2%A0%20%C2%A0%C2%A0%C2%A0window.unibotshb%20%3D%20window.unibotshb%20%7C%7C%20%7B%20cmd%3A%20%5B%5D%20%7D%3B%20%20%C2%A0%C2%A0%C2%A0%20%C2%A0%C2%A0%C2%A0unibotshb.cmd.push(()%3D%3E%7B%20ubHB(%22tupaki%22)%3B%20%7D)%3B%20%20%C2%A0%C2%A0%C2%A0%3C%2Fscript%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"async_body_tags","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"14333","overriden":true,"asyncHtmlMixin":true,"merged-in-sync":false},{"id":"13194","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"Tel-Article-RHS-3","widgetId":"null","mixinName":"","element_id":"right_level_5","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"13194","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"13524","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"left-ad-full-screen","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"13524","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"13525","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"right-ad-full-screen","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"13525","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"13595","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3Cbutton%20id%3D%22pmLink%22%3EPrivacy%20Manager%3C%2Fbutton%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"detail_wrap_ad_1","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"13595","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"13690","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3Cscript%20async%20src%3D%22https%3A%2F%2Ft.seedtag.com%2Ft%2F6537-0291-01.js%22%3E%3C%2Fscript%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_tags","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"13690","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"13747","end_point":"com.rdes.engine.news.RDNewsEngine#getTrendingNews","link":"/most-popular","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","figureTag":"true","shareClass":"true","classesWithFlex":"generic-right","extraClassHeading":"most-read","mixin_params":"undefined","displayHeading":"","chartId":"null","content_type":"GENERIC","newsCount":"9","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"MOST READ","widgetId":"null","mixinName":"verticalListWithImages","element_id":"movie_right_level_4","electionId":"null","adId":"null","page":"common","param_name":"","data_partner":"tupaki","categoryId":"10175","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"13747","merged-in-sync":false},{"id":"14645","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"bottom_snackbar_content","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"14645","overriden":true,"asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15779","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_2_right_level_2","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15779","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15780","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_11_trending_news","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15780","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15781","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_2_trending_news","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15781","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15782","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_5_right_level_2","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15782","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15783","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_5_trending_news","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15783","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15784","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_8_right_level_2","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15784","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15785","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_8_trending_news","electionId":"null","adId":"null","page":"news_details","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15785","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"12469","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"%3Cbutton%20id%3D%22pmLink%22%3EPrivacy%20Manager%3C%2Fbutton%3E","mixin_params":"","displayHeading":"","chartId":"null","content_type":"AD","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"news_buzz_updates","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"12469","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15794","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_11_gallery_right_level_2","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15794","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15795","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_2_gallery_right_level_2","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15795","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15796","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_5_gallery_right_level_2","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15796","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15797","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_8_gallery_right_level_2","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15797","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15799","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_11_movie_right_level_4","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15799","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15800","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_2_movie_right_level_4","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15800","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15801","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_5_movie_right_level_4","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15801","asyncHtmlMixin":true,"merged-in-sync":false},{"id":"15802","end_point":"","link":"","description":"","request_params":"","element_type":"CONTENT","is_sync":"false","content":"","mixin_params":"","displayHeading":"","chartId":"null","content_type":"HTML","newsCount":"null","theme":"theme_teal","state":"LIVE","generic_content_type":"null","is_visible":"true","heading":"","widgetId":"null","mixinName":"","element_id":"ad_after_news_level_8_movie_right_level_4","electionId":"null","adId":"null","page":"news_details_10078","param_name":"","data_partner":"tupaki","categoryId":"null","default_content":"","extra_css":"","rdm_partner":"tupaki","mixinId":"15802","asyncHtmlMixin":true,"merged-in-sync":false},{"newsId":"1357181","id":"","mixinName":"relatedPost","theme":"theme_teal","categoryId":"10078","link":"/photogallery","element_type":"CONTENT","element_id":"related_post","is_visible":"true","content":"","default_content":"","is_sync":"false","page":"news_details","excludeNews":"1357181","rdm_partner":"tupaki","extraCacheField":"","description":"","ignoreContentNews":true,"content_type":"CATEGORY_NEWS","similarPostFetchFromServer":"","heading":"Similar Posts","maxCount":"12","newsCount":13,"includeAsItemsInResponse":"inside_post_content_ad_1_before,inside_post_content_ad_2_before,inside_post_content_ad_3_before,inside_post_content_ad_4_before","merged-in-sync":false},{"id":"","newsId":"1357181","mixinName":"relatedPost2","theme":"theme_teal","categoryId":"10078","link":"/photogallery","element_type":"CONTENT","element_id":"related_post_2","is_visible":"true","content":"","default_content":"","rdm_partner":"tupaki","is_sync":"false","page":"news_details","excludeNews":"1357181","extraCacheField":"","description":"","ignoreContentNews":true,"content_type":"CATEGORY_NEWS","similarPostFetchFromServer":"","heading":"More News","maxCount":4,"newsCount":5,"merged-in-sync":false}];
   </script>
   <script>
    window.hocalApiEndPoints = {"/test-api":"localhost"};
   </script>
   <div class="mfp-hide" id="small-dialog">
   </div>
   <!-- -if(!env.partnerData.disable_location_settings_website){-->
   <!--     #floating-location-container.hide-->
   <!--         a#floating-button(href="https://hocalwire.com/get-geo?domain_partner="+env.partner+"&domain="+(encodeURIComponent(env.rootUrl)),target="_blank")-->
   <!--             img.location(src="/images/location.png")-->
   <!-- -} else {-->
   <!--     #floating-location-container.hide.no-manatory-loc-->
   <!--         a#floating-button(href="https://hocalwire.com/get-geo?domain_partner="+env.partner+"&domain="+(encodeURIComponent(env.rootUrl)),target="_blank")-->
   <!--             img.location(src="/images/location.png")-->
   <!-- -}-->
   <div id="floating-extra-container">
   </div>
   <div class="hide" id="fixed-bottom-content">
   </div>
   <div id="hidden_element_for_width">
   </div>
   <div id="hidden_element_for_desktop">
   </div>
   <div id="hidden_element_for_tablet_pro">
   </div>
   <div id="hidden_element_for_tablet">
   </div>
   <div class="hide" id="body_bottom_sync">
   </div>
   <div class="hide" id="after_everything">
   </div>
   <style>
    #hidden_element_for_desktop {
    display:block;
    height:0px;
}
#hidden_element_for_tablet_pro {
    display:none;
}
#hidden_element_for_tablet {
    display:none;
    height:0px;
}

@media(max-width:999px ){
    #hidden_element_for_width {
        display:none;
    }
}
@media(min-width:1000px ){
    #hidden_element_for_width {
        display:block;
        height:0px;
    }
}
@media(max-width:1191px){
    #hidden_element_for_desktop {
        display:none;
    }
    #hidden_element_for_tablet {
        display:none;
    }
    #hidden_element_for_tablet_pro {
        display:block;
    }
}
@media(max-width:767px){
    #hidden_element_for_desktop {
        display:none;
    }
    #hidden_element_for_tablet_pro {
        display:none;
    }
    #hidden_element_for_tablet {
        display:block;
    }
}
@media(max-width:479px){
    #hidden_element_for_desktop {
        display:none;
    }
    #hidden_element_for_tablet_pro {
        display:none;
    }
    #hidden_element_for_tablet {
        display:none;
    }
}
   </style>
   <div aria-hidden="true" class="pswp hide" id="gallery" role="dialog" tabindex="-1">
    <div class="pswp__bg">
    </div>
    <div class="pswp__scroll-wrap">
     <div class="pswp__container">
      <div class="pswp__item">
      </div>
      <div class="pswp__item">
      </div>
      <div class="pswp__item">
      </div>
     </div>
     <div class="pswp__ui pswp__ui--hidden">
      <div class="pswp__top-bar">
       <div class="pswp__counter">
       </div>
       <button class="pswp__button pswp__button--close" title="Close (Esc)">
       </button>
       <button class="pswp__button pswp__button--share" title="Share">
       </button>
       <button class="pswp__button pswp__button--fs" title="Toggle fullscreen">
       </button>
       <button class="pswp__button pswp__button--zoom" title="Zoom in/out">
       </button>
       <div class="pswp__preloader">
        <div class="pswp__preloader__icn">
         <div class="pswp__preloader__cut">
          <div class="pswp__preloader__donut">
          </div>
         </div>
        </div>
       </div>
      </div>
      <div class="pswp__share-modal pswp__share-modal--hidden pswp__single-tap">
       <div class="pswp__share-tooltip">
       </div>
      </div>
      <button class="pswp__button pswp__button--arrow--left" title="Previous (arrow left)">
      </button>
      <button class="pswp__button pswp__button--arrow--right" title="Next (arrow right)">
      </button>
      <div class="pswp__caption">
       <div class="pswp__caption__center">
       </div>
      </div>
     </div>
    </div>
   </div>
   <script type="text/javascript">
    window.checkForAdBlockerGA = function(code){
    if(window.ga && code=="1"){
        console.log("sending GA event for adblock");
        window.ga('event',"ad-block","detected","tupaki");
        window.ga('common.send', 'event',"ad-block","detected","tupaki");
        window.ga('common2.send', 'event',"ad-block","detected","tupaki");
    }
}
   </script>
   <script async="" onerror="window.checkForAdBlockerGA('1')" onload="window.checkForAdBlockerGA('0')" src="/scripts/adsbyhocalwiretest.js" type="text/javascript">
   </script>
   <div id="MODAL_DIALOG_PLACEHOLDER">
   </div>
   <div id="generic_style_body_bottom">
   </div>
   <div id="async_body_tags">
   </div>
   <div id="async_body_tags_2">
   </div>
   <link href="https://fonts.googleapis.com" rel="preconnect"/>
   <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
   <link href="https://fonts.googleapis.com/css2?family=Mallanna&amp;display=swap" rel="stylesheet"/>
   <style>
    #left-ad-full-screen,  #right-ad-full-screen{          z-index : 999;  }  #level_14  .card-text-content h3{  font-family: 'Ramabhadra' !important;  }  #photo_stories .reels-heading a.news-link:hover{         font-family: 'Ramabhadra';  }  .entertainment-bg h2{        font-family: 'Ramabhadra';      font-weight: 500;  }  .andhra-content.political-news .andhra-pradesh h4{    line-height: 1.4;  }   #top .reviews .entertainment-scroll .share-content span{     font-weight: 500;    font-family: 'Mallanna';  font-size: 18px;  }  .movie-details-page .constent-review .about-section.reviews p{      font-weight: 500;  font-size: 18px;      font-family: 'Mallanna' !important;  }  .share-content h3{         font-family: 'Ramabhadra';          font-weight: 500  }       .andhra-content.political-news .andhra-pradesh h4{    font-family: 'Ramabhadra';      font-weight: 300;  }  .andhra-district .andhra-pradesh .district .politics-business .content-flex p{    line-height: 16px;  }  .details-page-wrapper .content-flex p{       font-family: 'Mallanna' !important;    font-weight: 500 !important;;  }      .political-news h2{    font-family: 'Ramabhadra';      font-weight: 500;    }    .press-release.andhra-pradesh .content-padding p{  font-family: 'Ramabhadra';  }   .press-release h4{  font-family: 'Ramabhadra';     font-weight: 300;   }   .press-release h4 {     font-weight: 300;      font-size: 19PX;      font-family: 'Ramabhadra';  }  #level_11 .s-description-text{      font-size: 16px;        font-weight: 100;  line-height: 22px !important;  }  #level_7 .reelss .swiper-containernn .swiper-slide h3{         font-family: 'Ramabhadra';  font-weight: 100;      font-size: 17px;  }  #level_7 .reelss .heding h2{      font-family: 'Ramabhadra';  font-weight: 100;      font-size: 17px;  }  #level_7 .reelss .swiper-containernn .swiper-slide.swiper-slide-active h3{      font-family: 'Ramabhadra';  font-weight: 100;      font-size: 17px;  }  #tabs-home3 a.news-link p {  font-size: 18px !important;;  }  #tabs-profile3 a.news-link p {  font-size: 18px !important;;  }   .content-flex .entertainment-content p{  font-weight: 100;  }  .content-flex p{   font-family: 'Ramabhadra';          font-weight: 100;  }  .entertainment-scroll p{      font-weight: 100;  }  #parent .politics-flex p{     font-weight: 100;  }  a.news-link.news-list p {      font-family: 'Ramabhadra', sans-serif !important;      font-size: 17px;  }  div#level_3_2 a.news-link.news-list p {      font-family: 'Roboto', sans-serif !important;  }    a.news-link.atom_link.atom_valid p {      font-family: 'Ramabhadra', sans-serif !important;      font-size: 17px !important;  }  h2.s-amp-h3 {      font-family: 'Ramabhadra', sans-serif;  }  .politics-flex a.news-link p {      font-family: 'Ramabhadra', sans-serif !important;      font-size: 17px !important;  }  a.news-link p {      font-family: 'Ramabhadra', sans-serif !important;      font-size: 17px;  }  div#level_17 .content a.news-link h4 {      font-family: 'Ramabhadra', sans-serif;      font-size: 17px !important;  }  div#level_20 .content a h4 {      font-family: 'Ramabhadra', sans-serif !important;      font-size: 17px;  }  div#level_12 a.news-link h3 {      font-family: 'Ramabhadra', sans-serif;      font-size: 17px;  }   div#level_3_2 a.news-link.news-list p{      font-size: 16px;  }    @media only screen and (max-width: 767px){  a.news-link.news-list p{      font-weight: 400 !important ;  }  .andhra-district .andhra-pradesh .district .politics-business .content-flex p{      font-weight: 400;    }   div#level_3_2 a.news-link.news-list p{      font-size: 18px;  }  #tabs-profile3 a.news-link p{      font-weight: 400 !important;      font-size: 17px !important;  }  #tabs-home3 a.news-link p{      font-weight: 400 !important;      font-size: 17px !important;  }    .content-flex .entertainment-content p{  line-height: 30px;  }    .politics-business .content-flex .politics-flex p {      line-height: 24px;  font-weight: 400;      }      #parent .politics-flex p {      line-height: 24px;  }  .andhra-district .andhra-pradesh .district .politics-business .content-flex p {      line-height: 24px;      }        .reelss .loco_cat.loco_section .swiper-slide h4 {  line-height: 24px;  }    .latest-news-entertainment .entertainment-scroll p{  font-weight: 500;  }  }
   </style>
   <div class="bottom_snackbar_common" id="bottom_snackbar">
    <div id="bottom_snackbar_content">
    </div>
   </div>
   <div class="hide" id="bottom_element_for_popup">
   </div>
   <div class="popup-ad-content-wrap hide exclude-font-change">
    <div class="popup-overlay-bg">
    </div>
    <div class="popup-content-container exclude-font-change">
     <div class="center-content exclude-font-change">
      <div class="content-box exclude-font-change hocal-ad-block hide" id="POPUP_AD_CONTENT">
      </div>
      <div class="close-btn-popup">
       X
      </div>
     </div>
    </div>
   </div>
   <script>
    window.externalFunction = window.externalFunction || {};
   </script>
   <script>
    window.externalFunction['loadScripts'+new Date().getTime()+"-"+Math.floor((Math.random()*10000))] = function() {
    window.Utils.loadScripts('https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?v=1'.split(","),{'callback':function(){
        var event = new CustomEvent("EXTERNAL_RESOURCES_LOADED", { "detail": 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'.split(",")});
        document.dispatchEvent(event);
        if(window['']){
            window['']();
        }
    }});
};
document.addEventListener("ALL_RESOURCE_HTML_LOADED", function(e) {
    for(var k in window.externalFunction){
        if(window.externalFunction[k] && !window.externalFunction[k].loaded){
            window.externalFunction[k].loaded=true;
            window.externalFunction[k]();
        }
    }
    
    
});
if(window.insertLoadTriggered){
    for(var k in window.externalFunction){
        if(window.externalFunction[k] && !window.externalFunction[k].loaded){
            window.externalFunction[k].loaded=true;
            window.externalFunction[k]();
        }
    }
}
   </script>
   <script>
    window.externalFunction = window.externalFunction || {};
   </script>
   <script>
    window.externalFunction['loadScripts'+new Date().getTime()+"-"+Math.floor((Math.random()*10000))] = function() {
    window.Utils.loadScripts('https://www.instagram.com/embed.js?v=1'.split(","),{'callback':function(){
        var event = new CustomEvent("EXTERNAL_RESOURCES_LOADED", { "detail": 'https://www.instagram.com/embed.js'.split(",")});
        document.dispatchEvent(event);
        if(window['']){
            window['']();
        }
    }});
};
document.addEventListener("ALL_RESOURCE_HTML_LOADED", function(e) {
    for(var k in window.externalFunction){
        if(window.externalFunction[k] && !window.externalFunction[k].loaded){
            window.externalFunction[k].loaded=true;
            window.externalFunction[k]();
        }
    }
    
    
});
if(window.insertLoadTriggered){
    for(var k in window.externalFunction){
        if(window.externalFunction[k] && !window.externalFunction[k].loaded){
            window.externalFunction[k].loaded=true;
            window.externalFunction[k]();
        }
    }
}
   </script>
   <script>
    window.externalFunction = window.externalFunction || {};
   </script>
   <script>
    window.externalFunction['loadScripts'+new Date().getTime()+"-"+Math.floor((Math.random()*10000))] = function() {
    window.Utils.loadScripts('https://securepubads.g.doubleclick.net/tag/js/gpt.js?v=1'.split(","),{'callback':function(){
        var event = new CustomEvent("EXTERNAL_RESOURCES_LOADED", { "detail": 'https://securepubads.g.doubleclick.net/tag/js/gpt.js'.split(",")});
        document.dispatchEvent(event);
        if(window['']){
            window['']();
        }
    }});
};
document.addEventListener("ALL_RESOURCE_HTML_LOADED", function(e) {
    for(var k in window.externalFunction){
        if(window.externalFunction[k] && !window.externalFunction[k].loaded){
            window.externalFunction[k].loaded=true;
            window.externalFunction[k]();
        }
    }
    
    
});
if(window.insertLoadTriggered){
    for(var k in window.externalFunction){
        if(window.externalFunction[k] && !window.externalFunction[k].loaded){
            window.externalFunction[k].loaded=true;
            window.externalFunction[k]();
        }
    }
}
   </script>
   <script>
    window.externalFunction = window.externalFunction || {};
   </script>
   <script>
    window.externalFunction['loadScripts'+new Date().getTime()+"-"+Math.floor((Math.random()*10000))] = function() {
    window.Utils.loadScripts('https://platform.twitter.com/widgets.js?v=1'.split(","),{'callback':function(){
        var event = new CustomEvent("EXTERNAL_RESOURCES_LOADED", { "detail": 'https://platform.twitter.com/widgets.js'.split(",")});
        document.dispatchEvent(event);
        if(window['']){
            window['']();
        }
    }});
};
document.addEventListener("ALL_RESOURCE_HTML_LOADED", function(e) {
    for(var k in window.externalFunction){
        if(window.externalFunction[k] && !window.externalFunction[k].loaded){
            window.externalFunction[k].loaded=true;
            window.externalFunction[k]();
        }
    }
    
    
});
if(window.insertLoadTriggered){
    for(var k in window.externalFunction){
        if(window.externalFunction[k] && !window.externalFunction[k].loaded){
            window.externalFunction[k].loaded=true;
            window.externalFunction[k]();
        }
    }
}
   </script>
   <script>
    window.externalFunction = window.externalFunction || {};
   </script>
   <script>
    window.externalFunction['loadScripts'+new Date().getTime()+"-"+Math.floor((Math.random()*10000))] = function() {
    window.Utils.loadScripts('https://cdn.izooto.com/scripts/d8702c295e4a9476c3d31e1694fbb318711922f9.js?v=1'.split(","),{'callback':function(){
        var event = new CustomEvent("EXTERNAL_RESOURCES_LOADED", { "detail": 'https://cdn.izooto.com/scripts/d8702c295e4a9476c3d31e1694fbb318711922f9.js'.split(",")});
        document.dispatchEvent(event);
        if(window['']){
            window['']();
        }
    }});
};
document.addEventListener("ALL_RESOURCE_HTML_LOADED", function(e) {
    for(var k in window.externalFunction){
        if(window.externalFunction[k] && !window.externalFunction[k].loaded){
            window.externalFunction[k].loaded=true;
            window.externalFunction[k]();
        }
    }
    
    
});
if(window.insertLoadTriggered){
    for(var k in window.externalFunction){
        if(window.externalFunction[k] && !window.externalFunction[k].loaded){
            window.externalFunction[k].loaded=true;
            window.externalFunction[k]();
        }
    }
}
   </script>
   <script>
    window.externalFunction = window.externalFunction || {};
   </script>
   <script>
    window.externalFunction['loadScripts'+new Date().getTime()+"-"+Math.floor((Math.random()*10000))] = function() {
    window.Utils.loadScripts('https://t.seedtag.com/t/6537-0291-01.js?v=1'.split(","),{'callback':function(){
        var event = new CustomEvent("EXTERNAL_RESOURCES_LOADED", { "detail": 'https://t.seedtag.com/t/6537-0291-01.js'.split(",")});
        document.dispatchEvent(event);
        if(window['']){
            window['']();
        }
    }});
};
document.addEventListener("ALL_RESOURCE_HTML_LOADED", function(e) {
    for(var k in window.externalFunction){
        if(window.externalFunction[k] && !window.externalFunction[k].loaded){
            window.externalFunction[k].loaded=true;
            window.externalFunction[k]();
        }
    }
    
    
});
if(window.insertLoadTriggered){
    for(var k in window.externalFunction){
        if(window.externalFunction[k] && !window.externalFunction[k].loaded){
            window.externalFunction[k].loaded=true;
            window.externalFunction[k]();
        }
    }
}
   </script>
   <div class="tooltip-wall">
   </div>
   <script>
    window.translationData = {"test-key":"test"};
window.getTranslationValue = function(key,value){
    if(window.translationData && window.translationData[key]){
        return window.translationData[key];
    } else if(value){
        return value;
    } else {
        return key;
    }
}
   </script>
   <style id="generic_style_common_block">
   </style>
   <div class="sidekick-ad-content-wrap exclude-font-change hide">
    <div class="sidekick">
     <div class="sidebar-wrapper">
      <div class="sidebar">
       <div class="content-box exclude-font-change hocal-ad-block hide" id="SIDEKICK_AD_CONTENT">
       </div>
      </div>
      <div class="sidekick-nav-btn">
       <img alt="sidekick" class="sidekick-nav-img" src="/images/sidekick-open.png" title="sidkick"/>
      </div>
     </div>
    </div>
   </div>
   <script>
    window.isIOSBrowser = function(){
    var isIOS1 = /iPad|iPhone|iPod/.test(navigator.platform) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
    var isIOS2 = ['iPad Simulator','iPhone Simulator','iPod Simulator','iPad','iPhone','iPod'].includes(navigator.platform) || (navigator.userAgent.includes("Mac") && "ontouchend" in document)
    var isSafari = /^((?!chrome|android).)*safari/i.test(navigator.userAgent);
    var isSafari2 = navigator.vendor && navigator.vendor.indexOf('Apple') > -1 && navigator.userAgent && navigator.userAgent.indexOf('CriOS') == -1 && navigator.userAgent.indexOf('FxiOS') == -1;
    return isIOS1 || isIOS2 || isSafari || isSafari2;
}
if(window.isIOSBrowser()){
    document.body.className += ' ios-device';
}
   </script>
  </div>
  <script>
   document.addEventListener("RESOURCES_LOADED", function(e) {
    loadCssNow();
});
document.addEventListener("EXTRA_PAGE_RESOURCES_LOADED", function(e) {
    loadCssNow();
});
function loadCssNow(){
     !function(a){"use strict";var b=function(b,c,d){function j(a){return e.body?a():void setTimeout(function(){j(a)})}function l(){f.addEventListener&&f.removeEventListener("load",l),f.media=d||"all"}var g,e=a.document,f=e.createElement("link");if(c)g=c;else{var h=(e.body||e.getElementsByTagName("head")[0]).childNodes;g=h[h.length-1]}var i=e.styleSheets;f.rel="stylesheet",f.href=b,f.media="only x",j(function(){g.parentNode.insertBefore(f,c?g:g.nextSibling)});var k=function(a){for(var b=f.href,c=i.length;c--;)if(i[c].href===b)return a();setTimeout(function(){k(a)})};return f.addEventListener&&f.addEventListener("load",l),f.onloadcssdefined=k,k(l),f};"undefined"!=typeof exports?exports.loadCSS=b:a.loadCSS=b}("undefined"!=typeof global?global:window),function(a){if(a.loadCSS){var b=loadCSS.relpreload={};if(b.support=function(){try{return a.document.createElement("link").relList.supports("preload")}catch(a){return!1}},b.poly=function(){for(var b=a.document.getElementsByTagName("link"),c=0;c<b.length;c++){var d=b[c];"preload"===d.rel&&"style"===d.getAttribute("as")&&(a.loadCSS(d.href,d),d.rel=null)}},!b.support()){b.poly();var c=a.setInterval(b.poly,300);a.addEventListener&&a.addEventListener("load",function(){a.clearInterval(c)}),a.attachEvent&&a.attachEvent("onload",function(){a.clearInterval(c)})}}}(window);           
}
  </script>
  <link as="style" href="/styles/themetealfile.min.8b61cce3.css" onload="this.rel='stylesheet';if(window.oncssLoad)window.oncssLoad();" rel="preload"/>
  <script>
   (function () {
  if ( typeof window.CustomEvent === "function" ) return false;
  function CustomEvent ( event, params ) {
    params = params || { bubbles: false, cancelable: false, detail: undefined };
    var evt = document.createEvent( 'CustomEvent' );
    evt.initCustomEvent( event, params.bubbles, params.cancelable, params.detail );
    return evt;
  }
  CustomEvent.prototype = window.Event.prototype;
  window.CustomEvent = CustomEvent;
})();
var loadDeferredStyles = function() { 
  var head = document.getElementsByTagName("head")[0];
  var s = document.createElement("script");
      s.type = "text/javascript";
      s.src = "/scripts/hocalwirecommlightp1.min.38c2b3fd.js";
      //- s.async = true;
      s.defer = true;
      s.addEventListener("load", function (e) {
          var s1 = document.createElement("script");
          s1.type = "text/javascript";
          s1.src = "/scripts/themetealjs.min.702fa29d.js";
          //- s1.async = true;
          s1.defer = true;
          head.appendChild(s1);
          s1.addEventListener("load", function (e) {
              if(!window.insertLoadTriggered && window.triggerInsertLoad && document.readyState=="complete") {
                  window.triggerInsertLoad();
              }
              if("true"){
                var event2 = new CustomEvent("THEME_LAZY_RESOURCES_LOADED", { "detail": "ALL DEPENDENCIES LOADED" });
                document.dispatchEvent(event2);
                window.themeLazyResourceLoaded=true;
              }
              var event = new CustomEvent("RESOURCES_LOADED", { "detail": "ALL DEPENDENCIES LOADED" });
              document.dispatchEvent(event);
              
              window.themeResourceLoaded=true;
          });
      }, false);
      
  head.appendChild(s);
  
};
var part1Loaded = false;
var loadDeferredStylesPart2 = function() { 
  if(!part1Loaded){
    setTimeout(loadDeferredStylesPart2,100);
    return;
  }
  var head = document.getElementsByTagName("head")[0];
  if(''){
    if("/styles/themetealfile.min.8b61cce3.css"){
      var cssFile3 = document.createElement("link");
      cssFile3.href="/styles/themetealfile.min.8b61cce3.css";
      cssFile3.rel="stylesheet";
      head.appendChild(cssFile3);
    }
  }
  if(""){
    var cssFile2 = document.createElement("link");
    cssFile2.href="";
    cssFile2.rel="stylesheet";
    head.appendChild(cssFile2);
  }
  if(''){
    if(""){
      var cssFile4 = document.createElement("link");
      cssFile4.href="";
      cssFile4.rel="stylesheet";
      head.appendChild(cssFile4);
    }
  }
  
  var s = document.createElement("script");
      s.type = "text/javascript";
      s.src = "/scripts/hocalwirecommlightp2.min.b654f6c8.js";
      //- s.async = true;
      s.defer = true;
      s.addEventListener("load", function (e) {
          var s1 = document.createElement("script");
          s1.type = "text/javascript";
          s1.src = "/scripts/themetealjs.min.702fa29d.js";
          //- s1.async = true;
          s1.defer = true;
          head.appendChild(s1);
          s1.addEventListener("load", function (e) {
              if(!window.insertLoadTriggered && window.triggerInsertLoad && document.readyState=="complete") {
                  window.triggerInsertLoad();
              }
              if("true"){
                var event2 = new CustomEvent("THEME_LAZY_RESOURCES_LOADED", { "detail": "ALL DEPENDENCIES LOADED" });
                document.dispatchEvent(event2);
                window.themeLazyResourceLoaded=true;
              }
              var event = new CustomEvent("RESOURCES_LOADED", { "detail": "ALL DEPENDENCIES LOADED" });
              document.dispatchEvent(event);
              
              window.themeResourceLoaded=true;
          });
      }, false);
      
  head.appendChild(s);
  
};

var loadDeferredStylesPart1 = function() { 
  var head = document.getElementsByTagName("head")[0];
  var s = document.createElement("script");
      s.type = "text/javascript";
      s.src = "/scripts/hocalwirecommlightp1.min.38c2b3fd.js";
      //- s.async = true;
      s.defer = true;
  head.appendChild(s);
  s.addEventListener("load", function (e) {
    part1Loaded=true;
      //- window.setTimeout(loadDeferredStylesPart2, 1000);
  }, false);
  
};
var rafLoaded=false;
function loadThemeResourcesFinalOnRaf(loadEventName){
  if(rafLoaded){
    return;
  }
  rafLoaded=true;
  var rafFound=false;
  var raf = requestAnimationFrame || mozRequestAnimationFrame || webkitRequestAnimationFrame || msRequestAnimationFrame;
  if (raf) {
    rafFound =true;
    raf(function() { window.setTimeout(function(){
      loadDeferredStylesPart1();
      if(loadEventName){
        window.setTimeout(loadDeferredStylesPart2, window.scriptLoadDelay);
      }
    },0); });
  }
  if(window.addEventListener){
  
      window.addEventListener('load', function() {
        if(!rafFound){
          window.setTimeout(loadDeferredStylesPart1, 0); 
        }
        window.setTimeout(loadDeferredStylesPart2, window.scriptLoadDelay);
        
      });
  } else {
      window.attachEvent('load', function() {
        if(!rafFound){
            window.setTimeout(loadDeferredStylesPart1, 0); 
        }
          window.setTimeout(loadDeferredStylesPart2, window.scriptLoadDelay);
      });
      
  }
}
function loadConditionalForTriggerEvent(loadEventName){
    var screenSizeLoadCond = "600";
    if(screenSizeLoadCond && parseInt(screenSizeLoadCond)<window.screen.width){
      loadEventName="";
    }
    if(loadEventName){
      if(loadEventName=="true"){
        loadEventName = ["keydown", "mousedown", "mousemove", "touchmove", "touchstart", "touchend", "wheel"];
      } else {
        loadEventName = loadEventName.split(",");
      }
      for(var i=0;i<loadEventName.length;i++){
        if(window.addEventListener){
            window.addEventListener(loadEventName[i], function() {
                loadThemeResourcesFinalOnRaf(loadEventName);
            });
        } else {
            window.attachEvent(loadEventName[i], function() {
                loadThemeResourcesFinalOnRaf(loadEventName);
            });
            
        }
      }
    } else {
      loadThemeResourcesFinalOnRaf();
    }
}
if("true"){
  if("/scripts/hocalwirecommlightp2.min.b654f6c8.js"){
    var loadEventName = "";
    loadConditionalForTriggerEvent(loadEventName)
  } else {
    if(window.addEventListener){
        window.addEventListener('load', function() {
            window.setTimeout(loadDeferredStyles, window.scriptLoadDelay);
            
        });
    } else {
        window.attachEvent('load', function() {
            window.setTimeout(loadDeferredStyles, window.scriptLoadDelay);
        });
        
    }
  }
  
} else {
  var raf = requestAnimationFrame || mozRequestAnimationFrame ||
      webkitRequestAnimationFrame || msRequestAnimationFrame;
  if (raf) raf(function() { window.setTimeout(loadDeferredStyles, 0); });
  else window.addEventListener('load', loadDeferredStyles);
}
  </script>
  <div class="modal hide" id="news_on_exit">
  </div>
  <script>
   var cx = '';
if(cx){
    var gcse = document.createElement('script');
    gcse.type = 'text/javascript';
    gcse.async = true;
    gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(gcse, s);
}
  </script>
  <script>
   if (navigator.serviceWorker && !navigator.serviceWorker.controller) {
     navigator.serviceWorker.register("/service-worker.js").then(function(reg) {
     });
}
  </script>
  <script override-script="true">
   window.galleryLoaded=false;
document.addEventListener("GALLERY_RESOURCES_LOADED", function(e) {
    window.galleryLoaded=true;
});
  </script>
  <script override-script="true">
   function getElm(elem){
    return function(){
        return $(elem);
    }
}
window.createGallerySliderAjax = function(element){
    createInlineStorySliders(element);   
}
function createInlineStorySliders(element){
    var items = element ? element.find(".image-slider-wrapper .all-slider-items-wrapper:not(.already-init)") : $(".image-slider-wrapper .all-slider-items-wrapper:not(.already-init)");
    var count = (window.loadedGalleryCount || $(".image-slider-wrapper .all-slider-items-wrapper.already-init").length) +1;
    window.loadedGalleryCount = count;
    if(!items || !items.length){
        items = element ? element.find(".gallery-slider-wrapper .details-page-slider-wrapper:not(.already-init)") : $(".gallery-slider-wrapper .details-page-slider-wrapper:not(.already-init)");
        var count1 = $(".gallery-slider-wrapper .details-page-slider-wrapper.already-init").length + 1;
        count = count+count1;
        window.loadedGalleryCount = count;
    }
    
    if(items.length){
        for(var i=0;i<items.length;i++){
        
            var $elem = getElm($(items[i]))();
            if(!$elem.responsiveSlides){
                continue;
            }
            $elem.addClass("already-init");
            $elem.attr("data-namespace-count",count);
            count = count+1;
            $elem.responsiveSlides({
                speed: 800,
                nav:true,
                pager:false,
                pause:true,
                auto : window.autoSlideGallery || false,
                timeout : parseInt(window.autoSlideGalleryTimeout || 4000)
            });
            var images = $elem.find(".image-slider-item-wrapper img");
            if(!images.length){
                images = $elem.find("li img");
            }   
            
            var width = $elem.width();
            var minH = (width * 3)/5;
            for(var j=0;j<images.length;j++){
                var img = $(images[j]);
                var hh = img.height();
                if(hh && hh>minH){
                    minH = hh;
                }
            }
            minH = parseInt(minH);
            var id = $elem.closest(".image-slider-wrapper").attr("id");
            var style = "#"+id+".image-slider-wrapper .image-slider-item-wrapper{height:"+minH+"px !important;}";
            var fontStyle = $("#custom-font-size-"+id);
            if(!fontStyle || !fontStyle.length){
                fontStyle = $("<style id='custom-font-size-"+id+"'></style>");
                $("body").append(fontStyle);
            }
            fontStyle.html(style);
            initPhotoSwipeFromDOM("#"+id);
        }
    }
}
function createSingleGalleryElement(id){
    //- debugger;
    return function(){
        id=id+"";
        var hasType = id.indexOf("@")>-1 ? id.split("@")[1] : 'grid';
        if(hasType){
            id = id.split("@")[0];
        }
        var $el = $(id);
        if(!id || !$el.length || id=="undefined"){
            return;
        }
        if($el.hasClass("already-init")){
            return;
        }
        $el.addClass("already-init");
        var count = window.loadedGalleryCount || 1;
        count = count+1;
        window.loadedGalleryCount=count;
        $el.attr("data-namespace-count",count);
        var width = $el.attr("data-width") || 300
        if(hasType && hasType=="slide"){
            $el.responsiveSlides({
                speed: 800,
                nav:true,
                pager:false,
                pause:true,
                auto : window.autoSlideGallery || false,
                timeout : parseInt(window.autoSlideGalleryTimeout || 4000)
            });
            
        } else {
            var forceAspectRatioWidth = $el.attr("data-aspectratiowidth");
            if(forceAspectRatioWidth){
                var images = $el.find("figure img");
                for(var i=0;i<images.length;i++){
                    var img = $(images[i]);
                    var widthTemp = width;
                    var forceAspectRatioHeight = $el.attr("data-aspectratioheight");
                    if(forceAspectRatioHeight){
                        var ar = parseFloat(forceAspectRatioWidth/forceAspectRatioHeight);
                        var eheight = parseInt(widthTemp/ar);
                        var style2 = img.attr("style");
                        style2+=";height:"+eheight+"px;object-fit:cover;";
                        img.attr("style",style2);
                    }
                }
            }
            if($el.width()-40 < width){
                width = $el.width()-40;
            }
            var maxImgWidth = $el.find("figure").width();
            if(maxImgWidth-40 <  width ){
                width = maxImgWidth-40;
            }
            $el.boxify({width: width+"px"});
            var forceAspectRatioWidth = $el.attr("data-aspectratiowidth");
            if(forceAspectRatioWidth){
                var images = $el.find("figure img");
                for(var i=0;i<images.length;i++){
                    var img = $(images[i]);
                    var widthTemp = img.width();
                    var forceAspectRatioHeight = $el.attr("data-aspectratioheight");
                    if(forceAspectRatioHeight){
                        var ar = parseFloat(forceAspectRatioWidth/forceAspectRatioHeight);
                        var eheight = parseInt(widthTemp/ar);
                        var style2 = img.attr("style");
                        style2+=";height:"+eheight+"px;object-fit:cover;";
                        img.attr("style",style2);
                    }
                }
            }
            var height2=0;
            var els  = $el.find(".height-gallery-element");
            // alert("h1:"+height1+"els length"+els.length);
            setTimeout(function(){
                for(var i=0;i<els.length;i++){
                    var h = $(els[i]).offset().top;
                    // alert("h:"+h +" max height:"+height2);
                    if(h>height2){
                        height2=h;
                        // alert(height2);
                    }
                }
                var height1 = $el.offset().top;
                var diff = (height2-height1);
                var style = $el.attr("style");
                style+=";height:"+(diff+30)+"px;";
                $el.attr("style",style);
                
                
            },500);
            
        }
        
        initPhotoSwipeFromDOM(id);
        
        
    };
}
function initGallery(){

    var galleryIds = window.galleryIds || [];
    var count = window.allGalleryCount || 1;
    if(count && galleryIds.length<count) {
        setTimeout(initGallery,2000);
        return;
    }
    for(var j=0;j<galleryIds.length;j++){
        createSingleGalleryElement(galleryIds[j])();
    }
    setTimeout(function(){
        window.galleryIds = [];
    },2000); 
}
document.addEventListener("GALLERY_RESOURCES_LOADED", function(e) {
    var event = new CustomEvent("EXTRA_PAGE_RESOURCES_LOADED", { "detail": "ALL DEPENDENCIES LOADED" });
    document.dispatchEvent(event);
    initGallery();
    createInlineStorySliders();
    
});
  </script>
  <link as="style" href="/styles/galleryresources.min.4682527e.css" onload="this.rel='stylesheet'" override-script="true" rel="preload"/>
  <script override-script="true">
   var loadDeferredStylesGallery = function() {
    var head = document.getElementsByTagName("head")[0];
    var s = document.createElement("script");
    s.type = "text/javascript";
    s.src = "https://www.youtube.com/player_api";
    s.addEventListener("load", function (e) {
        var s1 = document.createElement("script");
        s1.type = "text/javascript";
        s1.src = "/scripts/allgalleryjs.min.474e2a08.js";
        head.appendChild(s1);
        s1.addEventListener("load", function (e) {
            var event = new CustomEvent("GALLERY_RESOURCES_LOADED", { "detail": "ALL GALLERY DEPENDENCIES LOADED"});
            document.dispatchEvent(event);
        });
    }, false);
    
    head.appendChild(s);
    
};
document.addEventListener("RESOURCES_LOADED", function(e) {
    loadDeferredStylesGallery();
});
if(window.themeResourceLoaded){
    loadDeferredStylesGallery();
}
  </script>
  <div class="hide" id="floating_button">
  </div>
  <div class="hide" id="sticky-bottom-element">
  </div>
  <div class="recommended-list-temp-pad hide">
  </div>
  <script>
   window.leadGeneration = ''
  </script>
  <div class="article-page hide" id="sticky_container">
  </div>
  <div class="hide" id="bottom_extra_content">
  </div>
  <style>
   /* deepika tupaki changes */
@media only screen and (min-width: 992px) {
    .live-tabs.photo-gallery .andhra-content .tabs-wrapper {
        height: 100%;
    }
}

.live-tabs.photo-gallery .tab-content .content-flex img {
    margin: 0;
    min-height: 300px;
    height: 100%;
    width: 180px;
    object-fit: cover;
}

.movie-details-page span.tags-wrapper button {
    margin-right: 6px;
}

/* end */


/* from Async Body Tags */
/*Destop larg Homepage*/
/*Trending*/
.details-page-wrapper .entertainment-telugu.trending .generic-right .entertainment-scroll img {
    min-height: inherit;
}

/**/

.grid-block-for-images {
    display: grid !important;
    grid-template-columns: 75px auto;
}

.navbar-fixed-top,
header .navbar-fixed-bottom {
    position: relative;
    /* position: fixed; */
    top: 0;
    right: 0;
    left: 0;
}

header .navbar-default .topbar-logo {
    background: #fff;
    padding: 10px 27px;
    display: flex;
    flex-wrap: inherit;
    align-items: center;
    justify-content: space-between;
    max-width: 1534px;
    margin-right: auto;
    margin-left: auto;
}


article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
    display: block;
    position: relative;
    top: 0;
    right: 0;
    left: 0;
}

.website-wrapper {
    display: flex;
    justify-content: space-between;

    position: relative;
    padding: 10px 0;
    background: #d6d6d6;
    flex-wrap: inherit;
    max-width: 1534px;
    margin-right: auto;
    margin-left: auto;
}

.footer-section {
    position: relative;
    padding: 10px 0 0;
    display: block;
    top: 0;
    right: 0;
    left: 0;
}

.container-footer {
    margin: auto;
    flex-wrap: inherit;
    max-width: 1073px;
    margin-right: auto;
    margin-left: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    padding: 10px 0;
}

.copyright-area {
    display: block;
    position: relative;
    top: 0;
    right: 0;
    left: 0;
}

.container-fluid {
    flex-wrap: inherit;
    max-width: 1534px;
    justify-content: space-between;
    align-items: center;
    position: relative;
}

/*End*/


@media(min-width:280px) and (max-width:736px) {
    .entertainment-telugu .view-all a {
        background: #c4c4c4;
    }

    .reelss.video-stories {
        padding: 0 0 40px;
    }

    .politics-business.topnews-left {
        margin: 0px 0 0;
    }

    /*.andhra-content.office img{
    display: none;
}*/

    /*.view-all-link img{
    display: none !important;
}*/

    .entertainment-telugu .view-all {
        padding: 20px 0 20px;
        background: #FFF;
    }

    .entertainment-telugu .view-all a {
        font-size: 17px;
    }

    .politics-business.topnews-left {
        margin: 0px 0 0 !important;
    }

    .latest-news-entertainment.latest-news-block {
        margin: 0px 0 0 !important
    }

    .grid-block-for-images {
        display: grid !important;
        grid-template-columns: 75px auto;
    }

    .live-tabs a {
        margin: 0px 0px;
    }

    .entertainment-telugu.spacing a {
        width: auto;
    }

    .content-tupaki-block {
        padding: 0 0px 0;
    }

    .news-category .box {
        margin-left: 10px;
        padding: 0px;
    }

    #parent {
        display: block;
    }

    .reelss.stories .loco_cat.loco_section .slide-fit img {
        width: 100%;
    }

    /*Footer Youtube*/

    .home-page .video-gallery-cls {
        grid-template-columns: 1fr;
    }

    .container-footer {
        flex-wrap: wrap;
    }

    .andhra-content.office .politics-business .politics-flex {
        width: -webkit-fill-available;
    }

    /*Social icon*/
    .political-news .share {
        display: block;
    }

    .details-page-wrapper .share .ind-social-cover .ind-social-ul li.ind-social-li,
    .movie-details-page .share .ind-social-cover .ind-social-ul li.ind-social-li {
        margin: 5px 2px;
    }


    /*slider Arrow*/
    .indrani .indrani-scroll .poll #carousel .carousel-control-next {
        left: 30px;
    }

    /*box office*/
    .andhra-content.office .reelss-ul a {
        display: block;
    }

    .reelss.video-stories .reelss-ul a {
        display: block;
    }

    /*End*/

}




@media(min-width:768px) and (max-width:820px) {
    #level_4_2_ad_2 {
        min-height: 570px !important;
        display: block !important;
    }

    .left-add {
        display: none;
    }

    .right-add {
        display: none;
    }

    .full-width {
        width: 95%;
    }

    .entertain-block {
        width: 100%;
    }

    .latest-news-block {
        display: block;
    }

    .telugu-block-entertainment {
        width: 100%;
        margin: 0 !important;
    }

    .tupaki-excusive {
        width: 100%;
        display: block;
        background-color: #FFF;
    }

    .excusive-inside {
        width: 100%;
        display: block;
    }

    .content-tupaki-block {
        padding: 0 0px 0;
    }


    .news-category .box {
        margin: 0;
        padding: 0 22px 0;
    }

    .slider-img-inside .loco_cat.loco_section .swiper-slide {
        height: 328px;
    }

    .inside-boxover {
        overflow: inherit !important;
    }

    .reelss.stories .loco_cat.loco_section .slide-fit img {
        width: 71%;
        object-fit: cover;
    }

    .tab-panel.is-active.top-1 {

        width: 100%;

    }

    .tab-content .content-flex img {
        width: 100%;
    }

    /*Box Office*/
    .politics-business.news {
        width: 100%;
        top: 23px;
    }


    .andhra-content.office .andhra-pradesh .politics-business {
        width: 100%;
        float: left;
    }

    /*End*/


    /*Top10*/

    .andhra-pradesh .politics-business {
        width: 100%;
    }

    .ott-bg {
        margin: 20px 0 0;
    }

    .heding.news-heding.desk {
        display: none;
    }

    /*End*/

    /*heading*/

    .heding {
        padding: 0 20px 0;
    }

    /*movie Reviews*/
    .entertainment-telugu {
        width: 100%;
    }

    .latest-news-entertainment {
        display: block;
    }

    .latest-news-entertainment.indrani-scroll .entertainment-telugu .entertainment-flex {
        padding: 0 15px 0;
    }

    .latest-news-entertainment.indrani-scroll .entertainment-telugu.spacing {
        overflow: inherit;
    }

    .indrani .indrani-scroll .poll #carousel .carousel-control-next {
        right: 38px;
    }

    .indrani .indrani-scroll .poll #carousel .carousel-control-prev {
        left: 38px;
    }

    .tabs-all .box {
        margin: 0px 15px 0;
    }

    /*End*/

    /*innerpages entertainment*/



    .live-ads {
        display: none;
    }

    .live-tabs {
        width: 100%;
    }

    .sub-flex ul {
        padding: 0 10px 0;

    }

    .andhra-district .andhra-pradesh .district .content-flex {
        max-width: 100%;
    }


    /*Telangana*/


    .andhra-district .andhra-pradesh .district-min {
        width: 100%;
        object-fit: cover;
    }

    .andhra-pradesh .district {
        display: flex;
        width: 100%;
    }

    .andhra-pradesh {
        display: block;
    }


    /*PRESS RELEASE*/
    .press-release .heding h2 {
        text-align: justify;
    }

    .content-flex p {
        width: 100%;
    }

    /*End*/
    /*Boxoffice*/
    .andhra-content.office .andhra-pradesh {
        float: left;
    }

    /*End*/
    .politics-business.topnews-left {
        margin: 588px 0 0;
        background: #FFF;
        padding: 0 11px 0;
    }


    /*Homepage*/

    .andhra-pradesh .politics-business {
        width: 32%;
        top: 0;
        float: left;
        margin: 0;
    }

    .latest-news-entertainment.latest-news-block {
        margin: 336px 0 0;
    }

    .noru {
        width: 100%;
    }

    .entertainment-scroll p {
        width: 500px;
    }

    .indrani {
        height: 785px;
    }

    .indrani h3 {
        line-height: 30px;
    }

    .entertainment-telugu.spacing a {
        width: 100%;
    }

    .indrani .indrani-scroll .poll #carousel .entertainment-flexs img {
        width: 78px;
        height: 104px;
    }

    .slider-mini {
        margin: 305px 0 0;
    }

    .indrani .indrani-scroll .poll #carousel .carousel-control-next {
        left: 20px;
    }

    /*PhotoPlay*/
    .s-amp-content-block {
        background: #FFF;
    }

    /*End*/

}




@media(max-width:820px) {

    .politics-business.topnews-left {
        margin: 40px 0 0;
        background: #FFF;
        padding: 0 11px 0;
    }

    .latest-news-entertainment.latest-news-block {
        margin: 0px 0 0;
    }

    .most-pp {
        margin: 138px 0 0;
    }

    .home-page .video-gallery-cls {
        grid-template-columns: 1fr;
    }

}

@media(max-width:768px) {
    .politics-business.topnews-left {
        margin: 596px 0 0;
        background: #FFF;
        padding: 0 11px 0;
    }

    .latest-news-entertainment.latest-news-block {

        margin: 400px 0 0;

    }

    .latest-news-entertainment {
        margin: 4px 0 0;
    }

    .latest-news-entertainment.upto-off {
        margin: 4px 0 0;
    }

    .politics-business.topnews-left {
        margin: 596px 0 0;
    }
}

@media(max-width:844px) {
    .politics-business.topnews-left {
        margin: 596px 0 0;
    }
}

/* from async body tags */
  </style>
  <div class="last-from-body-bottom" id="last-from-body-bottom">
  </div>
 </body>
</html>

[Finished in 997ms]
"""


href_pattern = r'href=["\'](https?://content[^"\']+)["\']'


hrefs = re.findall(href_pattern, html_content)


for href in hrefs:
    print(href)