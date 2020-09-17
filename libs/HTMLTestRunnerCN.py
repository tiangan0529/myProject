'''# <!DOCTYPE html>
# <html lang="zh-CN">
# <head data-suburl="">
# 	<meta charset="utf-8">
# 	<meta name="viewport" content="width=device-width, initial-scale=1">
# 	<meta http-equiv="x-ua-compatible" content="ie=edge">
# 	<title>wulinhao/apitest: 自动化api测试 - report/HTMLTestRunnerCN.py at local_test -  apitest - Gitea: Git with a cup of tea</title>
# 	<link rel="manifest" href="/manifest.json" crossorigin="use-credentials">
#
# 	<script>
# 		if ('serviceWorker' in navigator) {
# 			navigator.serviceWorker.register('/serviceworker.js').then(function(registration) {
#
# 				console.info('ServiceWorker registration successful with scope: ', registration.scope);
# 			}, function(err) {
#
# 				console.info('ServiceWorker registration failed: ', err);
# 			});
# 		}
# 	</script>
#
# 	<meta name="theme-color" content="#6cc644">
# 	<meta name="author" content="wulinhao" />
# 	<meta name="description" content="apitest - 自动化api测试" />
# 	<meta name="keywords" content="go,git,self-hosted,gitea">
# 	<meta name="referrer" content="no-referrer" />
# 	<meta name="_csrf" content="5BDMVY9M-HUhmi0zqpcG5_MVzkI6MTU5ODYwMzEwODE1NjY5ODc3Nw" />
# 	<meta name="_suburl" content="" />
#
# 		<meta name="_uid" content="26" />
#
#
#
#
#
# 	<script>
# 	/*
# 	@licstart  The following is the entire license notice for the
#         JavaScript code in this page.
#
# 	Copyright (c) 2016 The Gitea Authors
# 	Copyright (c) 2015 The Gogs Authors
#
# 	Permission is hereby granted, free of charge, to any person obtaining a copy
# 	of this software and associated documentation files (the "Software"), to deal
# 	in the Software without restriction, including without limitation the rights
# 	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# 	copies of the Software, and to permit persons to whom the Software is
# 	furnished to do so, subject to the following conditions:
#
# 	The above copyright notice and this permission notice shall be included in
# 	all copies or substantial portions of the Software.
#
# 	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# 	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# 	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# 	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# 	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# 	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# 	THE SOFTWARE.
# 	---
# 	Licensing information for additional javascript libraries can be found at:
# 	  {{StaticUrlPrefix}}/vendor/librejs.html
#
# 	@licend  The above is the entire license notice
#         for the JavaScript code in this page.
# 	*/
# 	</script>
#
# 	<link rel="shortcut icon" href="/img/favicon.png" />
# 	<link rel="mask-icon" href="/img/gitea-safari.svg" color="#609926">
# 	<link rel="preload" href="/vendor/assets/font-awesome/css/font-awesome.min.css" as="style" onload="this.rel='stylesheet'">
# 	<noscript><link rel="stylesheet" href="/vendor/assets/font-awesome/css/font-awesome.min.css"></noscript>
# 	<link rel="stylesheet" href="/vendor/assets/octicons/octicons.min.css">
#
#
#
#
#
#
# 	<link rel="stylesheet" href="/vendor/plugins/fomantic/semantic.min.css?v=2150802f140babb659fb7f59b121e3e9">
# 	<link rel="stylesheet" href="/css/index.css?v=2150802f140babb659fb7f59b121e3e9">
# 	<noscript>
# 		<style>
# 			.dropdown:hover > .menu { display: block; }
# 			.ui.secondary.menu .dropdown.item > .menu { margin-top: 0; }
# 		</style>
# 	</noscript>
#
#
# 	<link rel="stylesheet" href="/vendor/plugins/highlight/github.css">
#
#
#
#
#
# 	<style class="list-search-style"></style>
#
# 	<script src="/vendor/plugins/promise-polyfill/polyfill.min.js"></script>
# 	<script src="/vendor/plugins/cssrelpreload/loadCSS.min.js"></script>
# 	<script src="/vendor/plugins/cssrelpreload/cssrelpreload.min.js"></script>
#
#
# 		<meta property="og:title" content="apitest" />
# 		<meta property="og:url" content="https://code.dtedu.com/wulinhao/apitest" />
#
# 			<meta property="og:description" content="自动化api测试" />
#
#
# 	<meta property="og:type" content="object" />
# 	<meta property="og:image" content="https://code.dtedu.com/user/avatar/wulinhao/-1" />
#
# <meta property="og:site_name" content="Gitea: Git with a cup of tea" />
#
#
#
#
# </head>
# <body>
#
#
# 	<div class="full height">
# 		<noscript>使用 JavaScript能使本网站更好的工作。</noscript>
#
#
#
#
# 			<div class="ui top secondary stackable main menu following bar light">
# 				<div class="ui container" id="navbar">
# 	<div class="item brand" style="justify-content: space-between;">
# 		<a href="/">
# 			<img class="ui mini image" src="/img/gitea-sm.png">
# 		</a>
# 		<div class="ui basic icon button mobile-only" id="navbar-expand-toggle">
# 			<i class="sidebar icon"></i>
# 		</div>
# 	</div>
#
#
# 		<a class="item " href="/">首页</a>
# 		<a class="item " href="/issues">工单管理</a>
# 		<a class="item " href="/pulls">合并请求</a>
# 		<a class="item " href="/milestones">里程碑</a>
# 		<a class="item " href="/explore/repos">探索</a>
#
#
#
#
#
#
#
# 		<div class="right stackable menu">
# 			<a href="/notifications" class="item poping up" data-content='通知' data-variation="tiny inverted">
# 				<span class="text">
# 					<i class="fitted octicon octicon-bell"></i>
# 					<span class="sr-mobile-only">通知</span>
#
#
# 				</span>
# 			</a>
#
# 			<div class="ui dropdown jump item poping up" data-content="创建…" data-variation="tiny inverted">
# 				<span class="text">
# 					<i class="fitted octicon octicon-plus"></i>
# 					<span class="sr-mobile-only">创建…</span>
# 					<i class="fitted octicon octicon-triangle-down not-mobile"></i>
# 				</span>
# 				<div class="menu">
# 					<a class="item" href="/repo/create">
# 						<i class="octicon octicon-plus"></i> 创建仓库
# 					</a>
# 					<a class="item" href="/repo/migrate">
# 						<i class="octicon octicon-repo-clone"></i> 迁移外部仓库
# 					</a>
#
# 					<a class="item" href="/org/create">
# 						<i class="octicon octicon-organization"></i> 创建组织
# 					</a>
#
# 				</div>
# 			</div>
#
# 			<div class="ui dropdown jump item poping up" tabindex="-1" data-content="个人信息和配置" data-variation="tiny inverted">
# 				<span class="text">
# 					<img class="ui tiny avatar image" src="/user/avatar/zhongfeng/-1">
# 					<span class="sr-only">个人信息和配置</span>
# 					<span class="mobile-only">zhongfeng</span>
# 					<i class="fitted octicon octicon-triangle-down not-mobile" tabindex="-1"></i>
# 				</span>
# 				<div class="menu user-menu" tabindex="-1">
# 					<div class="ui header">
# 						已登录用户 <strong>zhongfeng</strong>
# 					</div>
#
# 					<div class="divider"></div>
# 					<a class="item" href="/zhongfeng">
# 						<i class="octicon octicon-person"></i>
# 						个人信息
# 					</a>
# 					<a class="item" href="/zhongfeng?tab=stars">
# 						<i class="octicon octicon-star"></i>
# 						已点赞
# 					</a>
# 					<a class=" item" href="/user/settings">
# 						<i class="octicon octicon-settings"></i>
# 						设置
# 					</a>
# 					<a class="item" target="_blank" rel="noopener noreferrer" href="https://docs.gitea.io">
# 						<i class="octicon octicon-question"></i>
# 						帮助
# 					</a>
#
#
# 					<div class="divider"></div>
# 					<a class="item link-action" href data-url="/user/logout" data-redirect="/">
# 						<i class="octicon octicon-sign-out"></i>
# 						退出
# 					</a>
# 				</div>
# 			</div>
# 		</div>
#
#
# </div>
#
# 			</div>
#
#
#
# <div class="repository file list">
# 	<div class="header-wrapper">
#
# 	<div class="ui container">
# 		<div class="repo-header">
# 			<div class="ui huge breadcrumb repo-title">
#
# 				<i class="mega-octicon octicon-lock"></i>
#
# 				<a href="/wulinhao">wulinhao</a>
# 				<div class="divider"> / </div>
# 				<a href="/wulinhao/apitest">apitest</a>
#
#
#
#
#
#
# 			</div>
#
# 				<div class="repo-buttons">
# 					<form method="post" action="/wulinhao/apitest/action/watch?redirect_to=%2fwulinhao%2fapitest%2fsrc%2fbranch%2flocal_test%2freport%2fHTMLTestRunnerCN.py">
# 						<input type="hidden" name="_csrf" value="5BDMVY9M-HUhmi0zqpcG5_MVzkI6MTU5ODYwMzEwODE1NjY5ODc3Nw">
# 						<div class="ui labeled button" tabindex="0">
# 							<button type="submit" class="ui compact basic button">
# 								<i class="icon fa-eye-slash"></i>关注
# 							</button>
# 							<a class="ui basic label" href="/wulinhao/apitest/watchers">
# 								1
# 							</a>
# 						</div>
# 					</form>
# 					<form method="post" action="/wulinhao/apitest/action/star?redirect_to=%2fwulinhao%2fapitest%2fsrc%2fbranch%2flocal_test%2freport%2fHTMLTestRunnerCN.py">
# 						<input type="hidden" name="_csrf" value="5BDMVY9M-HUhmi0zqpcG5_MVzkI6MTU5ODYwMzEwODE1NjY5ODc3Nw">
# 						<div class="ui labeled button" tabindex="0">
# 							<button type="submit" class="ui compact basic button">
# 								<i class="icon star outline"></i>点赞
# 							</button>
# 							<a class="ui basic label" href="/wulinhao/apitest/stars">
# 								0
# 							</a>
# 						</div>
# 					</form>
#
# 						<div class="ui labeled button " tabindex="0">
# 							<a class="ui compact basic button " href="/repo/fork/34" data-position="top center" data-variation="tiny">
# 								<i class="octicon octicon-repo-forked"></i>派生
# 							</a>
# 							<a class="ui basic label" href="/wulinhao/apitest/forks">
# 								0
# 							</a>
# 						</div>
#
# 				</div>
#
# 		</div>
# 	</div>
#
# 	<div class="ui tabs container">
#
# 			<div class="ui tabular stackable menu navbar">
#
# 				<a class="active item" href="/wulinhao/apitest/src/branch/local_test">
# 					<i class="octicon octicon-code"></i> 代码
# 				</a>
#
#
#
# 					<a class=" item" href="/wulinhao/apitest/issues">
# 						<i class="octicon octicon-issue-opened"></i> 工单 <span class="ui gray small label">0</span>
# 					</a>
#
#
#
#
#
# 					<a class=" item" href="/wulinhao/apitest/pulls">
# 						<i class="octicon octicon-git-pull-request"></i> 合并请求 <span class="ui gray small label">0</span>
# 					</a>
#
#
#
# 				<a class=" item" href="/wulinhao/apitest/releases">
# 					<i class="octicon octicon-tag"></i> 版本发布 <span class="ui gray small label">0</span>
# 				</a>
#
#
#
# 					<a class=" item" href="/wulinhao/apitest/wiki" >
# 						<i class="octicon octicon-book"></i> 百科
# 					</a>
#
#
#
# 					<a class=" item" href="/wulinhao/apitest/activity">
# 						<i class="octicon octicon-pulse"></i> 动态
# 					</a>
#
#
#
#
#
# 			</div>
#
# 	</div>
# 	<div class="ui tabs divider"></div>
# </div>
#
# 	<div class="ui container">
#
#
#
#
# 		<div class="ui repo-description">
# 			<div id="repo-desc">
# 				<span class="description has-emoji">自动化api测试</span>
# 				<a class="link" href=""></a>
# 			</div>
#
# 		</div>
# 		<div class="ui" id="repo-topics">
#
#
# 		</div>
#
# 		<div class="hide" id="validate_prompt">
# 			<span id="count_prompt">您最多选择25个主题</span>
# 			<span id="format_prompt">主题必须以字母或数字开头，可以包含连字符 (-)，并且长度不得超过35个字符</span>
# 		</div>
#
# 		<div class="ui segment sub-menu">
# 	<div class="ui two horizontal center link list">
#
# 			<div class="item">
# 				<a class="ui" href="/wulinhao/apitest/commits/branch/local_test"><i class="octicon octicon-history"></i> <b>35</b> 提交</a>
# 			</div>
#
#
# 			<div class="item">
# 				<a class="ui" href="/wulinhao/apitest/branches/"><i class="octicon octicon-git-branch"></i> <b>2</b> 分支</a>
# 			</div>
# 			<div class="item">
# 				<a class="ui" href="#"><i class="octicon octicon-database"></i> <b>879KB</b></a>
# 			</div>
#
# 	</div>
# </div>
#
# 		<div class="ui stackable secondary menu mobile--margin-between-items mobile--no-negative-margins">
# 			<div class="fitted item choose reference">
# 	<div class="ui floating filter dropdown custom" data-can-create-branch="false" data-no-results="未找到结果">
# 		<div class="ui basic small compact button" @click="menuVisible = !menuVisible" @keyup.enter="menuVisible = !menuVisible">
# 			<span class="text">
# 				<i class="octicon octicon-git-branch"></i>
# 				分支:
# 				<strong>local_test</strong>
# 			</span>
# 			<i class="dropdown icon"></i>
# 		</div>
# 		<div class="data" style="display: none" data-mode="branches">
#
# 				<div class="item branch selected" data-url="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py">local_test</div>
#
# 				<div class="item branch " data-url="/wulinhao/apitest/src/branch/master/report/HTMLTestRunnerCN.py">master</div>
#
#
# 		</div>
# 		<div class="menu transition" :class="{visible: menuVisible}" v-if="menuVisible" v-cloak>
# 			<div class="ui icon search input">
# 				<i class="filter icon"></i>
# 				<input name="search" ref="searchField" v-model="searchTerm" @keydown="keydown($event)" placeholder="过滤分支或标签...">
# 			</div>
# 			<div class="header branch-tag-choice">
# 				<div class="ui grid">
# 					<div class="two column row">
# 						<a class="reference column" href="#" @click="mode = 'branches'; focusSearchField()">
# 							<span class="text" :class="{black: mode == 'branches'}">
# 								<i class="octicon octicon-git-branch"></i> 分支列表
# 							</span>
# 						</a>
# 						<a class="reference column" href="#" @click="mode = 'tags'; focusSearchField()">
# 							<span class="text" :class="{black: mode == 'tags'}">
# 								<i class="reference tags icon"></i> 标签列表
# 							</span>
# 						</a>
# 					</div>
# 				</div>
# 			</div>
# 			<div class="scrolling menu" ref="scrollContainer">
# 				<div v-for="(item, index) in filteredItems" :key="item.name" class="item" :class="{selected: item.selected, active: active == index}" @click="selectItem(item)" :ref="'listItem' + index">${ item.name }</div>
# 				<div class="item" v-if="showCreateNewBranch" :class="{active: active == filteredItems.length}" :ref="'listItem' + filteredItems.length">
# 					<a href="#" @click="createNewBranch()">
# 						<div>
# 							<i class="octicon octicon-git-branch"></i>
# 							创建分支 <strong>${ searchTerm }</strong>
# 						</div>
# 						<div class="text small">
#
# 								从 &#39;local_test&#39;
#
# 						</div>
# 					</a>
# 					<form ref="newBranchForm" action="/wulinhao/apitest/branches/_new/branch/local_test" method="post">
# 						<input type="hidden" name="_csrf" value="5BDMVY9M-HUhmi0zqpcG5_MVzkI6MTU5ODYwMzEwODE1NjY5ODc3Nw">
# 						<input type="hidden" name="new_branch_name" v-model="searchTerm">
# 					</form>
# 				</div>
# 			</div>
# 			<div class="message" v-if="showNoResults">${ noResults }</div>
# 		</div>
# 	</div>
# </div>
#
#
#
#
#
# 				<div class="fitted item"><span class="ui breadcrumb repo-path"><a class="section" href="/wulinhao/apitest/src/branch/local_test" title="apitest">apitest</a><span class="divider">/</span><span class="section"><a href="/wulinhao/apitest/src/branch/local_test/report" title="report">report</a></span><span class="divider">/</span><span class="active section" title="HTMLTestRunnerCN.py">HTMLTestRunnerCN.py</span></span></div>
#
# 			<div class="right fitted item" id="file-buttons">
# 				<div class="ui tiny blue buttons">
#
#
#
#
#
# 				</div>
#
# 			</div>
# 			<div class="fitted item">
#
# 			</div>
# 			<div class="fitted item">
#
#
#
# 			</div>
# 		</div>
#
# 			<div class="tab-size-8 non-diff-file-content">
# 	<h4 class="file-header ui top attached header">
# 		<div class="file-header-left">
#
# 				<div class="file-info text grey normal mono">
#
# 						<div class="file-info-entry">
# 							1045 行
# 						</div>
#
#
# 						<div class="file-info-entry">
# 							34KB
# 						</div>
#
#
# 				</div>
#
# 		</div>
#
# 		<div class="file-header-right">
# 			<div class="ui right file-actions">
# 				<div class="ui buttons">
# 					<a class="ui button" href="/wulinhao/apitest/raw/branch/local_test/report/HTMLTestRunnerCN.py">原始文件</a>
#
# 						<a class="ui button" href="/wulinhao/apitest/src/commit/8075751a756014d85bd6d943207c4e950f3a76fd/report/HTMLTestRunnerCN.py">永久链接</a>
#
#
# 						<a class="ui button" href="/wulinhao/apitest/blame/branch/local_test/report/HTMLTestRunnerCN.py">Blame</a>
#
# 					<a class="ui button" href="/wulinhao/apitest/commits/branch/local_test/report/HTMLTestRunnerCN.py">文件历史</a>
# 				</div>
#
#
# 						<i class="octicon octicon-pencil btn-octicon poping up disabled" data-content="您必须在派生这个仓库才能对此文件进行修改操作" data-position="bottom center" data-variation="tiny inverted"></i>
#
#
# 						<i class="octicon octicon-trashcan btn-octicon poping up disabled" data-content="您必须具有写权限才能对此文件进行修改操作。" data-position="bottom center" data-variation="tiny inverted"></i>
#
#
# 			</div>
# 		</div>
#
# 	</h4>
# 	<div class="ui attached table unstackable segment">
# 		<div class="file-view code-view has-emoji">
#
# 				<table>
# 					<tbody>
# 						<tr>
#
# 							<td class="lines-num"><span id="L1" data-line-number="1"></span><span id="L2" data-line-number="2"></span><span id="L3" data-line-number="3"></span><span id="L4" data-line-number="4"></span><span id="L5" data-line-number="5"></span><span id="L6" data-line-number="6"></span><span id="L7" data-line-number="7"></span><span id="L8" data-line-number="8"></span><span id="L9" data-line-number="9"></span><span id="L10" data-line-number="10"></span><span id="L11" data-line-number="11"></span><span id="L12" data-line-number="12"></span><span id="L13" data-line-number="13"></span><span id="L14" data-line-number="14"></span><span id="L15" data-line-number="15"></span><span id="L16" data-line-number="16"></span><span id="L17" data-line-number="17"></span><span id="L18" data-line-number="18"></span><span id="L19" data-line-number="19"></span><span id="L20" data-line-number="20"></span><span id="L21" data-line-number="21"></span><span id="L22" data-line-number="22"></span><span id="L23" data-line-number="23"></span><span id="L24" data-line-number="24"></span><span id="L25" data-line-number="25"></span><span id="L26" data-line-number="26"></span><span id="L27" data-line-number="27"></span><span id="L28" data-line-number="28"></span><span id="L29" data-line-number="29"></span><span id="L30" data-line-number="30"></span><span id="L31" data-line-number="31"></span><span id="L32" data-line-number="32"></span><span id="L33" data-line-number="33"></span><span id="L34" data-line-number="34"></span><span id="L35" data-line-number="35"></span><span id="L36" data-line-number="36"></span><span id="L37" data-line-number="37"></span><span id="L38" data-line-number="38"></span><span id="L39" data-line-number="39"></span><span id="L40" data-line-number="40"></span><span id="L41" data-line-number="41"></span><span id="L42" data-line-number="42"></span><span id="L43" data-line-number="43"></span><span id="L44" data-line-number="44"></span><span id="L45" data-line-number="45"></span><span id="L46" data-line-number="46"></span><span id="L47" data-line-number="47"></span><span id="L48" data-line-number="48"></span><span id="L49" data-line-number="49"></span><span id="L50" data-line-number="50"></span><span id="L51" data-line-number="51"></span><span id="L52" data-line-number="52"></span><span id="L53" data-line-number="53"></span><span id="L54" data-line-number="54"></span><span id="L55" data-line-number="55"></span><span id="L56" data-line-number="56"></span><span id="L57" data-line-number="57"></span><span id="L58" data-line-number="58"></span><span id="L59" data-line-number="59"></span><span id="L60" data-line-number="60"></span><span id="L61" data-line-number="61"></span><span id="L62" data-line-number="62"></span><span id="L63" data-line-number="63"></span><span id="L64" data-line-number="64"></span><span id="L65" data-line-number="65"></span><span id="L66" data-line-number="66"></span><span id="L67" data-line-number="67"></span><span id="L68" data-line-number="68"></span><span id="L69" data-line-number="69"></span><span id="L70" data-line-number="70"></span><span id="L71" data-line-number="71"></span><span id="L72" data-line-number="72"></span><span id="L73" data-line-number="73"></span><span id="L74" data-line-number="74"></span><span id="L75" data-line-number="75"></span><span id="L76" data-line-number="76"></span><span id="L77" data-line-number="77"></span><span id="L78" data-line-number="78"></span><span id="L79" data-line-number="79"></span><span id="L80" data-line-number="80"></span><span id="L81" data-line-number="81"></span><span id="L82" data-line-number="82"></span><span id="L83" data-line-number="83"></span><span id="L84" data-line-number="84"></span><span id="L85" data-line-number="85"></span><span id="L86" data-line-number="86"></span><span id="L87" data-line-number="87"></span><span id="L88" data-line-number="88"></span><span id="L89" data-line-number="89"></span><span id="L90" data-line-number="90"></span><span id="L91" data-line-number="91"></span><span id="L92" data-line-number="92"></span><span id="L93" data-line-number="93"></span><span id="L94" data-line-number="94"></span><span id="L95" data-line-number="95"></span><span id="L96" data-line-number="96"></span><span id="L97" data-line-number="97"></span><span id="L98" data-line-number="98"></span><span id="L99" data-line-number="99"></span><span id="L100" data-line-number="100"></span><span id="L101" data-line-number="101"></span><span id="L102" data-line-number="102"></span><span id="L103" data-line-number="103"></span><span id="L104" data-line-number="104"></span><span id="L105" data-line-number="105"></span><span id="L106" data-line-number="106"></span><span id="L107" data-line-number="107"></span><span id="L108" data-line-number="108"></span><span id="L109" data-line-number="109"></span><span id="L110" data-line-number="110"></span><span id="L111" data-line-number="111"></span><span id="L112" data-line-number="112"></span><span id="L113" data-line-number="113"></span><span id="L114" data-line-number="114"></span><span id="L115" data-line-number="115"></span><span id="L116" data-line-number="116"></span><span id="L117" data-line-number="117"></span><span id="L118" data-line-number="118"></span><span id="L119" data-line-number="119"></span><span id="L120" data-line-number="120"></span><span id="L121" data-line-number="121"></span><span id="L122" data-line-number="122"></span><span id="L123" data-line-number="123"></span><span id="L124" data-line-number="124"></span><span id="L125" data-line-number="125"></span><span id="L126" data-line-number="126"></span><span id="L127" data-line-number="127"></span><span id="L128" data-line-number="128"></span><span id="L129" data-line-number="129"></span><span id="L130" data-line-number="130"></span><span id="L131" data-line-number="131"></span><span id="L132" data-line-number="132"></span><span id="L133" data-line-number="133"></span><span id="L134" data-line-number="134"></span><span id="L135" data-line-number="135"></span><span id="L136" data-line-number="136"></span><span id="L137" data-line-number="137"></span><span id="L138" data-line-number="138"></span><span id="L139" data-line-number="139"></span><span id="L140" data-line-number="140"></span><span id="L141" data-line-number="141"></span><span id="L142" data-line-number="142"></span><span id="L143" data-line-number="143"></span><span id="L144" data-line-number="144"></span><span id="L145" data-line-number="145"></span><span id="L146" data-line-number="146"></span><span id="L147" data-line-number="147"></span><span id="L148" data-line-number="148"></span><span id="L149" data-line-number="149"></span><span id="L150" data-line-number="150"></span><span id="L151" data-line-number="151"></span><span id="L152" data-line-number="152"></span><span id="L153" data-line-number="153"></span><span id="L154" data-line-number="154"></span><span id="L155" data-line-number="155"></span><span id="L156" data-line-number="156"></span><span id="L157" data-line-number="157"></span><span id="L158" data-line-number="158"></span><span id="L159" data-line-number="159"></span><span id="L160" data-line-number="160"></span><span id="L161" data-line-number="161"></span><span id="L162" data-line-number="162"></span><span id="L163" data-line-number="163"></span><span id="L164" data-line-number="164"></span><span id="L165" data-line-number="165"></span><span id="L166" data-line-number="166"></span><span id="L167" data-line-number="167"></span><span id="L168" data-line-number="168"></span><span id="L169" data-line-number="169"></span><span id="L170" data-line-number="170"></span><span id="L171" data-line-number="171"></span><span id="L172" data-line-number="172"></span><span id="L173" data-line-number="173"></span><span id="L174" data-line-number="174"></span><span id="L175" data-line-number="175"></span><span id="L176" data-line-number="176"></span><span id="L177" data-line-number="177"></span><span id="L178" data-line-number="178"></span><span id="L179" data-line-number="179"></span><span id="L180" data-line-number="180"></span><span id="L181" data-line-number="181"></span><span id="L182" data-line-number="182"></span><span id="L183" data-line-number="183"></span><span id="L184" data-line-number="184"></span><span id="L185" data-line-number="185"></span><span id="L186" data-line-number="186"></span><span id="L187" data-line-number="187"></span><span id="L188" data-line-number="188"></span><span id="L189" data-line-number="189"></span><span id="L190" data-line-number="190"></span><span id="L191" data-line-number="191"></span><span id="L192" data-line-number="192"></span><span id="L193" data-line-number="193"></span><span id="L194" data-line-number="194"></span><span id="L195" data-line-number="195"></span><span id="L196" data-line-number="196"></span><span id="L197" data-line-number="197"></span><span id="L198" data-line-number="198"></span><span id="L199" data-line-number="199"></span><span id="L200" data-line-number="200"></span><span id="L201" data-line-number="201"></span><span id="L202" data-line-number="202"></span><span id="L203" data-line-number="203"></span><span id="L204" data-line-number="204"></span><span id="L205" data-line-number="205"></span><span id="L206" data-line-number="206"></span><span id="L207" data-line-number="207"></span><span id="L208" data-line-number="208"></span><span id="L209" data-line-number="209"></span><span id="L210" data-line-number="210"></span><span id="L211" data-line-number="211"></span><span id="L212" data-line-number="212"></span><span id="L213" data-line-number="213"></span><span id="L214" data-line-number="214"></span><span id="L215" data-line-number="215"></span><span id="L216" data-line-number="216"></span><span id="L217" data-line-number="217"></span><span id="L218" data-line-number="218"></span><span id="L219" data-line-number="219"></span><span id="L220" data-line-number="220"></span><span id="L221" data-line-number="221"></span><span id="L222" data-line-number="222"></span><span id="L223" data-line-number="223"></span><span id="L224" data-line-number="224"></span><span id="L225" data-line-number="225"></span><span id="L226" data-line-number="226"></span><span id="L227" data-line-number="227"></span><span id="L228" data-line-number="228"></span><span id="L229" data-line-number="229"></span><span id="L230" data-line-number="230"></span><span id="L231" data-line-number="231"></span><span id="L232" data-line-number="232"></span><span id="L233" data-line-number="233"></span><span id="L234" data-line-number="234"></span><span id="L235" data-line-number="235"></span><span id="L236" data-line-number="236"></span><span id="L237" data-line-number="237"></span><span id="L238" data-line-number="238"></span><span id="L239" data-line-number="239"></span><span id="L240" data-line-number="240"></span><span id="L241" data-line-number="241"></span><span id="L242" data-line-number="242"></span><span id="L243" data-line-number="243"></span><span id="L244" data-line-number="244"></span><span id="L245" data-line-number="245"></span><span id="L246" data-line-number="246"></span><span id="L247" data-line-number="247"></span><span id="L248" data-line-number="248"></span><span id="L249" data-line-number="249"></span><span id="L250" data-line-number="250"></span><span id="L251" data-line-number="251"></span><span id="L252" data-line-number="252"></span><span id="L253" data-line-number="253"></span><span id="L254" data-line-number="254"></span><span id="L255" data-line-number="255"></span><span id="L256" data-line-number="256"></span><span id="L257" data-line-number="257"></span><span id="L258" data-line-number="258"></span><span id="L259" data-line-number="259"></span><span id="L260" data-line-number="260"></span><span id="L261" data-line-number="261"></span><span id="L262" data-line-number="262"></span><span id="L263" data-line-number="263"></span><span id="L264" data-line-number="264"></span><span id="L265" data-line-number="265"></span><span id="L266" data-line-number="266"></span><span id="L267" data-line-number="267"></span><span id="L268" data-line-number="268"></span><span id="L269" data-line-number="269"></span><span id="L270" data-line-number="270"></span><span id="L271" data-line-number="271"></span><span id="L272" data-line-number="272"></span><span id="L273" data-line-number="273"></span><span id="L274" data-line-number="274"></span><span id="L275" data-line-number="275"></span><span id="L276" data-line-number="276"></span><span id="L277" data-line-number="277"></span><span id="L278" data-line-number="278"></span><span id="L279" data-line-number="279"></span><span id="L280" data-line-number="280"></span><span id="L281" data-line-number="281"></span><span id="L282" data-line-number="282"></span><span id="L283" data-line-number="283"></span><span id="L284" data-line-number="284"></span><span id="L285" data-line-number="285"></span><span id="L286" data-line-number="286"></span><span id="L287" data-line-number="287"></span><span id="L288" data-line-number="288"></span><span id="L289" data-line-number="289"></span><span id="L290" data-line-number="290"></span><span id="L291" data-line-number="291"></span><span id="L292" data-line-number="292"></span><span id="L293" data-line-number="293"></span><span id="L294" data-line-number="294"></span><span id="L295" data-line-number="295"></span><span id="L296" data-line-number="296"></span><span id="L297" data-line-number="297"></span><span id="L298" data-line-number="298"></span><span id="L299" data-line-number="299"></span><span id="L300" data-line-number="300"></span><span id="L301" data-line-number="301"></span><span id="L302" data-line-number="302"></span><span id="L303" data-line-number="303"></span><span id="L304" data-line-number="304"></span><span id="L305" data-line-number="305"></span><span id="L306" data-line-number="306"></span><span id="L307" data-line-number="307"></span><span id="L308" data-line-number="308"></span><span id="L309" data-line-number="309"></span><span id="L310" data-line-number="310"></span><span id="L311" data-line-number="311"></span><span id="L312" data-line-number="312"></span><span id="L313" data-line-number="313"></span><span id="L314" data-line-number="314"></span><span id="L315" data-line-number="315"></span><span id="L316" data-line-number="316"></span><span id="L317" data-line-number="317"></span><span id="L318" data-line-number="318"></span><span id="L319" data-line-number="319"></span><span id="L320" data-line-number="320"></span><span id="L321" data-line-number="321"></span><span id="L322" data-line-number="322"></span><span id="L323" data-line-number="323"></span><span id="L324" data-line-number="324"></span><span id="L325" data-line-number="325"></span><span id="L326" data-line-number="326"></span><span id="L327" data-line-number="327"></span><span id="L328" data-line-number="328"></span><span id="L329" data-line-number="329"></span><span id="L330" data-line-number="330"></span><span id="L331" data-line-number="331"></span><span id="L332" data-line-number="332"></span><span id="L333" data-line-number="333"></span><span id="L334" data-line-number="334"></span><span id="L335" data-line-number="335"></span><span id="L336" data-line-number="336"></span><span id="L337" data-line-number="337"></span><span id="L338" data-line-number="338"></span><span id="L339" data-line-number="339"></span><span id="L340" data-line-number="340"></span><span id="L341" data-line-number="341"></span><span id="L342" data-line-number="342"></span><span id="L343" data-line-number="343"></span><span id="L344" data-line-number="344"></span><span id="L345" data-line-number="345"></span><span id="L346" data-line-number="346"></span><span id="L347" data-line-number="347"></span><span id="L348" data-line-number="348"></span><span id="L349" data-line-number="349"></span><span id="L350" data-line-number="350"></span><span id="L351" data-line-number="351"></span><span id="L352" data-line-number="352"></span><span id="L353" data-line-number="353"></span><span id="L354" data-line-number="354"></span><span id="L355" data-line-number="355"></span><span id="L356" data-line-number="356"></span><span id="L357" data-line-number="357"></span><span id="L358" data-line-number="358"></span><span id="L359" data-line-number="359"></span><span id="L360" data-line-number="360"></span><span id="L361" data-line-number="361"></span><span id="L362" data-line-number="362"></span><span id="L363" data-line-number="363"></span><span id="L364" data-line-number="364"></span><span id="L365" data-line-number="365"></span><span id="L366" data-line-number="366"></span><span id="L367" data-line-number="367"></span><span id="L368" data-line-number="368"></span><span id="L369" data-line-number="369"></span><span id="L370" data-line-number="370"></span><span id="L371" data-line-number="371"></span><span id="L372" data-line-number="372"></span><span id="L373" data-line-number="373"></span><span id="L374" data-line-number="374"></span><span id="L375" data-line-number="375"></span><span id="L376" data-line-number="376"></span><span id="L377" data-line-number="377"></span><span id="L378" data-line-number="378"></span><span id="L379" data-line-number="379"></span><span id="L380" data-line-number="380"></span><span id="L381" data-line-number="381"></span><span id="L382" data-line-number="382"></span><span id="L383" data-line-number="383"></span><span id="L384" data-line-number="384"></span><span id="L385" data-line-number="385"></span><span id="L386" data-line-number="386"></span><span id="L387" data-line-number="387"></span><span id="L388" data-line-number="388"></span><span id="L389" data-line-number="389"></span><span id="L390" data-line-number="390"></span><span id="L391" data-line-number="391"></span><span id="L392" data-line-number="392"></span><span id="L393" data-line-number="393"></span><span id="L394" data-line-number="394"></span><span id="L395" data-line-number="395"></span><span id="L396" data-line-number="396"></span><span id="L397" data-line-number="397"></span><span id="L398" data-line-number="398"></span><span id="L399" data-line-number="399"></span><span id="L400" data-line-number="400"></span><span id="L401" data-line-number="401"></span><span id="L402" data-line-number="402"></span><span id="L403" data-line-number="403"></span><span id="L404" data-line-number="404"></span><span id="L405" data-line-number="405"></span><span id="L406" data-line-number="406"></span><span id="L407" data-line-number="407"></span><span id="L408" data-line-number="408"></span><span id="L409" data-line-number="409"></span><span id="L410" data-line-number="410"></span><span id="L411" data-line-number="411"></span><span id="L412" data-line-number="412"></span><span id="L413" data-line-number="413"></span><span id="L414" data-line-number="414"></span><span id="L415" data-line-number="415"></span><span id="L416" data-line-number="416"></span><span id="L417" data-line-number="417"></span><span id="L418" data-line-number="418"></span><span id="L419" data-line-number="419"></span><span id="L420" data-line-number="420"></span><span id="L421" data-line-number="421"></span><span id="L422" data-line-number="422"></span><span id="L423" data-line-number="423"></span><span id="L424" data-line-number="424"></span><span id="L425" data-line-number="425"></span><span id="L426" data-line-number="426"></span><span id="L427" data-line-number="427"></span><span id="L428" data-line-number="428"></span><span id="L429" data-line-number="429"></span><span id="L430" data-line-number="430"></span><span id="L431" data-line-number="431"></span><span id="L432" data-line-number="432"></span><span id="L433" data-line-number="433"></span><span id="L434" data-line-number="434"></span><span id="L435" data-line-number="435"></span><span id="L436" data-line-number="436"></span><span id="L437" data-line-number="437"></span><span id="L438" data-line-number="438"></span><span id="L439" data-line-number="439"></span><span id="L440" data-line-number="440"></span><span id="L441" data-line-number="441"></span><span id="L442" data-line-number="442"></span><span id="L443" data-line-number="443"></span><span id="L444" data-line-number="444"></span><span id="L445" data-line-number="445"></span><span id="L446" data-line-number="446"></span><span id="L447" data-line-number="447"></span><span id="L448" data-line-number="448"></span><span id="L449" data-line-number="449"></span><span id="L450" data-line-number="450"></span><span id="L451" data-line-number="451"></span><span id="L452" data-line-number="452"></span><span id="L453" data-line-number="453"></span><span id="L454" data-line-number="454"></span><span id="L455" data-line-number="455"></span><span id="L456" data-line-number="456"></span><span id="L457" data-line-number="457"></span><span id="L458" data-line-number="458"></span><span id="L459" data-line-number="459"></span><span id="L460" data-line-number="460"></span><span id="L461" data-line-number="461"></span><span id="L462" data-line-number="462"></span><span id="L463" data-line-number="463"></span><span id="L464" data-line-number="464"></span><span id="L465" data-line-number="465"></span><span id="L466" data-line-number="466"></span><span id="L467" data-line-number="467"></span><span id="L468" data-line-number="468"></span><span id="L469" data-line-number="469"></span><span id="L470" data-line-number="470"></span><span id="L471" data-line-number="471"></span><span id="L472" data-line-number="472"></span><span id="L473" data-line-number="473"></span><span id="L474" data-line-number="474"></span><span id="L475" data-line-number="475"></span><span id="L476" data-line-number="476"></span><span id="L477" data-line-number="477"></span><span id="L478" data-line-number="478"></span><span id="L479" data-line-number="479"></span><span id="L480" data-line-number="480"></span><span id="L481" data-line-number="481"></span><span id="L482" data-line-number="482"></span><span id="L483" data-line-number="483"></span><span id="L484" data-line-number="484"></span><span id="L485" data-line-number="485"></span><span id="L486" data-line-number="486"></span><span id="L487" data-line-number="487"></span><span id="L488" data-line-number="488"></span><span id="L489" data-line-number="489"></span><span id="L490" data-line-number="490"></span><span id="L491" data-line-number="491"></span><span id="L492" data-line-number="492"></span><span id="L493" data-line-number="493"></span><span id="L494" data-line-number="494"></span><span id="L495" data-line-number="495"></span><span id="L496" data-line-number="496"></span><span id="L497" data-line-number="497"></span><span id="L498" data-line-number="498"></span><span id="L499" data-line-number="499"></span><span id="L500" data-line-number="500"></span><span id="L501" data-line-number="501"></span><span id="L502" data-line-number="502"></span><span id="L503" data-line-number="503"></span><span id="L504" data-line-number="504"></span><span id="L505" data-line-number="505"></span><span id="L506" data-line-number="506"></span><span id="L507" data-line-number="507"></span><span id="L508" data-line-number="508"></span><span id="L509" data-line-number="509"></span><span id="L510" data-line-number="510"></span><span id="L511" data-line-number="511"></span><span id="L512" data-line-number="512"></span><span id="L513" data-line-number="513"></span><span id="L514" data-line-number="514"></span><span id="L515" data-line-number="515"></span><span id="L516" data-line-number="516"></span><span id="L517" data-line-number="517"></span><span id="L518" data-line-number="518"></span><span id="L519" data-line-number="519"></span><span id="L520" data-line-number="520"></span><span id="L521" data-line-number="521"></span><span id="L522" data-line-number="522"></span><span id="L523" data-line-number="523"></span><span id="L524" data-line-number="524"></span><span id="L525" data-line-number="525"></span><span id="L526" data-line-number="526"></span><span id="L527" data-line-number="527"></span><span id="L528" data-line-number="528"></span><span id="L529" data-line-number="529"></span><span id="L530" data-line-number="530"></span><span id="L531" data-line-number="531"></span><span id="L532" data-line-number="532"></span><span id="L533" data-line-number="533"></span><span id="L534" data-line-number="534"></span><span id="L535" data-line-number="535"></span><span id="L536" data-line-number="536"></span><span id="L537" data-line-number="537"></span><span id="L538" data-line-number="538"></span><span id="L539" data-line-number="539"></span><span id="L540" data-line-number="540"></span><span id="L541" data-line-number="541"></span><span id="L542" data-line-number="542"></span><span id="L543" data-line-number="543"></span><span id="L544" data-line-number="544"></span><span id="L545" data-line-number="545"></span><span id="L546" data-line-number="546"></span><span id="L547" data-line-number="547"></span><span id="L548" data-line-number="548"></span><span id="L549" data-line-number="549"></span><span id="L550" data-line-number="550"></span><span id="L551" data-line-number="551"></span><span id="L552" data-line-number="552"></span><span id="L553" data-line-number="553"></span><span id="L554" data-line-number="554"></span><span id="L555" data-line-number="555"></span><span id="L556" data-line-number="556"></span><span id="L557" data-line-number="557"></span><span id="L558" data-line-number="558"></span><span id="L559" data-line-number="559"></span><span id="L560" data-line-number="560"></span><span id="L561" data-line-number="561"></span><span id="L562" data-line-number="562"></span><span id="L563" data-line-number="563"></span><span id="L564" data-line-number="564"></span><span id="L565" data-line-number="565"></span><span id="L566" data-line-number="566"></span><span id="L567" data-line-number="567"></span><span id="L568" data-line-number="568"></span><span id="L569" data-line-number="569"></span><span id="L570" data-line-number="570"></span><span id="L571" data-line-number="571"></span><span id="L572" data-line-number="572"></span><span id="L573" data-line-number="573"></span><span id="L574" data-line-number="574"></span><span id="L575" data-line-number="575"></span><span id="L576" data-line-number="576"></span><span id="L577" data-line-number="577"></span><span id="L578" data-line-number="578"></span><span id="L579" data-line-number="579"></span><span id="L580" data-line-number="580"></span><span id="L581" data-line-number="581"></span><span id="L582" data-line-number="582"></span><span id="L583" data-line-number="583"></span><span id="L584" data-line-number="584"></span><span id="L585" data-line-number="585"></span><span id="L586" data-line-number="586"></span><span id="L587" data-line-number="587"></span><span id="L588" data-line-number="588"></span><span id="L589" data-line-number="589"></span><span id="L590" data-line-number="590"></span><span id="L591" data-line-number="591"></span><span id="L592" data-line-number="592"></span><span id="L593" data-line-number="593"></span><span id="L594" data-line-number="594"></span><span id="L595" data-line-number="595"></span><span id="L596" data-line-number="596"></span><span id="L597" data-line-number="597"></span><span id="L598" data-line-number="598"></span><span id="L599" data-line-number="599"></span><span id="L600" data-line-number="600"></span><span id="L601" data-line-number="601"></span><span id="L602" data-line-number="602"></span><span id="L603" data-line-number="603"></span><span id="L604" data-line-number="604"></span><span id="L605" data-line-number="605"></span><span id="L606" data-line-number="606"></span><span id="L607" data-line-number="607"></span><span id="L608" data-line-number="608"></span><span id="L609" data-line-number="609"></span><span id="L610" data-line-number="610"></span><span id="L611" data-line-number="611"></span><span id="L612" data-line-number="612"></span><span id="L613" data-line-number="613"></span><span id="L614" data-line-number="614"></span><span id="L615" data-line-number="615"></span><span id="L616" data-line-number="616"></span><span id="L617" data-line-number="617"></span><span id="L618" data-line-number="618"></span><span id="L619" data-line-number="619"></span><span id="L620" data-line-number="620"></span><span id="L621" data-line-number="621"></span><span id="L622" data-line-number="622"></span><span id="L623" data-line-number="623"></span><span id="L624" data-line-number="624"></span><span id="L625" data-line-number="625"></span><span id="L626" data-line-number="626"></span><span id="L627" data-line-number="627"></span><span id="L628" data-line-number="628"></span><span id="L629" data-line-number="629"></span><span id="L630" data-line-number="630"></span><span id="L631" data-line-number="631"></span><span id="L632" data-line-number="632"></span><span id="L633" data-line-number="633"></span><span id="L634" data-line-number="634"></span><span id="L635" data-line-number="635"></span><span id="L636" data-line-number="636"></span><span id="L637" data-line-number="637"></span><span id="L638" data-line-number="638"></span><span id="L639" data-line-number="639"></span><span id="L640" data-line-number="640"></span><span id="L641" data-line-number="641"></span><span id="L642" data-line-number="642"></span><span id="L643" data-line-number="643"></span><span id="L644" data-line-number="644"></span><span id="L645" data-line-number="645"></span><span id="L646" data-line-number="646"></span><span id="L647" data-line-number="647"></span><span id="L648" data-line-number="648"></span><span id="L649" data-line-number="649"></span><span id="L650" data-line-number="650"></span><span id="L651" data-line-number="651"></span><span id="L652" data-line-number="652"></span><span id="L653" data-line-number="653"></span><span id="L654" data-line-number="654"></span><span id="L655" data-line-number="655"></span><span id="L656" data-line-number="656"></span><span id="L657" data-line-number="657"></span><span id="L658" data-line-number="658"></span><span id="L659" data-line-number="659"></span><span id="L660" data-line-number="660"></span><span id="L661" data-line-number="661"></span><span id="L662" data-line-number="662"></span><span id="L663" data-line-number="663"></span><span id="L664" data-line-number="664"></span><span id="L665" data-line-number="665"></span><span id="L666" data-line-number="666"></span><span id="L667" data-line-number="667"></span><span id="L668" data-line-number="668"></span><span id="L669" data-line-number="669"></span><span id="L670" data-line-number="670"></span><span id="L671" data-line-number="671"></span><span id="L672" data-line-number="672"></span><span id="L673" data-line-number="673"></span><span id="L674" data-line-number="674"></span><span id="L675" data-line-number="675"></span><span id="L676" data-line-number="676"></span><span id="L677" data-line-number="677"></span><span id="L678" data-line-number="678"></span><span id="L679" data-line-number="679"></span><span id="L680" data-line-number="680"></span><span id="L681" data-line-number="681"></span><span id="L682" data-line-number="682"></span><span id="L683" data-line-number="683"></span><span id="L684" data-line-number="684"></span><span id="L685" data-line-number="685"></span><span id="L686" data-line-number="686"></span><span id="L687" data-line-number="687"></span><span id="L688" data-line-number="688"></span><span id="L689" data-line-number="689"></span><span id="L690" data-line-number="690"></span><span id="L691" data-line-number="691"></span><span id="L692" data-line-number="692"></span><span id="L693" data-line-number="693"></span><span id="L694" data-line-number="694"></span><span id="L695" data-line-number="695"></span><span id="L696" data-line-number="696"></span><span id="L697" data-line-number="697"></span><span id="L698" data-line-number="698"></span><span id="L699" data-line-number="699"></span><span id="L700" data-line-number="700"></span><span id="L701" data-line-number="701"></span><span id="L702" data-line-number="702"></span><span id="L703" data-line-number="703"></span><span id="L704" data-line-number="704"></span><span id="L705" data-line-number="705"></span><span id="L706" data-line-number="706"></span><span id="L707" data-line-number="707"></span><span id="L708" data-line-number="708"></span><span id="L709" data-line-number="709"></span><span id="L710" data-line-number="710"></span><span id="L711" data-line-number="711"></span><span id="L712" data-line-number="712"></span><span id="L713" data-line-number="713"></span><span id="L714" data-line-number="714"></span><span id="L715" data-line-number="715"></span><span id="L716" data-line-number="716"></span><span id="L717" data-line-number="717"></span><span id="L718" data-line-number="718"></span><span id="L719" data-line-number="719"></span><span id="L720" data-line-number="720"></span><span id="L721" data-line-number="721"></span><span id="L722" data-line-number="722"></span><span id="L723" data-line-number="723"></span><span id="L724" data-line-number="724"></span><span id="L725" data-line-number="725"></span><span id="L726" data-line-number="726"></span><span id="L727" data-line-number="727"></span><span id="L728" data-line-number="728"></span><span id="L729" data-line-number="729"></span><span id="L730" data-line-number="730"></span><span id="L731" data-line-number="731"></span><span id="L732" data-line-number="732"></span><span id="L733" data-line-number="733"></span><span id="L734" data-line-number="734"></span><span id="L735" data-line-number="735"></span><span id="L736" data-line-number="736"></span><span id="L737" data-line-number="737"></span><span id="L738" data-line-number="738"></span><span id="L739" data-line-number="739"></span><span id="L740" data-line-number="740"></span><span id="L741" data-line-number="741"></span><span id="L742" data-line-number="742"></span><span id="L743" data-line-number="743"></span><span id="L744" data-line-number="744"></span><span id="L745" data-line-number="745"></span><span id="L746" data-line-number="746"></span><span id="L747" data-line-number="747"></span><span id="L748" data-line-number="748"></span><span id="L749" data-line-number="749"></span><span id="L750" data-line-number="750"></span><span id="L751" data-line-number="751"></span><span id="L752" data-line-number="752"></span><span id="L753" data-line-number="753"></span><span id="L754" data-line-number="754"></span><span id="L755" data-line-number="755"></span><span id="L756" data-line-number="756"></span><span id="L757" data-line-number="757"></span><span id="L758" data-line-number="758"></span><span id="L759" data-line-number="759"></span><span id="L760" data-line-number="760"></span><span id="L761" data-line-number="761"></span><span id="L762" data-line-number="762"></span><span id="L763" data-line-number="763"></span><span id="L764" data-line-number="764"></span><span id="L765" data-line-number="765"></span><span id="L766" data-line-number="766"></span><span id="L767" data-line-number="767"></span><span id="L768" data-line-number="768"></span><span id="L769" data-line-number="769"></span><span id="L770" data-line-number="770"></span><span id="L771" data-line-number="771"></span><span id="L772" data-line-number="772"></span><span id="L773" data-line-number="773"></span><span id="L774" data-line-number="774"></span><span id="L775" data-line-number="775"></span><span id="L776" data-line-number="776"></span><span id="L777" data-line-number="777"></span><span id="L778" data-line-number="778"></span><span id="L779" data-line-number="779"></span><span id="L780" data-line-number="780"></span><span id="L781" data-line-number="781"></span><span id="L782" data-line-number="782"></span><span id="L783" data-line-number="783"></span><span id="L784" data-line-number="784"></span><span id="L785" data-line-number="785"></span><span id="L786" data-line-number="786"></span><span id="L787" data-line-number="787"></span><span id="L788" data-line-number="788"></span><span id="L789" data-line-number="789"></span><span id="L790" data-line-number="790"></span><span id="L791" data-line-number="791"></span><span id="L792" data-line-number="792"></span><span id="L793" data-line-number="793"></span><span id="L794" data-line-number="794"></span><span id="L795" data-line-number="795"></span><span id="L796" data-line-number="796"></span><span id="L797" data-line-number="797"></span><span id="L798" data-line-number="798"></span><span id="L799" data-line-number="799"></span><span id="L800" data-line-number="800"></span><span id="L801" data-line-number="801"></span><span id="L802" data-line-number="802"></span><span id="L803" data-line-number="803"></span><span id="L804" data-line-number="804"></span><span id="L805" data-line-number="805"></span><span id="L806" data-line-number="806"></span><span id="L807" data-line-number="807"></span><span id="L808" data-line-number="808"></span><span id="L809" data-line-number="809"></span><span id="L810" data-line-number="810"></span><span id="L811" data-line-number="811"></span><span id="L812" data-line-number="812"></span><span id="L813" data-line-number="813"></span><span id="L814" data-line-number="814"></span><span id="L815" data-line-number="815"></span><span id="L816" data-line-number="816"></span><span id="L817" data-line-number="817"></span><span id="L818" data-line-number="818"></span><span id="L819" data-line-number="819"></span><span id="L820" data-line-number="820"></span><span id="L821" data-line-number="821"></span><span id="L822" data-line-number="822"></span><span id="L823" data-line-number="823"></span><span id="L824" data-line-number="824"></span><span id="L825" data-line-number="825"></span><span id="L826" data-line-number="826"></span><span id="L827" data-line-number="827"></span><span id="L828" data-line-number="828"></span><span id="L829" data-line-number="829"></span><span id="L830" data-line-number="830"></span><span id="L831" data-line-number="831"></span><span id="L832" data-line-number="832"></span><span id="L833" data-line-number="833"></span><span id="L834" data-line-number="834"></span><span id="L835" data-line-number="835"></span><span id="L836" data-line-number="836"></span><span id="L837" data-line-number="837"></span><span id="L838" data-line-number="838"></span><span id="L839" data-line-number="839"></span><span id="L840" data-line-number="840"></span><span id="L841" data-line-number="841"></span><span id="L842" data-line-number="842"></span><span id="L843" data-line-number="843"></span><span id="L844" data-line-number="844"></span><span id="L845" data-line-number="845"></span><span id="L846" data-line-number="846"></span><span id="L847" data-line-number="847"></span><span id="L848" data-line-number="848"></span><span id="L849" data-line-number="849"></span><span id="L850" data-line-number="850"></span><span id="L851" data-line-number="851"></span><span id="L852" data-line-number="852"></span><span id="L853" data-line-number="853"></span><span id="L854" data-line-number="854"></span><span id="L855" data-line-number="855"></span><span id="L856" data-line-number="856"></span><span id="L857" data-line-number="857"></span><span id="L858" data-line-number="858"></span><span id="L859" data-line-number="859"></span><span id="L860" data-line-number="860"></span><span id="L861" data-line-number="861"></span><span id="L862" data-line-number="862"></span><span id="L863" data-line-number="863"></span><span id="L864" data-line-number="864"></span><span id="L865" data-line-number="865"></span><span id="L866" data-line-number="866"></span><span id="L867" data-line-number="867"></span><span id="L868" data-line-number="868"></span><span id="L869" data-line-number="869"></span><span id="L870" data-line-number="870"></span><span id="L871" data-line-number="871"></span><span id="L872" data-line-number="872"></span><span id="L873" data-line-number="873"></span><span id="L874" data-line-number="874"></span><span id="L875" data-line-number="875"></span><span id="L876" data-line-number="876"></span><span id="L877" data-line-number="877"></span><span id="L878" data-line-number="878"></span><span id="L879" data-line-number="879"></span><span id="L880" data-line-number="880"></span><span id="L881" data-line-number="881"></span><span id="L882" data-line-number="882"></span><span id="L883" data-line-number="883"></span><span id="L884" data-line-number="884"></span><span id="L885" data-line-number="885"></span><span id="L886" data-line-number="886"></span><span id="L887" data-line-number="887"></span><span id="L888" data-line-number="888"></span><span id="L889" data-line-number="889"></span><span id="L890" data-line-number="890"></span><span id="L891" data-line-number="891"></span><span id="L892" data-line-number="892"></span><span id="L893" data-line-number="893"></span><span id="L894" data-line-number="894"></span><span id="L895" data-line-number="895"></span><span id="L896" data-line-number="896"></span><span id="L897" data-line-number="897"></span><span id="L898" data-line-number="898"></span><span id="L899" data-line-number="899"></span><span id="L900" data-line-number="900"></span><span id="L901" data-line-number="901"></span><span id="L902" data-line-number="902"></span><span id="L903" data-line-number="903"></span><span id="L904" data-line-number="904"></span><span id="L905" data-line-number="905"></span><span id="L906" data-line-number="906"></span><span id="L907" data-line-number="907"></span><span id="L908" data-line-number="908"></span><span id="L909" data-line-number="909"></span><span id="L910" data-line-number="910"></span><span id="L911" data-line-number="911"></span><span id="L912" data-line-number="912"></span><span id="L913" data-line-number="913"></span><span id="L914" data-line-number="914"></span><span id="L915" data-line-number="915"></span><span id="L916" data-line-number="916"></span><span id="L917" data-line-number="917"></span><span id="L918" data-line-number="918"></span><span id="L919" data-line-number="919"></span><span id="L920" data-line-number="920"></span><span id="L921" data-line-number="921"></span><span id="L922" data-line-number="922"></span><span id="L923" data-line-number="923"></span><span id="L924" data-line-number="924"></span><span id="L925" data-line-number="925"></span><span id="L926" data-line-number="926"></span><span id="L927" data-line-number="927"></span><span id="L928" data-line-number="928"></span><span id="L929" data-line-number="929"></span><span id="L930" data-line-number="930"></span><span id="L931" data-line-number="931"></span><span id="L932" data-line-number="932"></span><span id="L933" data-line-number="933"></span><span id="L934" data-line-number="934"></span><span id="L935" data-line-number="935"></span><span id="L936" data-line-number="936"></span><span id="L937" data-line-number="937"></span><span id="L938" data-line-number="938"></span><span id="L939" data-line-number="939"></span><span id="L940" data-line-number="940"></span><span id="L941" data-line-number="941"></span><span id="L942" data-line-number="942"></span><span id="L943" data-line-number="943"></span><span id="L944" data-line-number="944"></span><span id="L945" data-line-number="945"></span><span id="L946" data-line-number="946"></span><span id="L947" data-line-number="947"></span><span id="L948" data-line-number="948"></span><span id="L949" data-line-number="949"></span><span id="L950" data-line-number="950"></span><span id="L951" data-line-number="951"></span><span id="L952" data-line-number="952"></span><span id="L953" data-line-number="953"></span><span id="L954" data-line-number="954"></span><span id="L955" data-line-number="955"></span><span id="L956" data-line-number="956"></span><span id="L957" data-line-number="957"></span><span id="L958" data-line-number="958"></span><span id="L959" data-line-number="959"></span><span id="L960" data-line-number="960"></span><span id="L961" data-line-number="961"></span><span id="L962" data-line-number="962"></span><span id="L963" data-line-number="963"></span><span id="L964" data-line-number="964"></span><span id="L965" data-line-number="965"></span><span id="L966" data-line-number="966"></span><span id="L967" data-line-number="967"></span><span id="L968" data-line-number="968"></span><span id="L969" data-line-number="969"></span><span id="L970" data-line-number="970"></span><span id="L971" data-line-number="971"></span><span id="L972" data-line-number="972"></span><span id="L973" data-line-number="973"></span><span id="L974" data-line-number="974"></span><span id="L975" data-line-number="975"></span><span id="L976" data-line-number="976"></span><span id="L977" data-line-number="977"></span><span id="L978" data-line-number="978"></span><span id="L979" data-line-number="979"></span><span id="L980" data-line-number="980"></span><span id="L981" data-line-number="981"></span><span id="L982" data-line-number="982"></span><span id="L983" data-line-number="983"></span><span id="L984" data-line-number="984"></span><span id="L985" data-line-number="985"></span><span id="L986" data-line-number="986"></span><span id="L987" data-line-number="987"></span><span id="L988" data-line-number="988"></span><span id="L989" data-line-number="989"></span><span id="L990" data-line-number="990"></span><span id="L991" data-line-number="991"></span><span id="L992" data-line-number="992"></span><span id="L993" data-line-number="993"></span><span id="L994" data-line-number="994"></span><span id="L995" data-line-number="995"></span><span id="L996" data-line-number="996"></span><span id="L997" data-line-number="997"></span><span id="L998" data-line-number="998"></span><span id="L999" data-line-number="999"></span><span id="L1000" data-line-number="1000"></span><span id="L1001" data-line-number="1001"></span><span id="L1002" data-line-number="1002"></span><span id="L1003" data-line-number="1003"></span><span id="L1004" data-line-number="1004"></span><span id="L1005" data-line-number="1005"></span><span id="L1006" data-line-number="1006"></span><span id="L1007" data-line-number="1007"></span><span id="L1008" data-line-number="1008"></span><span id="L1009" data-line-number="1009"></span><span id="L1010" data-line-number="1010"></span><span id="L1011" data-line-number="1011"></span><span id="L1012" data-line-number="1012"></span><span id="L1013" data-line-number="1013"></span><span id="L1014" data-line-number="1014"></span><span id="L1015" data-line-number="1015"></span><span id="L1016" data-line-number="1016"></span><span id="L1017" data-line-number="1017"></span><span id="L1018" data-line-number="1018"></span><span id="L1019" data-line-number="1019"></span><span id="L1020" data-line-number="1020"></span><span id="L1021" data-line-number="1021"></span><span id="L1022" data-line-number="1022"></span><span id="L1023" data-line-number="1023"></span><span id="L1024" data-line-number="1024"></span><span id="L1025" data-line-number="1025"></span><span id="L1026" data-line-number="1026"></span><span id="L1027" data-line-number="1027"></span><span id="L1028" data-line-number="1028"></span><span id="L1029" data-line-number="1029"></span><span id="L1030" data-line-number="1030"></span><span id="L1031" data-line-number="1031"></span><span id="L1032" data-line-number="1032"></span><span id="L1033" data-line-number="1033"></span><span id="L1034" data-line-number="1034"></span><span id="L1035" data-line-number="1035"></span><span id="L1036" data-line-number="1036"></span><span id="L1037" data-line-number="1037"></span><span id="L1038" data-line-number="1038"></span><span id="L1039" data-line-number="1039"></span><span id="L1040" data-line-number="1040"></span><span id="L1041" data-line-number="1041"></span><span id="L1042" data-line-number="1042"></span><span id="L1043" data-line-number="1043"></span><span id="L1044" data-line-number="1044"></span></td>
# 							<td class="lines-code"><pre><code class="python"><ol class="linenums"><li class="L1" rel="L1">#coding=utf-8
# </li><li class="L2" rel="L2">&#34;&#34;&#34;
# </li><li class="L3" rel="L3">A TestRunner for use with the Python unit testing framework. It
# </li><li class="L4" rel="L4">generates a HTML report to show the result at a glance.
# </li><li class="L5" rel="L5">
# </li><li class="L6" rel="L6">The simplest way to use this is to invoke its main method. E.g.
# </li><li class="L7" rel="L7">
# </li><li class="L8" rel="L8">    import unittest
# </li><li class="L9" rel="L9">    import HTMLTestReportCN
# </li><li class="L10" rel="L10">
# </li><li class="L11" rel="L11">    ... define your tests ...
# </li><li class="L12" rel="L12">
# </li><li class="L13" rel="L13">    if __name__ == &#39;__main__&#39;:
# </li><li class="L14" rel="L14">        HTMLTestReportCN.main()
# </li><li class="L15" rel="L15">
# </li><li class="L16" rel="L16">
# </li><li class="L17" rel="L17">For more customization options, instantiates a HTMLTestReportCN object.
# </li><li class="L18" rel="L18">HTMLTestReportCN is a counterpart to unittest&#39;s TextTestRunner. E.g.
# </li><li class="L19" rel="L19">
# </li><li class="L20" rel="L20">    # output to a file
# </li><li class="L21" rel="L21">    fp = file(&#39;my_report.html&#39;, &#39;wb&#39;)
# </li><li class="L22" rel="L22">    runner = HTMLTestReportCN.HTMLTestReportCN(
# </li><li class="L23" rel="L23">                stream=fp,
# </li><li class="L24" rel="L24">                title=&#39;My unit test&#39;,
# </li><li class="L25" rel="L25">                description=&#39;This demonstrates the report output by HTMLTestReportCN.&#39;
# </li><li class="L26" rel="L26">                )
# </li><li class="L27" rel="L27">
# </li><li class="L28" rel="L28">    # Use an external stylesheet.
# </li><li class="L29" rel="L29">    # See the Template_mixin class for more customizable options
# </li><li class="L30" rel="L30">    runner.STYLESHEET_TMPL = &#39;&lt;link rel=&#34;stylesheet&#34; href=&#34;my_stylesheet.css&#34; type=&#34;text/css&#34;&gt;&#39;
# </li><li class="L31" rel="L31">
# </li><li class="L32" rel="L32">    # run the test
# </li><li class="L33" rel="L33">    runner.run(my_test_suite)
# </li><li class="L34" rel="L34">
# </li><li class="L35" rel="L35">
# </li><li class="L36" rel="L36">------------------------------------------------------------------------
# </li><li class="L37" rel="L37">Copyright (c) 2004-2007, Wai Yip Tung
# </li><li class="L38" rel="L38">Copyright (c) 2017, Findyou
# </li><li class="L39" rel="L39">All rights reserved.
# </li><li class="L40" rel="L40">
# </li><li class="L41" rel="L41">Redistribution and use in source and binary forms, with or without
# </li><li class="L42" rel="L42">modification, are permitted provided that the following conditions are
# </li><li class="L43" rel="L43">met:
# </li><li class="L44" rel="L44">
# </li><li class="L45" rel="L45">* Redistributions of source code must retain the above copyright notice,
# </li><li class="L46" rel="L46">  this list of conditions and the following disclaimer.
# </li><li class="L47" rel="L47">* Redistributions in binary form must reproduce the above copyright
# </li><li class="L48" rel="L48">  notice, this list of conditions and the following disclaimer in the
# </li><li class="L49" rel="L49">  documentation and/or other materials provided with the distribution.
# </li><li class="L50" rel="L50">* Neither the name Wai Yip Tung nor the names of its contributors may be
# </li><li class="L51" rel="L51">  used to endorse or promote products derived from this software without
# </li><li class="L52" rel="L52">  specific prior written permission.
# </li><li class="L53" rel="L53">
# </li><li class="L54" rel="L54">THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS &#34;AS
# </li><li class="L55" rel="L55">IS&#34; AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
# </li><li class="L56" rel="L56">TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# </li><li class="L57" rel="L57">PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
# </li><li class="L58" rel="L58">OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# </li><li class="L59" rel="L59">EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# </li><li class="L60" rel="L60">PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# </li><li class="L61" rel="L61">PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# </li><li class="L62" rel="L62">LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# </li><li class="L63" rel="L63">NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# </li><li class="L64" rel="L64">SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# </li><li class="L65" rel="L65">&#34;&#34;&#34;
# </li><li class="L66" rel="L66">
# </li><li class="L67" rel="L67"># URL: http://tungwaiyip.info/software/HTMLTestRunner.html
# </li><li class="L68" rel="L68">
# </li><li class="L69" rel="L69">__author__ = &#34;Wai Yip Tung,  Findyou&#34;
# </li><li class="L70" rel="L70">__version__ = &#34;0.8.3&#34;
# </li><li class="L71" rel="L71">
# </li><li class="L72" rel="L72">
# </li><li class="L73" rel="L73">&#34;&#34;&#34;
# </li><li class="L74" rel="L74">Change History
# </li><li class="L75" rel="L75">Version 0.8.3 -Findyou 20171206
# </li><li class="L76" rel="L76">* BUG fixed :错误的测试用例没有统计与显示
# </li><li class="L77" rel="L77">* BUG fixed :当PASS的测试用例有print内容时，通过按钮显示为红色
# </li><li class="L78" rel="L78">* 表格背景颜色根据用例结果显示颜色，优先级： 错误(黄色)&gt;失败(红色)&gt;通过(绿色)
# </li><li class="L79" rel="L79">* 合并文为HTMLTestRunner*N.py 同时支持python2,python3
# </li><li class="L80" rel="L80">
# </li><li class="L81" rel="L81">Version 0.8.2.2 -Findyou
# </li><li class="L82" rel="L82">* HTMLTestRunnerEN.py 支持 python3.x
# </li><li class="L83" rel="L83">* HTMLTestRunnerEN.py 支持 python2.x
# </li><li class="L84" rel="L84">
# </li><li class="L85" rel="L85">Version 0.8.2.1 -Findyou
# </li><li class="L86" rel="L86">* 支持中文，汉化
# </li><li class="L87" rel="L87">* 调整样式，美化（需要连入网络，使用的百度的Bootstrap.js）
# </li><li class="L88" rel="L88">* 增加 通过分类显示、测试人员、通过率的展示
# </li><li class="L89" rel="L89">* 优化“详细”与“收起”状态的变换
# </li><li class="L90" rel="L90">* 增加返回顶部的锚点
# </li><li class="L91" rel="L91">
# </li><li class="L92" rel="L92">Version 0.8.2
# </li><li class="L93" rel="L93">* Show output inline instead of popup window (Viorel Lupu).
# </li><li class="L94" rel="L94">
# </li><li class="L95" rel="L95">Version in 0.8.1
# </li><li class="L96" rel="L96">* Validated XHTML (Wolfgang Borgert).
# </li><li class="L97" rel="L97">* Added description of test classes and test cases.
# </li><li class="L98" rel="L98">
# </li><li class="L99" rel="L99">Version in 0.8.0
# </li><li class="L100" rel="L100">* Define Template_mixin class for customization.
# </li><li class="L101" rel="L101">* Workaround a IE 6 bug that it does not treat &lt;script&gt; block as CDATA.
# </li><li class="L102" rel="L102">
# </li><li class="L103" rel="L103">Version in 0.7.1
# </li><li class="L104" rel="L104">* Back port to Python 2.3 (Frank Horowitz).
# </li><li class="L105" rel="L105">* Fix missing scroll bars in detail log (Podi).
# </li><li class="L106" rel="L106">&#34;&#34;&#34;
# </li><li class="L107" rel="L107">
# </li><li class="L108" rel="L108"># TODO: color stderr
# </li><li class="L109" rel="L109"># TODO: simplify javascript using ,ore than 1 class in the class attribute?
# </li><li class="L110" rel="L110">
# </li><li class="L111" rel="L111">import datetime
# </li><li class="L112" rel="L112">try:
# </li><li class="L113" rel="L113">    from StringIO import StringIO
# </li><li class="L114" rel="L114">except ImportError:
# </li><li class="L115" rel="L115">    from io import StringIO
# </li><li class="L116" rel="L116">import sys
# </li><li class="L117" rel="L117">import time
# </li><li class="L118" rel="L118">import unittest
# </li><li class="L119" rel="L119">from xml.sax import saxutils
# </li><li class="L120" rel="L120">import logging
# </li><li class="L121" rel="L121">import io
# </li><li class="L122" rel="L122">import re
# </li><li class="L123" rel="L123">try:
# </li><li class="L124" rel="L124">    reload(sys)
# </li><li class="L125" rel="L125">    sys.setdefaultencoding(&#39;utf-8&#39;)
# </li><li class="L126" rel="L126">except NameError:
# </li><li class="L127" rel="L127">    pass
# </li><li class="L128" rel="L128">
# </li><li class="L129" rel="L129"># ------------------------------------------------------------------------
# </li><li class="L130" rel="L130"># The redirectors below are used to capture output during testing. Output
# </li><li class="L131" rel="L131"># sent to sys.stdout and sys.stderr are automatically captured. However
# </li><li class="L132" rel="L132"># in some cases sys.stdout is already cached before HTMLTestRunner is
# </li><li class="L133" rel="L133"># invoked (e.g. calling logging.basicConfig). In order to capture those
# </li><li class="L134" rel="L134"># output, use the redirectors for the cached stream.
# </li><li class="L135" rel="L135">#
# </li><li class="L136" rel="L136"># e.g.
# </li><li class="L137" rel="L137">#   &gt;&gt;&gt; logging.basicConfig(stream=HTMLTestRunner.stdout_redirector)
# </li><li class="L138" rel="L138">#   &gt;&gt;&gt;
# </li><li class="L139" rel="L139">
# </li><li class="L140" rel="L140">class OutputRedirector(object):
# </li><li class="L141" rel="L141">    &#34;&#34;&#34; Wrapper to redirect stdout or stderr &#34;&#34;&#34;
# </li><li class="L142" rel="L142">    def __init__(self, fp):
# </li><li class="L143" rel="L143">        self.fp = fp
# </li><li class="L144" rel="L144">
# </li><li class="L145" rel="L145">    def write(self, s):
# </li><li class="L146" rel="L146">        self.fp.write(s)
# </li><li class="L147" rel="L147">
# </li><li class="L148" rel="L148">    def writelines(self, lines):
# </li><li class="L149" rel="L149">        self.fp.writelines(lines)
# </li><li class="L150" rel="L150">
# </li><li class="L151" rel="L151">    def flush(self):
# </li><li class="L152" rel="L152">        self.fp.flush()
# </li><li class="L153" rel="L153">
# </li><li class="L154" rel="L154">stdout_redirector = OutputRedirector(sys.stdout)
# </li><li class="L155" rel="L155">stderr_redirector = OutputRedirector(sys.stderr)
# </li><li class="L156" rel="L156">
# </li><li class="L157" rel="L157"># ----------------------------------------------------------------------
# </li><li class="L158" rel="L158"># Template
# </li><li class="L159" rel="L159">
# </li><li class="L160" rel="L160">class Template_mixin(object):
# </li><li class="L161" rel="L161">    &#34;&#34;&#34;
# </li><li class="L162" rel="L162">    Define a HTML template for report customerization and generation.
# </li><li class="L163" rel="L163">
# </li><li class="L164" rel="L164">    Overall structure of an HTML report
# </li><li class="L165" rel="L165">
# </li><li class="L166" rel="L166">    HTML
# </li><li class="L167" rel="L167">    +------------------------+
# </li><li class="L168" rel="L168">    |&lt;html&gt;                  |
# </li><li class="L169" rel="L169">    |  &lt;head&gt;                |
# </li><li class="L170" rel="L170">    |                        |
# </li><li class="L171" rel="L171">    |   STYLESHEET           |
# </li><li class="L172" rel="L172">    |   +----------------+   |
# </li><li class="L173" rel="L173">    |   |                |   |
# </li><li class="L174" rel="L174">    |   +----------------+   |
# </li><li class="L175" rel="L175">    |                        |
# </li><li class="L176" rel="L176">    |  &lt;/head&gt;               |
# </li><li class="L177" rel="L177">    |                        |
# </li><li class="L178" rel="L178">    |  &lt;body&gt;                |
# </li><li class="L179" rel="L179">    |                        |
# </li><li class="L180" rel="L180">    |   HEADING              |
# </li><li class="L181" rel="L181">    |   +----------------+   |
# </li><li class="L182" rel="L182">    |   |                |   |
# </li><li class="L183" rel="L183">    |   +----------------+   |
# </li><li class="L184" rel="L184">    |                        |
# </li><li class="L185" rel="L185">    |   REPORT               |
# </li><li class="L186" rel="L186">    |   +----------------+   |
# </li><li class="L187" rel="L187">    |   |                |   |
# </li><li class="L188" rel="L188">    |   +----------------+   |
# </li><li class="L189" rel="L189">    |                        |
# </li><li class="L190" rel="L190">    |   ENDING               |
# </li><li class="L191" rel="L191">    |   +----------------+   |
# </li><li class="L192" rel="L192">    |   |                |   |
# </li><li class="L193" rel="L193">    |   +----------------+   |
# </li><li class="L194" rel="L194">    |                        |
# </li><li class="L195" rel="L195">    |  &lt;/body&gt;               |
# </li><li class="L196" rel="L196">    |&lt;/html&gt;                 |
# </li><li class="L197" rel="L197">    +------------------------+
# </li><li class="L198" rel="L198">    &#34;&#34;&#34;
# </li><li class="L199" rel="L199">
# </li><li class="L200" rel="L200">    STATUS = {
# </li><li class="L201" rel="L201">    0: &#39;通过&#39;,
# </li><li class="L202" rel="L202">    1: &#39;失败&#39;,
# </li><li class="L203" rel="L203">    2: &#39;错误&#39;,
# </li><li class="L204" rel="L204">    }
# </li><li class="L205" rel="L205">
# </li><li class="L206" rel="L206">    DEFAULT_TITLE = &#39;测试报告&#39;
# </li><li class="L207" rel="L207">    DEFAULT_DESCRIPTION = &#39;&#39;
# </li><li class="L208" rel="L208">    DEFAULT_TESTER=&#39;QA&#39;
# </li><li class="L209" rel="L209">
# </li><li class="L210" rel="L210">    # ------------------------------------------------------------------------
# </li><li class="L211" rel="L211">    # HTML Template
# </li><li class="L212" rel="L212">
# </li><li class="L213" rel="L213">    HTML_TMPL = r&#34;&#34;&#34;&lt;?xml version=&#34;1.0&#34; encoding=&#34;UTF-8&#34;?&gt;
# </li><li class="L214" rel="L214">&lt;!DOCTYPE html PUBLIC &#34;-//W3C//DTD XHTML 1.0 Strict//EN&#34; &#34;http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd&#34;&gt;
# </li><li class="L215" rel="L215">&lt;html xmlns=&#34;http://www.w3.org/1999/xhtml&#34;&gt;
# </li><li class="L216" rel="L216">&lt;head&gt;
# </li><li class="L217" rel="L217">    &lt;title&gt;%(title)s&lt;/title&gt;
# </li><li class="L218" rel="L218">    &lt;meta name=&#34;generator&#34; content=&#34;%(generator)s&#34;/&gt;
# </li><li class="L219" rel="L219">    &lt;meta http-equiv=&#34;Content-Type&#34; content=&#34;text/html; charset=UTF-8&#34;/&gt;
# </li><li class="L220" rel="L220">    &lt;link href=&#34;http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css&#34; rel=&#34;stylesheet&#34;&gt;
# </li><li class="L221" rel="L221">    &lt;script src=&#34;http://libs.baidu.com/jquery/2.0.0/jquery.min.js&#34;&gt;&lt;/script&gt;
# </li><li class="L222" rel="L222">    &lt;script src=&#34;http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js&#34;&gt;&lt;/script&gt;
# </li><li class="L223" rel="L223">    &lt;script type=&#34;text/javascript&#34; src=&#34;https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js&#34;&gt;&lt;/script&gt;
# </li><li class="L224" rel="L224">    %(stylesheet)s
# </li><li class="L225" rel="L225">&lt;/head&gt;
# </li><li class="L226" rel="L226">&lt;body &gt;
# </li><li class="L227" rel="L227">%(heading)s
# </li><li class="L228" rel="L228">%(report)s
# </li><li class="L229" rel="L229">%(ending)s
# </li><li class="L230" rel="L230">&lt;script language=&#34;javascript&#34; type=&#34;text/javascript&#34;&gt;
# </li><li class="L231" rel="L231">output_list = Array();
# </li><li class="L232" rel="L232">// 修改按钮颜色显示错误问题 --Findyou v0.8.2.3
# </li><li class="L233" rel="L233">
# </li><li class="L234" rel="L234">$(&#34;button[id^=&#39;btn_pt&#39;]&#34;).addClass(&#34;btn btn-success&#34;);
# </li><li class="L235" rel="L235">$(&#34;button[id^=&#39;btn_ft&#39;]&#34;).addClass(&#34;btn btn-danger&#34;);
# </li><li class="L236" rel="L236">$(&#34;button[id^=&#39;btn_et&#39;]&#34;).addClass(&#34;btn btn-warning&#34;);
# </li><li class="L237" rel="L237">
# </li><li class="L238" rel="L238">/*level
# </li><li class="L239" rel="L239">增加分类并调整，增加error按钮事件 --Findyou v0.8.2.3
# </li><li class="L240" rel="L240">0:Pass    //pt none, ft hiddenRow, et hiddenRow
# </li><li class="L241" rel="L241">1:Failed  //pt hiddenRow, ft none, et hiddenRow
# </li><li class="L242" rel="L242">2:Error    //pt hiddenRow, ft hiddenRow, et none
# </li><li class="L243" rel="L243">3:All     //pt none, ft none, et none
# </li><li class="L244" rel="L244">4:Summary //all hiddenRow
# </li><li class="L245" rel="L245">*/
# </li><li class="L246" rel="L246">
# </li><li class="L247" rel="L247">//add Error button event --Findyou v0.8.2.3
# </li><li class="L248" rel="L248">function showCase(level) {
# </li><li class="L249" rel="L249">    trs = document.getElementsByTagName(&#34;tr&#34;);
# </li><li class="L250" rel="L250">    for (var i = 0; i &lt; trs.length; i++) {
# </li><li class="L251" rel="L251">        tr = trs[i];
# </li><li class="L252" rel="L252">        id = tr.id;
# </li><li class="L253" rel="L253">        if (id.substr(0,2) == &#39;ft&#39;) {
# </li><li class="L254" rel="L254">            if (level == 0 || level == 2 || level == 4 ) {
# </li><li class="L255" rel="L255">                tr.className = &#39;hiddenRow&#39;;
# </li><li class="L256" rel="L256">            }
# </li><li class="L257" rel="L257">            else {
# </li><li class="L258" rel="L258">                tr.className = &#39;&#39;;
# </li><li class="L259" rel="L259">            }
# </li><li class="L260" rel="L260">        }
# </li><li class="L261" rel="L261">        if (id.substr(0,2) == &#39;pt&#39;) {
# </li><li class="L262" rel="L262">            if (level == 1 || level == 2 || level == 4) {
# </li><li class="L263" rel="L263">                tr.className = &#39;hiddenRow&#39;;
# </li><li class="L264" rel="L264">            }
# </li><li class="L265" rel="L265">            else {
# </li><li class="L266" rel="L266">                tr.className = &#39;&#39;;
# </li><li class="L267" rel="L267">            }
# </li><li class="L268" rel="L268">        }
# </li><li class="L269" rel="L269">        if (id.substr(0,2) == &#39;et&#39;) {
# </li><li class="L270" rel="L270">            if (level == 0 || level == 1 || level == 4) {
# </li><li class="L271" rel="L271">                tr.className = &#39;hiddenRow&#39;;
# </li><li class="L272" rel="L272">            }
# </li><li class="L273" rel="L273">            else {
# </li><li class="L274" rel="L274">                tr.className = &#39;&#39;;
# </li><li class="L275" rel="L275">            }
# </li><li class="L276" rel="L276">        }
# </li><li class="L277" rel="L277">    }
# </li><li class="L278" rel="L278">
# </li><li class="L279" rel="L279">    //加入【详细】切换文字变化 --Findyou
# </li><li class="L280" rel="L280">    detail_class=document.getElementsByClassName(&#39;detail&#39;);
# </li><li class="L281" rel="L281">	//console.log(detail_class.length)
# </li><li class="L282" rel="L282">	if (level == 3) {
# </li><li class="L283" rel="L283">		for (var i = 0; i &lt; detail_class.length; i++){
# </li><li class="L284" rel="L284">			detail_class[i].innerHTML=&#34;收起&#34;
# </li><li class="L285" rel="L285">		}
# </li><li class="L286" rel="L286">	}
# </li><li class="L287" rel="L287">	else{
# </li><li class="L288" rel="L288">			for (var i = 0; i &lt; detail_class.length; i++){
# </li><li class="L289" rel="L289">			detail_class[i].innerHTML=&#34;详细&#34;
# </li><li class="L290" rel="L290">		}
# </li><li class="L291" rel="L291">	}
# </li><li class="L292" rel="L292">}
# </li><li class="L293" rel="L293">
# </li><li class="L294" rel="L294">//add Error button event --Findyou v0.8.2.3
# </li><li class="L295" rel="L295">function showClassDetail(cid, count) {
# </li><li class="L296" rel="L296">    var id_list = Array(count);
# </li><li class="L297" rel="L297">    var toHide = 1;
# </li><li class="L298" rel="L298">    for (var i = 0; i &lt; count; i++) {
# </li><li class="L299" rel="L299">        tid0 = &#39;t&#39; + cid.substr(1) + &#39;_&#39; + (i+1);
# </li><li class="L300" rel="L300">        tid = &#39;f&#39; + tid0;
# </li><li class="L301" rel="L301">        tr = document.getElementById(tid);
# </li><li class="L302" rel="L302">        if (!tr) {
# </li><li class="L303" rel="L303">            tid = &#39;p&#39; + tid0;
# </li><li class="L304" rel="L304">            tr = document.getElementById(tid);
# </li><li class="L305" rel="L305">        }
# </li><li class="L306" rel="L306">        if (!tr) {
# </li><li class="L307" rel="L307">            tid = &#39;e&#39; + tid0;
# </li><li class="L308" rel="L308">            tr = document.getElementById(tid);
# </li><li class="L309" rel="L309">        }
# </li><li class="L310" rel="L310">        id_list[i] = tid;
# </li><li class="L311" rel="L311">        if (tr.className) {
# </li><li class="L312" rel="L312">            toHide = 0;
# </li><li class="L313" rel="L313">        }
# </li><li class="L314" rel="L314">    }
# </li><li class="L315" rel="L315">    for (var i = 0; i &lt; count; i++) {
# </li><li class="L316" rel="L316">        tid = id_list[i];
# </li><li class="L317" rel="L317">        //修改点击无法收起的BUG，加入【详细】切换文字变化 --Findyou
# </li><li class="L318" rel="L318">        if (toHide) {
# </li><li class="L319" rel="L319">            document.getElementById(tid).className = &#39;hiddenRow&#39;;
# </li><li class="L320" rel="L320">            document.getElementById(cid).innerText = &#34;详细&#34;
# </li><li class="L321" rel="L321">        }
# </li><li class="L322" rel="L322">        else {
# </li><li class="L323" rel="L323">            document.getElementById(tid).className = &#39;&#39;;
# </li><li class="L324" rel="L324">            document.getElementById(cid).innerText = &#34;收起&#34;
# </li><li class="L325" rel="L325">        }
# </li><li class="L326" rel="L326">    }
# </li><li class="L327" rel="L327">}
# </li><li class="L328" rel="L328">
# </li><li class="L329" rel="L329">function html_escape(s) {
# </li><li class="L330" rel="L330">    s = s.replace(/&amp;/g,&#39;&amp;amp;&#39;);
# </li><li class="L331" rel="L331">    s = s.replace(/&lt;/g,&#39;&amp;lt;&#39;);
# </li><li class="L332" rel="L332">    s = s.replace(/&gt;/g,&#39;&amp;gt;&#39;);
# </li><li class="L333" rel="L333">    return s;
# </li><li class="L334" rel="L334">}
# </li><li class="L335" rel="L335">//add line
# </li><li class="L336" rel="L336">var dom = document.getElementById(&#34;main&#34;);
# </li><li class="L337" rel="L337">var myChart = echarts.init(dom);
# </li><li class="L338" rel="L338">var app = {};
# </li><li class="L339" rel="L339">option = null;
# </li><li class="L340" rel="L340">option = {
# </li><li class="L341" rel="L341">tooltip: {},
# </li><li class="L342" rel="L342">    xAxis: {
# </li><li class="L343" rel="L343">        type: &#39;category&#39;,
# </li><li class="L344" rel="L344">		&#34;axisTick&#34;:{       //y轴刻度线
# </li><li class="L345" rel="L345">          &#34;show&#34;:false
# </li><li class="L346" rel="L346">        },
# </li><li class="L347" rel="L347">		        &#34;axisLine&#34;:{       //y轴
# </li><li class="L348" rel="L348">          &#34;show&#34;:false
# </li><li class="L349" rel="L349">
# </li><li class="L350" rel="L350">        },axisLabel:{interval:0, formatter: function (name) {return &#39;&#39;;}},//取消x轴名称
# </li><li class="L351" rel="L351">        data: %(line_name)s
# </li><li class="L352" rel="L352">    },
# </li><li class="L353" rel="L353">    yAxis: {
# </li><li class="L354" rel="L354">        type: &#39;value&#39;
# </li><li class="L355" rel="L355">    },
# </li><li class="L356" rel="L356">    series: [{
# </li><li class="L357" rel="L357">		name:&#39;响应时间 单位：ms&#39;,
# </li><li class="L358" rel="L358">        data: %(line_time)s,
# </li><li class="L359" rel="L359">        type: &#39;line&#39;,
# </li><li class="L360" rel="L360">
# </li><li class="L361" rel="L361">	itemStyle: {
# </li><li class="L362" rel="L362">		normal: {
# </li><li class="L363" rel="L363">			color: &#39;#d9534f&#39;,
# </li><li class="L364" rel="L364">			lineStyle: {
# </li><li class="L365" rel="L365">				color: &#39;#d9534f&#39;
# </li><li class="L366" rel="L366">			}
# </li><li class="L367" rel="L367">		}
# </li><li class="L368" rel="L368">	}
# </li><li class="L369" rel="L369">    }]
# </li><li class="L370" rel="L370">};
# </li><li class="L371" rel="L371">;
# </li><li class="L372" rel="L372">if (option &amp;&amp; typeof option === &#34;object&#34;) {
# </li><li class="L373" rel="L373">    myChart.setOption(option, true);
# </li><li class="L374" rel="L374">}
# </li><li class="L375" rel="L375">&lt;/script&gt;
# </li><li class="L376" rel="L376">&lt;/body&gt;
# </li><li class="L377" rel="L377">&lt;/html&gt;
# </li><li class="L378" rel="L378">&#34;&#34;&#34;
# </li><li class="L379" rel="L379">    # variables: (title, generator, stylesheet, heading, report, ending)
# </li><li class="L380" rel="L380">
# </li><li class="L381" rel="L381">
# </li><li class="L382" rel="L382">    # ------------------------------------------------------------------------
# </li><li class="L383" rel="L383">    # Stylesheet
# </li><li class="L384" rel="L384">    #
# </li><li class="L385" rel="L385">    # alternatively use a &lt;link&gt; for external style sheet, e.g.
# </li><li class="L386" rel="L386">    #   &lt;link rel=&#34;stylesheet&#34; href=&#34;$url&#34; type=&#34;text/css&#34;&gt;
# </li><li class="L387" rel="L387">
# </li><li class="L388" rel="L388">    STYLESHEET_TMPL = &#34;&#34;&#34;
# </li><li class="L389" rel="L389">&lt;style type=&#34;text/css&#34; media=&#34;screen&#34;&gt;
# </li><li class="L390" rel="L390">body        { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px; font-size: 100%; }
# </li><li class="L391" rel="L391">table       { font-size: 100%; }
# </li><li class="L392" rel="L392">.head_line div {float:left}
# </li><li class="L393" rel="L393">.line {width:1400px;height:249px}
# </li><li class="L394" rel="L394">.res {float:left;width:510px;height:550px;margin:2px;overflow:auto;}/*增加2列信息 wulinhao*/
# </li><li class="L395" rel="L395">/* -- heading ---------------------------------------------------------------------- */
# </li><li class="L396" rel="L396">.heading {
# </li><li class="L397" rel="L397">    margin-top: 0ex;
# </li><li class="L398" rel="L398">    margin-bottom: 1ex;
# </li><li class="L399" rel="L399">}
# </li><li class="L400" rel="L400">
# </li><li class="L401" rel="L401">.heading .description {
# </li><li class="L402" rel="L402">    margin-top: 4ex;
# </li><li class="L403" rel="L403">    margin-bottom: 6ex;
# </li><li class="L404" rel="L404">}
# </li><li class="L405" rel="L405">
# </li><li class="L406" rel="L406">/* -- report ------------------------------------------------------------------------ */
# </li><li class="L407" rel="L407">#total_row  { font-weight: bold; }
# </li><li class="L408" rel="L408">.passCase   { color: #5cb85c; }
# </li><li class="L409" rel="L409">.failCase   { color: #d9534f; font-weight: bold; }
# </li><li class="L410" rel="L410">.errorCase  { color: #f0ad4e; font-weight: bold; }
# </li><li class="L411" rel="L411">.hiddenRow  { display: none; }
# </li><li class="L412" rel="L412">.testcase   { margin-left: 2em; }
# </li><li class="L413" rel="L413">&lt;/style&gt;
# </li><li class="L414" rel="L414">&#34;&#34;&#34;
# </li><li class="L415" rel="L415">
# </li><li class="L416" rel="L416">    # ------------------------------------------------------------------------
# </li><li class="L417" rel="L417">    # Heading
# </li><li class="L418" rel="L418">    #
# </li><li class="L419" rel="L419">
# </li><li class="L420" rel="L420">    HEADING_TMPL = &#34;&#34;&#34;&lt;div class=&#39;head_line&#39;&gt;&lt;div class=&#39;heading&#39;&gt;
# </li><li class="L421" rel="L421">&lt;h3 style=&#34;font-family: Microsoft YaHei&#34;&gt;%(title)s&lt;/h3&gt;
# </li><li class="L422" rel="L422">%(parameters)s
# </li><li class="L423" rel="L423">&lt;p class=&#39;description&#39;&gt;%(description)s&lt;/p&gt;
# </li><li class="L424" rel="L424">
# </li><li class="L425" rel="L425">
# </li><li class="L426" rel="L426">&#34;&#34;&#34; # variables: (title, parameters, description)
# </li><li class="L427" rel="L427">
# </li><li class="L428" rel="L428">    HEADING_ATTRIBUTE_TMPL = &#34;&#34;&#34;&lt;p class=&#39;attribute&#39;&gt;&lt;strong&gt;%(name)s : &lt;/strong&gt; %(value)s&lt;/p&gt;
# </li><li class="L429" rel="L429">&#34;&#34;&#34; # variables: (name, value)
# </li><li class="L430" rel="L430">
# </li><li class="L431" rel="L431">
# </li><li class="L432" rel="L432">
# </li><li class="L433" rel="L433">    # ------------------------------------------------------------------------
# </li><li class="L434" rel="L434">    # Report
# </li><li class="L435" rel="L435">    #
# </li><li class="L436" rel="L436">    # 汉化,加美化效果 --Findyou
# </li><li class="L437" rel="L437">    REPORT_TMPL = &#34;&#34;&#34;
# </li><li class="L438" rel="L438">&lt;p id=&#39;show_detail_line&#39;&gt;
# </li><li class="L439" rel="L439">&lt;a class=&#34;btn btn-primary&#34; href=&#39;javascript:showCase(4)&#39;&gt;通过率 %(passrate)s &lt;/a&gt;
# </li><li class="L440" rel="L440">&lt;a class=&#34;btn btn-success&#34; href=&#39;javascript:showCase(0)&#39;&gt;通过 %(Pass)s &lt;/a&gt;
# </li><li class="L441" rel="L441">&lt;a class=&#34;btn btn-danger&#34; href=&#39;javascript:showCase(1)&#39;&gt;失败 %(fail)s &lt;/a&gt;
# </li><li class="L442" rel="L442">&lt;a class=&#34;btn btn-warning&#34; href=&#39;javascript:showCase(2)&#39;&gt;错误 %(error)s &lt;/a&gt;
# </li><li class="L443" rel="L443">&lt;a class=&#34;btn btn-info&#34; href=&#39;javascript:showCase(3)&#39;&gt;所有 %(count)s &lt;/a&gt;
# </li><li class="L444" rel="L444">&lt;/p&gt;&lt;/div&gt;
# </li><li class="L445" rel="L445">&lt;div class=&#39;line&#39; id=&#39;main&#39;&gt;p&lt;/div&gt;
# </li><li class="L446" rel="L446">&lt;/div&gt;
# </li><li class="L447" rel="L447">&lt;table id=&#39;result_table&#39; class=&#34;table table-condensed table-bordered table-hover&#34;&gt;
# </li><li class="L448" rel="L448">&lt;colgroup&gt;
# </li><li class="L449" rel="L449">&lt;col align=&#39;left&#39; /&gt;
# </li><li class="L450" rel="L450">&lt;col align=&#39;right&#39; /&gt;
# </li><li class="L451" rel="L451">&lt;col align=&#39;right&#39; /&gt;
# </li><li class="L452" rel="L452">&lt;col align=&#39;right&#39; /&gt;
# </li><li class="L453" rel="L453">&lt;col align=&#39;right&#39; /&gt;
# </li><li class="L454" rel="L454">&lt;col align=&#39;right&#39; /&gt;
# </li><li class="L455" rel="L455">&lt;/colgroup&gt;
# </li><li class="L456" rel="L456">&lt;tr id=&#39;header_row&#39; class=&#34;text-center active&#34; style=&#34;font-weight: bold;font-size: 14px;&#34;&gt;
# </li><li class="L457" rel="L457">    &lt;td&gt;用例集/测试用例&lt;/td&gt;
# </li><li class="L458" rel="L458">    &lt;td&gt;总计&lt;/td&gt;
# </li><li class="L459" rel="L459">    &lt;td&gt;通过&lt;/td&gt;
# </li><li class="L460" rel="L460">    &lt;td&gt;失败&lt;/td&gt;
# </li><li class="L461" rel="L461">    &lt;td&gt;错误&lt;/td&gt;
# </li><li class="L462" rel="L462">    &lt;td&gt;详细&lt;/td&gt;
# </li><li class="L463" rel="L463">&lt;/tr&gt;
# </li><li class="L464" rel="L464">%(test_list)s
# </li><li class="L465" rel="L465">&lt;tr id=&#39;total_row&#39; class=&#34;text-center info&#34;&gt;
# </li><li class="L466" rel="L466">    &lt;td&gt;总计&lt;/td&gt;
# </li><li class="L467" rel="L467">    &lt;td&gt;%(count)s&lt;/td&gt;
# </li><li class="L468" rel="L468">    &lt;td&gt;%(Pass)s&lt;/td&gt;
# </li><li class="L469" rel="L469">    &lt;td&gt;%(fail)s&lt;/td&gt;
# </li><li class="L470" rel="L470">    &lt;td&gt;%(error)s&lt;/td&gt;
# </li><li class="L471" rel="L471">    &lt;td&gt;通过率：%(passrate)s&lt;/td&gt;
# </li><li class="L472" rel="L472">&lt;/tr&gt;
# </li><li class="L473" rel="L473">&lt;/table&gt;
# </li><li class="L474" rel="L474">&#34;&#34;&#34; # variables: (test_list, count, Pass, fail, error ,passrate)
# </li><li class="L475" rel="L475">
# </li><li class="L476" rel="L476">    REPORT_CLASS_TMPL = r&#34;&#34;&#34;
# </li><li class="L477" rel="L477">&lt;tr class=&#39;%(style)s&#39;&gt;
# </li><li class="L478" rel="L478">    &lt;td&gt;%(desc)s&lt;/td&gt;
# </li><li class="L479" rel="L479">    &lt;td class=&#34;text-center&#34;&gt;%(count)s&lt;/td&gt;
# </li><li class="L480" rel="L480">    &lt;td class=&#34;text-center&#34;&gt;%(Pass)s&lt;/td&gt;
# </li><li class="L481" rel="L481">    &lt;td class=&#34;text-center&#34;&gt;%(fail)s&lt;/td&gt;
# </li><li class="L482" rel="L482">    &lt;td class=&#34;text-center&#34;&gt;%(error)s&lt;/td&gt;
# </li><li class="L483" rel="L483">    &lt;td class=&#34;text-center&#34;&gt;&lt;a href=&#34;javascript:showClassDetail(&#39;%(cid)s&#39;,%(count)s)&#34; class=&#34;detail&#34; id=&#39;%(cid)s&#39;&gt;详细&lt;/a&gt;&lt;/td&gt;
# </li><li class="L484" rel="L484">&lt;/tr&gt;
# </li><li class="L485" rel="L485">&#34;&#34;&#34; # variables: (style, desc, count, Pass, fail, error, cid)
# </li><li class="L486" rel="L486">
# </li><li class="L487" rel="L487">    #有output内容的样式，去掉原来JS效果，美化展示效果  -Findyou v0.8.2.3
# </li><li class="L488" rel="L488">    REPORT_TEST_WITH_OUTPUT_TMPL = r&#34;&#34;&#34;
# </li><li class="L489" rel="L489">&lt;tr id=&#39;%(tid)s&#39; class=&#39;%(Class)s&#39;&gt;
# </li><li class="L490" rel="L490">    &lt;td class=&#39;%(style)s&#39;&gt;&lt;div class=&#39;testcase&#39;&gt;%(desc)s&lt;/div&gt;&lt;/td&gt;
# </li><li class="L491" rel="L491">    &lt;td colspan=&#39;5&#39; align=&#39;center&#39;&gt;
# </li><li class="L492" rel="L492">    &lt;!--默认收起output信息 -Findyou --&gt;
# </li><li class="L493" rel="L493">    &lt;button id=&#39;btn_%(tid)s&#39; type=&#34;button&#34;  class=&#34;btn-xs collapsed&#34; data-toggle=&#34;collapse&#34; data-target=&#39;#div_%(tid)s&#39;&gt;%(status)s&lt;/button&gt;
# </li><li class="L494" rel="L494">    &lt;div id=&#39;div_%(tid)s&#39; class=&#34;collapse&#34;&gt;
# </li><li class="L495" rel="L495">
# </li><li class="L496" rel="L496">    &lt;!-- 默认展开output信息 -Findyou
# </li><li class="L497" rel="L497">    &lt;button id=&#39;btn_%(tid)s&#39; type=&#34;button&#34;  class=&#34;btn-xs&#34; data-toggle=&#34;collapse&#34; data-target=&#39;#div_%(tid)s&#39;&gt;%(status)s&lt;/button&gt;
# </li><li class="L498" rel="L498">    &lt;div id=&#39;div_%(tid)s&#39; class=&#34;collapse in&#34; &gt;  --&gt;
# </li><li class="L499" rel="L499">    &lt;div class=&#39;res&#39;&gt;
# </li><li class="L500" rel="L500">    &lt;h5&gt;请求参数&lt;/h5&gt;
# </li><li class="L501" rel="L501">    &lt;table class=&#39;table&#39;  style=&#34;background-color:#f5f5f5;border-color: #fffefe;&#34; border=&#34;1&#34; cellspacing=&#34;0&#34;&gt;
# </li><li class="L502" rel="L502">    &lt;tr&gt;&lt;th&gt;URL&lt;/th&gt;&lt;td style=&#34;word-break:break-all; word-wrap:break-word;&#34;&gt;%(res_url)s&lt;/td&gt;&lt;/tr&gt;
# </li><li class="L503" rel="L503">    &lt;tr&gt;&lt;th&gt;Method&lt;/th&gt;&lt;td style=&#34;word-break:break-all; word-wrap:break-word;&#34;&gt;%(request_method)s&lt;/td&gt;&lt;/tr&gt;
# </li><li class="L504" rel="L504">    &lt;tr&gt;&lt;th&gt;Headers&lt;/th&gt;&lt;td style=&#34;word-break:break-all; word-wrap:break-word;&#34;&gt;%(request_headers)s&lt;/td&gt;&lt;/tr&gt;
# </li><li class="L505" rel="L505">    &lt;tr&gt;&lt;th&gt;Body&lt;/th&gt;&lt;td style=&#34;word-break:break-all; word-wrap:break-word;&#34;&gt;%(request_str)s&lt;/td&gt;&lt;/tr&gt;
# </li><li class="L506" rel="L506">    &lt;/table&gt;
# </li><li class="L507" rel="L507">    &lt;/div&gt;
# </li><li class="L508" rel="L508">    &lt;div class=&#39;res&#39;&gt;
# </li><li class="L509" rel="L509">    &lt;h5&gt;响应结果&lt;/h5&gt;
# </li><li class="L510" rel="L510">    &lt;table class=&#39;table&#39;  style=&#34;background-color:#f5f5f5;border-color: #fffefe;&#34; border=&#34;1&#34; cellspacing=&#34;0&#34;&gt;
# </li><li class="L511" rel="L511">    &lt;tr&gt;&lt;th&gt;URL&lt;/th&gt;&lt;td style=&#34;word-break:break-all; word-wrap:break-word;&#34;&gt;%(res_url)s&lt;/td&gt;&lt;/tr&gt;
# </li><li class="L512" rel="L512">    &lt;tr&gt;&lt;th&gt;Status&lt;/th&gt;&lt;td style=&#34;word-break:break-all; word-wrap:break-word;&#34;&gt;%(res_code)s&lt;/td&gt;&lt;/tr&gt;
# </li><li class="L513" rel="L513">    &lt;tr&gt;&lt;th&gt;Time&lt;/th&gt;&lt;td style=&#34;word-break:break-all; word-wrap:break-word;&#34;&gt;%(respond_time)s&lt;/td&gt;&lt;/tr&gt;
# </li><li class="L514" rel="L514">    &lt;tr&gt;&lt;th&gt;Headers&lt;/th&gt;&lt;td style=&#34;word-break:break-all; word-wrap:break-word;&#34;&gt;%(res_headers)s&lt;/td&gt;&lt;/tr&gt;
# </li><li class="L515" rel="L515">    &lt;tr&gt;&lt;th&gt;Body&lt;/th&gt;&lt;td style=&#34;word-break:break-all; word-wrap:break-word;&#34;&gt;%(respond_str)s&lt;/td&gt;&lt;/tr&gt;
# </li><li class="L516" rel="L516">    &lt;tr&gt;&lt;th&gt;Expect&lt;/th&gt;&lt;td style=&#34;word-break:break-all; word-wrap:break-word;&#34;&gt;%(res_expect)s&lt;/td&gt;&lt;/tr&gt;
# </li><li class="L517" rel="L517">    &lt;/table&gt;
# </li><li class="L518" rel="L518">    &lt;/div&gt;
# </li><li class="L519" rel="L519">    &lt;div class=&#39;res&#39;&gt;
# </li><li class="L520" rel="L520">    &lt;h5&gt;详细步骤&lt;/h5&gt;
# </li><li class="L521" rel="L521">    &lt;pre&gt;
# </li><li class="L522" rel="L522">    %(script)s
# </li><li class="L523" rel="L523">    &lt;/pre&gt;
# </li><li class="L524" rel="L524">    &lt;/div&gt;
# </li><li class="L525" rel="L525">    &lt;/div&gt;
# </li><li class="L526" rel="L526">    &lt;/td&gt;
# </li><li class="L527" rel="L527">&lt;/tr&gt;
# </li><li class="L528" rel="L528">&#34;&#34;&#34; # variables: (tid, Class, style, desc, status)
# </li><li class="L529" rel="L529">
# </li><li class="L530" rel="L530">    # 无output内容样式改为button，按钮效果为不可点击  -Findyou v0.8.2.3
# </li><li class="L531" rel="L531">    REPORT_TEST_NO_OUTPUT_TMPL = r&#34;&#34;&#34;
# </li><li class="L532" rel="L532">&lt;tr id=&#39;%(tid)s&#39; class=&#39;%(Class)s&#39;&gt;
# </li><li class="L533" rel="L533">    &lt;td class=&#39;%(style)s&#39;&gt;&lt;div class=&#39;testcase&#39;&gt;%(desc)s&lt;/div&gt;&lt;/td&gt;
# </li><li class="L534" rel="L534">    &lt;td colspan=&#39;5&#39; align=&#39;center&#39;&gt;&lt;button id=&#39;btn_%(tid)s&#39; type=&#34;button&#34;  class=&#34;btn-xs&#34; disabled=&#34;disabled&#34; data-toggle=&#34;collapse&#34; data-target=&#39;#div_%(tid)s&#39;&gt;%(status)s&lt;/button&gt;&lt;/td&gt;
# </li><li class="L535" rel="L535">&lt;/tr&gt;
# </li><li class="L536" rel="L536">&#34;&#34;&#34; # variables: (tid, Class, style, desc, status)
# </li><li class="L537" rel="L537">
# </li><li class="L538" rel="L538">    REPORT_TEST_OUTPUT_TMPL = r&#34;&#34;&#34;
# </li><li class="L539" rel="L539">%(id)s: %(output)s
# </li><li class="L540" rel="L540">&#34;&#34;&#34; # variables: (id, output)
# </li><li class="L541" rel="L541">
# </li><li class="L542" rel="L542">    # ------------------------------------------------------------------------
# </li><li class="L543" rel="L543">    # ENDING
# </li><li class="L544" rel="L544">    #
# </li><li class="L545" rel="L545">    # 增加返回顶部按钮  --Findyou
# </li><li class="L546" rel="L546">    ENDING_TMPL = &#34;&#34;&#34;&lt;div id=&#39;ending&#39;&gt;&amp;nbsp;&lt;/div&gt;
# </li><li class="L547" rel="L547">    &lt;div style=&#34; position:fixed;right:50px; bottom:30px; width:20px; height:20px;cursor:pointer&#34;&gt;
# </li><li class="L548" rel="L548">    &lt;a href=&#34;#&#34;&gt;&lt;span class=&#34;glyphicon glyphicon-eject&#34; style = &#34;font-size:30px;&#34; aria-hidden=&#34;true&#34;&gt;
# </li><li class="L549" rel="L549">    &lt;/span&gt;&lt;/a&gt;&lt;/div&gt;
# </li><li class="L550" rel="L550">    &#34;&#34;&#34;
# </li><li class="L551" rel="L551">
# </li><li class="L552" rel="L552"># -------------------- The end of the Template class -------------------
# </li><li class="L553" rel="L553">
# </li><li class="L554" rel="L554">
# </li><li class="L555" rel="L555">TestResult = unittest.TestResult
# </li><li class="L556" rel="L556">
# </li><li class="L557" rel="L557">class _TestResult(TestResult):
# </li><li class="L558" rel="L558">    # note: _TestResult is a pure representation of results.
# </li><li class="L559" rel="L559">    # It lacks the output and reporting ability compares to unittest._TextTestResult.
# </li><li class="L560" rel="L560">
# </li><li class="L561" rel="L561">    def __init__(self, verbosity=1):
# </li><li class="L562" rel="L562">        TestResult.__init__(self)
# </li><li class="L563" rel="L563">        self.stdout0 = None
# </li><li class="L564" rel="L564">        self.stderr0 = None
# </li><li class="L565" rel="L565">        self.success_count = 0
# </li><li class="L566" rel="L566">        self.failure_count = 0
# </li><li class="L567" rel="L567">        self.error_count = 0
# </li><li class="L568" rel="L568">        self.verbosity = verbosity
# </li><li class="L569" rel="L569">
# </li><li class="L570" rel="L570">        # result is a list of result in 4 tuple
# </li><li class="L571" rel="L571">        # (
# </li><li class="L572" rel="L572">        #   result code (0: success; 1: fail; 2: error),
# </li><li class="L573" rel="L573">        #   TestCase object,
# </li><li class="L574" rel="L574">        #   Test output (byte string),
# </li><li class="L575" rel="L575">        #   stack trace,
# </li><li class="L576" rel="L576">        # )
# </li><li class="L577" rel="L577">        self.result = []
# </li><li class="L578" rel="L578">        #增加一个测试通过率 --Findyou
# </li><li class="L579" rel="L579">        self.passrate=float(0)
# </li><li class="L580" rel="L580">        #加入日志记录
# </li><li class="L581" rel="L581">        self.logger = logging.getLogger(&#39;mylog&#39;)
# </li><li class="L582" rel="L582">
# </li><li class="L583" rel="L583">
# </li><li class="L584" rel="L584">    def startTest(self, test):
# </li><li class="L585" rel="L585">        TestResult.startTest(self, test)
# </li><li class="L586" rel="L586">        # just one buffer for both stdout and stderr
# </li><li class="L587" rel="L587">        self.outputBuffer = StringIO()
# </li><li class="L588" rel="L588">        stdout_redirector.fp = self.outputBuffer
# </li><li class="L589" rel="L589">        stderr_redirector.fp = self.outputBuffer
# </li><li class="L590" rel="L590">        self.stdout0 = sys.stdout
# </li><li class="L591" rel="L591">        self.stderr0 = sys.stderr
# </li><li class="L592" rel="L592">        sys.stdout = stdout_redirector
# </li><li class="L593" rel="L593">        sys.stderr = stderr_redirector
# </li><li class="L594" rel="L594">        #加入日志记录
# </li><li class="L595" rel="L595">        self.log_cap = io.StringIO()
# </li><li class="L596" rel="L596">        self.ch = logging.StreamHandler(self.log_cap)
# </li><li class="L597" rel="L597">        self.ch.setLevel(logging.DEBUG)
# </li><li class="L598" rel="L598">        formatter = logging.Formatter(
# </li><li class="L599" rel="L599">            &#39;[%(levelname)s][%(asctime)s]---&gt; %(message)s&#39;)
# </li><li class="L600" rel="L600">        # formatter = logging.Formatter(
# </li><li class="L601" rel="L601">        #     &#39;[%(levelname)s][%(asctime)s] [%(filename)s]-&gt;[%(funcName)s] line:%(lineno)d ---&gt; %(message)s&#39;)
# </li><li class="L602" rel="L602">        self.ch.setFormatter(formatter)
# </li><li class="L603" rel="L603">        self.logger.addHandler(self.ch)
# </li><li class="L604" rel="L604">
# </li><li class="L605" rel="L605">
# </li><li class="L606" rel="L606">
# </li><li class="L607" rel="L607">    def complete_output(self):
# </li><li class="L608" rel="L608">        &#34;&#34;&#34;
# </li><li class="L609" rel="L609">        Disconnect output redirection and return buffer.
# </li><li class="L610" rel="L610">        Safe to call multiple times.
# </li><li class="L611" rel="L611">        &#34;&#34;&#34;
# </li><li class="L612" rel="L612">        if self.stdout0:
# </li><li class="L613" rel="L613">            sys.stdout = self.stdout0
# </li><li class="L614" rel="L614">            sys.stderr = self.stderr0
# </li><li class="L615" rel="L615">            self.stdout0 = None
# </li><li class="L616" rel="L616">            self.stderr0 = None
# </li><li class="L617" rel="L617">        #return self.outputBuffer.getvalue()
# </li><li class="L618" rel="L618">        #加入日志记录
# </li><li class="L619" rel="L619">        return self.outputBuffer.getvalue() + &#39;\n&#39; + self.log_cap.getvalue()
# </li><li class="L620" rel="L620">
# </li><li class="L621" rel="L621">
# </li><li class="L622" rel="L622">    def stopTest(self, test):
# </li><li class="L623" rel="L623">        # Usually one of addSuccess, addError or addFailure would have been called.
# </li><li class="L624" rel="L624">        # But there are some path in unittest that would bypass this.
# </li><li class="L625" rel="L625">        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
# </li><li class="L626" rel="L626">        # 加入日志记录 清除log的handle
# </li><li class="L627" rel="L627">        self.logger.removeHandler(self.ch)
# </li><li class="L628" rel="L628">
# </li><li class="L629" rel="L629">        self.complete_output()
# </li><li class="L630" rel="L630">
# </li><li class="L631" rel="L631">
# </li><li class="L632" rel="L632">    def addSuccess(self, test):
# </li><li class="L633" rel="L633">        self.success_count += 1
# </li><li class="L634" rel="L634">        TestResult.addSuccess(self, test)
# </li><li class="L635" rel="L635">        output = self.complete_output()
# </li><li class="L636" rel="L636">        self.result.append((0, test, output, &#39;&#39;))
# </li><li class="L637" rel="L637">        if self.verbosity &gt; 1:
# </li><li class="L638" rel="L638">            sys.stderr.write(&#39;ok &#39;)
# </li><li class="L639" rel="L639">            sys.stderr.write(str(test))
# </li><li class="L640" rel="L640">            sys.stderr.write(&#39;\n&#39;)
# </li><li class="L641" rel="L641">        else:
# </li><li class="L642" rel="L642">            sys.stderr.write(&#39;.&#39;)
# </li><li class="L643" rel="L643">
# </li><li class="L644" rel="L644">    def addError(self, test, err):
# </li><li class="L645" rel="L645">        self.error_count += 1
# </li><li class="L646" rel="L646">        TestResult.addError(self, test, err)
# </li><li class="L647" rel="L647">        _, _exc_str = self.errors[-1]
# </li><li class="L648" rel="L648">        output = self.complete_output()
# </li><li class="L649" rel="L649">        self.result.append((2, test, output, _exc_str))
# </li><li class="L650" rel="L650">        if self.verbosity &gt; 1:
# </li><li class="L651" rel="L651">            sys.stderr.write(&#39;E  &#39;)
# </li><li class="L652" rel="L652">            sys.stderr.write(str(test))
# </li><li class="L653" rel="L653">            sys.stderr.write(&#39;\n&#39;)
# </li><li class="L654" rel="L654">        else:
# </li><li class="L655" rel="L655">            sys.stderr.write(&#39;E&#39;)
# </li><li class="L656" rel="L656">
# </li><li class="L657" rel="L657">    def addFailure(self, test, err):
# </li><li class="L658" rel="L658">        self.failure_count += 1
# </li><li class="L659" rel="L659">        TestResult.addFailure(self, test, err)
# </li><li class="L660" rel="L660">        _, _exc_str = self.failures[-1]
# </li><li class="L661" rel="L661">        output = self.complete_output()
# </li><li class="L662" rel="L662">        self.result.append((1, test, output, _exc_str))
# </li><li class="L663" rel="L663">        if self.verbosity &gt; 1:
# </li><li class="L664" rel="L664">            sys.stderr.write(&#39;F  &#39;)
# </li><li class="L665" rel="L665">            sys.stderr.write(str(test))
# </li><li class="L666" rel="L666">            sys.stderr.write(&#39;\n&#39;)
# </li><li class="L667" rel="L667">        else:
# </li><li class="L668" rel="L668">            sys.stderr.write(&#39;F&#39;)
# </li><li class="L669" rel="L669">
# </li><li class="L670" rel="L670">
# </li><li class="L671" rel="L671">class HTMLTestReportCN(Template_mixin):
# </li><li class="L672" rel="L672">    &#34;&#34;&#34;
# </li><li class="L673" rel="L673">    &#34;&#34;&#34;
# </li><li class="L674" rel="L674">    def __init__(self, stream=sys.stdout, verbosity=1,title=None,description=None,tester=None):
# </li><li class="L675" rel="L675">        self.stream = stream
# </li><li class="L676" rel="L676">        self.verbosity = verbosity
# </li><li class="L677" rel="L677">        if title is None:
# </li><li class="L678" rel="L678">            self.title = self.DEFAULT_TITLE
# </li><li class="L679" rel="L679">        else:
# </li><li class="L680" rel="L680">            self.title = title
# </li><li class="L681" rel="L681">        if description is None:
# </li><li class="L682" rel="L682">            self.description = self.DEFAULT_DESCRIPTION
# </li><li class="L683" rel="L683">        else:
# </li><li class="L684" rel="L684">            self.description = description
# </li><li class="L685" rel="L685">        if tester is None:
# </li><li class="L686" rel="L686">            self.tester = self.DEFAULT_TESTER
# </li><li class="L687" rel="L687">        else:
# </li><li class="L688" rel="L688">            self.tester = tester
# </li><li class="L689" rel="L689">
# </li><li class="L690" rel="L690">        self.startTime = datetime.datetime.now()
# </li><li class="L691" rel="L691">        #add line
# </li><li class="L692" rel="L692">        self.line_name=[]
# </li><li class="L693" rel="L693">        self.line_time=[]
# </li><li class="L694" rel="L694">
# </li><li class="L695" rel="L695">
# </li><li class="L696" rel="L696">    def run(self, test):
# </li><li class="L697" rel="L697">        &#34;Run the given test case or test suite.&#34;
# </li><li class="L698" rel="L698">        result = _TestResult(self.verbosity)
# </li><li class="L699" rel="L699">        test(result)
# </li><li class="L700" rel="L700">        self.stopTime = datetime.datetime.now()
# </li><li class="L701" rel="L701">        self.generateReport(test, result)
# </li><li class="L702" rel="L702">        # print &gt;&gt;sys.stderr, &#39;\nTime Elapsed: %s&#39; % (self.stopTime-self.startTime)
# </li><li class="L703" rel="L703">        sys.stderr.write(&#39;\nTime Elapsed: %s&#39; % (self.stopTime-self.startTime))
# </li><li class="L704" rel="L704">        return result
# </li><li class="L705" rel="L705">
# </li><li class="L706" rel="L706">
# </li><li class="L707" rel="L707">    def sortResult(self, result_list):
# </li><li class="L708" rel="L708">        # unittest does not seems to run in any particular order.
# </li><li class="L709" rel="L709">        # Here at least we want to group them together by class.
# </li><li class="L710" rel="L710">        rmap = {}
# </li><li class="L711" rel="L711">        classes = []
# </li><li class="L712" rel="L712">        for n,t,o,e in result_list:
# </li><li class="L713" rel="L713">            cls = t.__class__
# </li><li class="L714" rel="L714">            # if not rmap.has_key(cls):
# </li><li class="L715" rel="L715">            if cls not in rmap:
# </li><li class="L716" rel="L716">                rmap[cls] = []
# </li><li class="L717" rel="L717">                classes.append(cls)
# </li><li class="L718" rel="L718">            rmap[cls].append((n,t,o,e))
# </li><li class="L719" rel="L719">        r = [(cls, rmap[cls]) for cls in classes]
# </li><li class="L720" rel="L720">        return r
# </li><li class="L721" rel="L721">
# </li><li class="L722" rel="L722">    #替换测试结果status为通过率 --Findyou
# </li><li class="L723" rel="L723">    def getReportAttributes(self, result):
# </li><li class="L724" rel="L724">        &#34;&#34;&#34;
# </li><li class="L725" rel="L725">        Return report attributes as a list of (name, value).
# </li><li class="L726" rel="L726">        Override this to add custom attributes.
# </li><li class="L727" rel="L727">        &#34;&#34;&#34;
# </li><li class="L728" rel="L728">        startTime = str(self.startTime)[:19]
# </li><li class="L729" rel="L729">        duration = str(self.stopTime - self.startTime)
# </li><li class="L730" rel="L730">        status = []
# </li><li class="L731" rel="L731">        status.append(&#39;共 %s&#39; % (result.success_count + result.failure_count + result.error_count))
# </li><li class="L732" rel="L732">        if result.success_count: status.append(&#39;通过 %s&#39;    % result.success_count)
# </li><li class="L733" rel="L733">        if result.failure_count: status.append(&#39;失败 %s&#39; % result.failure_count)
# </li><li class="L734" rel="L734">        if result.error_count:   status.append(&#39;错误 %s&#39;   % result.error_count  )
# </li><li class="L735" rel="L735">        if status:
# </li><li class="L736" rel="L736">            status = &#39;，&#39;.join(status)
# </li><li class="L737" rel="L737">        # 合入Github：boafantasy代码
# </li><li class="L738" rel="L738">            if (result.success_count + result.failure_count + result.error_count) &gt; 0:
# </li><li class="L739" rel="L739">                self.passrate = str(&#34;%.2f%%&#34; % (float(result.success_count) / float(result.success_count + result.failure_count + result.error_count) * 100))
# </li><li class="L740" rel="L740">            else:
# </li><li class="L741" rel="L741">                self.passrate = &#34;0.00 %&#34;
# </li><li class="L742" rel="L742">        else:
# </li><li class="L743" rel="L743">            status = &#39;none&#39;
# </li><li class="L744" rel="L744">        return [
# </li><li class="L745" rel="L745">            (u&#39;测试人员&#39;, self.tester),
# </li><li class="L746" rel="L746">            (u&#39;开始时间&#39;,startTime),
# </li><li class="L747" rel="L747">            (u&#39;合计耗时&#39;,duration),
# </li><li class="L748" rel="L748">            (u&#39;测试结果&#39;,status + &#34;，通过率= &#34;+self.passrate),
# </li><li class="L749" rel="L749">        ]
# </li><li class="L750" rel="L750">
# </li><li class="L751" rel="L751">
# </li><li class="L752" rel="L752">    def generateReport(self, test, result):
# </li><li class="L753" rel="L753">        report_attrs = self.getReportAttributes(result)
# </li><li class="L754" rel="L754">        generator = &#39;HTMLTestReportCN %s&#39; % __version__
# </li><li class="L755" rel="L755">        stylesheet = self._generate_stylesheet()
# </li><li class="L756" rel="L756">        heading = self._generate_heading(report_attrs)
# </li><li class="L757" rel="L757">        report = self._generate_report(result)
# </li><li class="L758" rel="L758">        ending = self._generate_ending()
# </li><li class="L759" rel="L759">        output = self.HTML_TMPL % dict(
# </li><li class="L760" rel="L760">            title = saxutils.escape(self.title),
# </li><li class="L761" rel="L761">            generator = generator,
# </li><li class="L762" rel="L762">            stylesheet = stylesheet,
# </li><li class="L763" rel="L763">            heading = heading,
# </li><li class="L764" rel="L764">            report = report,
# </li><li class="L765" rel="L765">            ending = ending,
# </li><li class="L766" rel="L766">            line_name=self.line_name,
# </li><li class="L767" rel="L767">            line_time=self.line_time
# </li><li class="L768" rel="L768">        )
# </li><li class="L769" rel="L769">        self.stream.write(output.encode(&#39;utf8&#39;))
# </li><li class="L770" rel="L770">
# </li><li class="L771" rel="L771">
# </li><li class="L772" rel="L772">    def _generate_stylesheet(self):
# </li><li class="L773" rel="L773">        return self.STYLESHEET_TMPL
# </li><li class="L774" rel="L774">
# </li><li class="L775" rel="L775">    #增加Tester显示 -Findyou
# </li><li class="L776" rel="L776">    def _generate_heading(self, report_attrs):
# </li><li class="L777" rel="L777">        a_lines = []
# </li><li class="L778" rel="L778">        for name, value in report_attrs:
# </li><li class="L779" rel="L779">            line = self.HEADING_ATTRIBUTE_TMPL % dict(
# </li><li class="L780" rel="L780">                    name = saxutils.escape(name),
# </li><li class="L781" rel="L781">                    value = saxutils.escape(value),
# </li><li class="L782" rel="L782">                )
# </li><li class="L783" rel="L783">            a_lines.append(line)
# </li><li class="L784" rel="L784">        heading = self.HEADING_TMPL % dict(
# </li><li class="L785" rel="L785">            title = saxutils.escape(self.title),
# </li><li class="L786" rel="L786">            parameters = &#39;&#39;.join(a_lines),
# </li><li class="L787" rel="L787">            description = saxutils.escape(self.description),
# </li><li class="L788" rel="L788">            tester= saxutils.escape(self.tester),
# </li><li class="L789" rel="L789">        )
# </li><li class="L790" rel="L790">        return heading
# </li><li class="L791" rel="L791">
# </li><li class="L792" rel="L792">    #生成报告  --Findyou添加注释
# </li><li class="L793" rel="L793">    def _generate_report(self, result):
# </li><li class="L794" rel="L794">        rows = []
# </li><li class="L795" rel="L795">        sortedResult = self.sortResult(result.result)
# </li><li class="L796" rel="L796">        for cid, (cls, cls_results) in enumerate(sortedResult):
# </li><li class="L797" rel="L797">            # subtotal for a class
# </li><li class="L798" rel="L798">            np = nf = ne = 0
# </li><li class="L799" rel="L799">            for n,t,o,e in cls_results:
# </li><li class="L800" rel="L800">                if n == 0: np += 1
# </li><li class="L801" rel="L801">                elif n == 1: nf += 1
# </li><li class="L802" rel="L802">                else: ne += 1
# </li><li class="L803" rel="L803">                #add line
# </li><li class="L804" rel="L804">                if o.__contains__(&#39;响应时间&#39;):
# </li><li class="L805" rel="L805">                    self.line_name.append(t._testMethodName)
# </li><li class="L806" rel="L806">                    s = re.findall(&#39;响应时间 (.+?) ms&#39;, o)
# </li><li class="L807" rel="L807">                    time=int(&#34;&#34;.join(s))
# </li><li class="L808" rel="L808">                    self.line_time.append(time)
# </li><li class="L809" rel="L809">
# </li><li class="L810" rel="L810">            # format class description
# </li><li class="L811" rel="L811">            if cls.__module__ == &#34;__main__&#34;:
# </li><li class="L812" rel="L812">                name = cls.__name__
# </li><li class="L813" rel="L813">            else:
# </li><li class="L814" rel="L814">                name = &#34;%s.%s&#34; % (cls.__module__, cls.__name__)
# </li><li class="L815" rel="L815">            doc = cls.__doc__ and cls.__doc__.split(&#34;\n&#34;)[0] or &#34;&#34;
# </li><li class="L816" rel="L816">            desc = doc and &#39;%s: %s&#39; % (name, doc) or name
# </li><li class="L817" rel="L817">
# </li><li class="L818" rel="L818">            row = self.REPORT_CLASS_TMPL % dict(
# </li><li class="L819" rel="L819">                style = ne &gt; 0 and &#39;warning&#39; or nf &gt; 0 and &#39;danger&#39; or &#39;success&#39;,
# </li><li class="L820" rel="L820">                desc = desc,
# </li><li class="L821" rel="L821">                count = np+nf+ne,
# </li><li class="L822" rel="L822">                Pass = np,
# </li><li class="L823" rel="L823">                fail = nf,
# </li><li class="L824" rel="L824">                error = ne,
# </li><li class="L825" rel="L825">                cid = &#39;c%s&#39; % (cid+1),
# </li><li class="L826" rel="L826">            )
# </li><li class="L827" rel="L827">            rows.append(row)
# </li><li class="L828" rel="L828">
# </li><li class="L829" rel="L829">            for tid, (n,t,o,e) in enumerate(cls_results):
# </li><li class="L830" rel="L830">                self._generate_report_test(rows, cid, tid, n, t, o, e)
# </li><li class="L831" rel="L831">
# </li><li class="L832" rel="L832">        report = self.REPORT_TMPL % dict(
# </li><li class="L833" rel="L833">            test_list = &#39;&#39;.join(rows),
# </li><li class="L834" rel="L834">            count = str(result.success_count+result.failure_count+result.error_count),
# </li><li class="L835" rel="L835">            Pass = str(result.success_count),
# </li><li class="L836" rel="L836">            fail = str(result.failure_count),
# </li><li class="L837" rel="L837">            error = str(result.error_count),
# </li><li class="L838" rel="L838">            passrate =self.passrate,
# </li><li class="L839" rel="L839">        )
# </li><li class="L840" rel="L840">        return report
# </li><li class="L841" rel="L841">
# </li><li class="L842" rel="L842">
# </li><li class="L843" rel="L843">    def _generate_report_test(self, rows, cid, tid, n, t, o, e):
# </li><li class="L844" rel="L844">        # e.g. &#39;pt1.1&#39;, &#39;ft1.1&#39;, etc
# </li><li class="L845" rel="L845">        has_output = bool(o or e)
# </li><li class="L846" rel="L846">        # ID修改点为下划线,支持Bootstrap折叠展开特效 - Findyou v0.8.2.1
# </li><li class="L847" rel="L847">        #增加error分类 - Findyou v0.8.2.3
# </li><li class="L848" rel="L848">        tid = (n == 0 and &#39;p&#39; or n == 1 and &#39;f&#39; or &#39;e&#39;) + &#39;t%s_%s&#39; % (cid + 1, tid + 1)
# </li><li class="L849" rel="L849">        name = (t.id().split(&#39;.&#39;)[-1])
# </li><li class="L850" rel="L850">        doc = t.shortDescription() or &#34;&#34;
# </li><li class="L851" rel="L851">        desc = doc and (&#39;%s: %s&#39; % (name, doc)) or name
# </li><li class="L852" rel="L852">        tmpl = has_output and self.REPORT_TEST_WITH_OUTPUT_TMPL or self.REPORT_TEST_NO_OUTPUT_TMPL
# </li><li class="L853" rel="L853">
# </li><li class="L854" rel="L854">        # utf-8 支持中文 - Findyou
# </li><li class="L855" rel="L855">         # o and e should be byte string because they are collected from stdout and stderr?
# </li><li class="L856" rel="L856">        if isinstance(o, str):
# </li><li class="L857" rel="L857">            # TODO: some problem with &#39;string_escape&#39;: it escape \n and mess up formating
# </li><li class="L858" rel="L858">            # uo = unicode(o.encode(&#39;string_escape&#39;))
# </li><li class="L859" rel="L859">            try:
# </li><li class="L860" rel="L860">                uo = o
# </li><li class="L861" rel="L861">            except:
# </li><li class="L862" rel="L862">                uo = o.decode(&#39;utf-8&#39;)
# </li><li class="L863" rel="L863">        else:
# </li><li class="L864" rel="L864">            uo = o
# </li><li class="L865" rel="L865">        if isinstance(e, str):
# </li><li class="L866" rel="L866">            # TODO: some problem with &#39;string_escape&#39;: it escape \n and mess up formating
# </li><li class="L867" rel="L867">            # ue = unicode(e.encode(&#39;string_escape&#39;))
# </li><li class="L868" rel="L868">            try:
# </li><li class="L869" rel="L869">                ue = e
# </li><li class="L870" rel="L870">            except:
# </li><li class="L871" rel="L871">                ue = e.decode(&#39;utf-8&#39;)
# </li><li class="L872" rel="L872">        else:
# </li><li class="L873" rel="L873">            ue = e
# </li><li class="L874" rel="L874">
# </li><li class="L875" rel="L875">        script = self.REPORT_TEST_OUTPUT_TMPL % dict(
# </li><li class="L876" rel="L876">            id = tid,
# </li><li class="L877" rel="L877">            output = saxutils.escape(uo+ue),
# </li><li class="L878" rel="L878">        )
# </li><li class="L879" rel="L879">
# </li><li class="L880" rel="L880">        row = tmpl % dict(
# </li><li class="L881" rel="L881">            tid = tid,
# </li><li class="L882" rel="L882">            Class = (n == 0 and &#39;hiddenRow&#39; or &#39;none&#39;),
# </li><li class="L883" rel="L883">            style = n == 2 and &#39;errorCase&#39; or (n == 1 and &#39;failCase&#39; or &#39;passCase&#39;),
# </li><li class="L884" rel="L884">            desc = desc,
# </li><li class="L885" rel="L885">            script = script,
# </li><li class="L886" rel="L886">            #加入请求和响应信息列 wulinhao
# </li><li class="L887" rel="L887">            request_str=get_req_scri(script),
# </li><li class="L888" rel="L888">            respond_str=get_res_scri(script),
# </li><li class="L889" rel="L889">            res_url=get_res_url(script),
# </li><li class="L890" rel="L890">            res_code=get_res_code(script),
# </li><li class="L891" rel="L891">            res_headers=get_res_headers(script),
# </li><li class="L892" rel="L892">            res_expect=get_res_expect(script),
# </li><li class="L893" rel="L893">            request_headers=get_request_headers(script),
# </li><li class="L894" rel="L894">            request_method=get_request_method(script),
# </li><li class="L895" rel="L895">            respond_time=get_respond_time(script),
# </li><li class="L896" rel="L896">            #
# </li><li class="L897" rel="L897">            status = self.STATUS[n],
# </li><li class="L898" rel="L898">        )
# </li><li class="L899" rel="L899">        rows.append(row)
# </li><li class="L900" rel="L900">        if not has_output:
# </li><li class="L901" rel="L901">            return
# </li><li class="L902" rel="L902">
# </li><li class="L903" rel="L903">    def _generate_ending(self):
# </li><li class="L904" rel="L904">        return self.ENDING_TMPL
# </li><li class="L905" rel="L905">
# </li><li class="L906" rel="L906"># 加入请求信息列和响应信息列 wulinhao
# </li><li class="L907" rel="L907">def get_req_scri(script):
# </li><li class="L908" rel="L908">    if(script):
# </li><li class="L909" rel="L909">        strlist = script.split(&#39;[INFO]&#39;)
# </li><li class="L910" rel="L910">        for v in strlist:
# </li><li class="L911" rel="L911">            if v.__contains__(&#39;获取没有依赖的请求参数&#39;):
# </li><li class="L912" rel="L912">                re=v.split(&#39;\n&#39;)
# </li><li class="L913" rel="L913">                return re[1]
# </li><li class="L914" rel="L914">
# </li><li class="L915" rel="L915">            if v.__contains__(&#39;最终&#39;):
# </li><li class="L916" rel="L916">                re = v.split(&#39;\n&#39;)
# </li><li class="L917" rel="L917">                return re[1]
# </li><li class="L918" rel="L918">
# </li><li class="L919" rel="L919">        return &#39;&#39;
# </li><li class="L920" rel="L920">    return &#39;&#39;
# </li><li class="L921" rel="L921">
# </li><li class="L922" rel="L922"># 加入请求信息列和响应信息列 wulinhao
# </li><li class="L923" rel="L923">def get_res_scri(script,req=True):
# </li><li class="L924" rel="L924">
# </li><li class="L925" rel="L925">    if(script):
# </li><li class="L926" rel="L926">        strlist = script.split(&#39;[INFO]&#39;)
# </li><li class="L927" rel="L927">        for v in strlist:
# </li><li class="L928" rel="L928">            if v.__contains__(&#39;响应结果:&#39;):
# </li><li class="L929" rel="L929">                re=v.split(&#39;\n&#39;)
# </li><li class="L930" rel="L930">                return re[1]
# </li><li class="L931" rel="L931">        return &#39;&#39;
# </li><li class="L932" rel="L932">    return &#39;&#39;
# </li><li class="L933" rel="L933">
# </li><li class="L934" rel="L934">def get_res_url(script):
# </li><li class="L935" rel="L935">
# </li><li class="L936" rel="L936">    if(script):
# </li><li class="L937" rel="L937">        strlist = script.split(&#39;[INFO]&#39;)
# </li><li class="L938" rel="L938">        for v in strlist:
# </li><li class="L939" rel="L939">            if v.__contains__(&#39;获取请求地址&#39;):
# </li><li class="L940" rel="L940">                re=v.split(&#39;\n&#39;)
# </li><li class="L941" rel="L941">                return re[1]
# </li><li class="L942" rel="L942">        return &#39;&#39;
# </li><li class="L943" rel="L943">    return &#39;&#39;
# </li><li class="L944" rel="L944">
# </li><li class="L945" rel="L945">def get_res_code(script):
# </li><li class="L946" rel="L946">
# </li><li class="L947" rel="L947">    if(script):
# </li><li class="L948" rel="L948">        strlist = script.split(&#39;[INFO]&#39;)
# </li><li class="L949" rel="L949">        for v in strlist:
# </li><li class="L950" rel="L950">            if v.__contains__(&#39;status_code&#39;):
# </li><li class="L951" rel="L951">                re=v.split(&#39;status_code&#39;)
# </li><li class="L952" rel="L952">                return re[1]
# </li><li class="L953" rel="L953">        return &#39;&#39;
# </li><li class="L954" rel="L954">    return &#39;&#39;
# </li><li class="L955" rel="L955">
# </li><li class="L956" rel="L956">def get_res_headers(script):
# </li><li class="L957" rel="L957">
# </li><li class="L958" rel="L958">    if(script):
# </li><li class="L959" rel="L959">        strlist = script.split(&#39;[INFO]&#39;)
# </li><li class="L960" rel="L960">        for v in strlist:
# </li><li class="L961" rel="L961">            if v.__contains__(&#39;respond_headers&#39;):
# </li><li class="L962" rel="L962">                re=v.split(&#39;respond_headers&#39;)
# </li><li class="L963" rel="L963">                if re[1].__contains__(&#39;[ERROR]&#39;):
# </li><li class="L964" rel="L964">                    r = re[1].split(&#39;[ERROR]&#39;)
# </li><li class="L965" rel="L965">                    return r[0]
# </li><li class="L966" rel="L966">                return re[1]
# </li><li class="L967" rel="L967">        return &#39;&#39;
# </li><li class="L968" rel="L968">    return &#39;&#39;
# </li><li class="L969" rel="L969">
# </li><li class="L970" rel="L970">def get_res_expect(script):
# </li><li class="L971" rel="L971">
# </li><li class="L972" rel="L972">    if(script):
# </li><li class="L973" rel="L973">        strlist = script.split(&#39;[INFO]&#39;)
# </li><li class="L974" rel="L974">        for v in strlist:
# </li><li class="L975" rel="L975">            if v.__contains__(&#39;获取预期结果&#39;):
# </li><li class="L976" rel="L976">                re=v.split(&#39;获取预期结果&#39;)
# </li><li class="L977" rel="L977">                return re[1]
# </li><li class="L978" rel="L978">        return &#39;&#39;
# </li><li class="L979" rel="L979">    return &#39;&#39;
# </li><li class="L980" rel="L980">
# </li><li class="L981" rel="L981">def get_request_headers(script):
# </li><li class="L982" rel="L982">
# </li><li class="L983" rel="L983">    if(script):
# </li><li class="L984" rel="L984">        strlist = script.split(&#39;[INFO]&#39;)
# </li><li class="L985" rel="L985">        for v in strlist:
# </li><li class="L986" rel="L986">            if v.__contains__(&#39;request_headers&#39;):
# </li><li class="L987" rel="L987">                re=v.split(&#39;request_headers&#39;)
# </li><li class="L988" rel="L988">                if re[1].__contains__(&#39;{}&#39;) or not re[1]:
# </li><li class="L989" rel="L989">                    return &#39;Content-type:application/json&#39;
# </li><li class="L990" rel="L990">                return re[1]
# </li><li class="L991" rel="L991">        return &#39;&#39;
# </li><li class="L992" rel="L992">    return &#39;&#39;
# </li><li class="L993" rel="L993">
# </li><li class="L994" rel="L994">
# </li><li class="L995" rel="L995">def get_request_method(script):
# </li><li class="L996" rel="L996">
# </li><li class="L997" rel="L997">    if(script):
# </li><li class="L998" rel="L998">        strlist = script.split(&#39;[INFO]&#39;)
# </li><li class="L999" rel="L999">        for v in strlist:
# </li><li class="L1000" rel="L1000">            if v.__contains__(&#39;获取请求方式&#39;):
# </li><li class="L1001" rel="L1001">                re=v.split(&#39;获取请求方式&#39;)
# </li><li class="L1002" rel="L1002">                return re[1]
# </li><li class="L1003" rel="L1003">        return &#39;&#39;
# </li><li class="L1004" rel="L1004">    return &#39;&#39;
# </li><li class="L1005" rel="L1005">
# </li><li class="L1006" rel="L1006">
# </li><li class="L1007" rel="L1007">def get_respond_time(script):
# </li><li class="L1008" rel="L1008">
# </li><li class="L1009" rel="L1009">    if(script):
# </li><li class="L1010" rel="L1010">        strlist = script.split(&#39;[INFO]&#39;)
# </li><li class="L1011" rel="L1011">        for v in strlist:
# </li><li class="L1012" rel="L1012">            if v.__contains__(&#39;响应时间&#39;):
# </li><li class="L1013" rel="L1013">                re=v.split(&#39;响应时间&#39;)
# </li><li class="L1014" rel="L1014">                return re[1]
# </li><li class="L1015" rel="L1015">        return &#39;&#39;
# </li><li class="L1016" rel="L1016">    return &#39;&#39;
# </li><li class="L1017" rel="L1017">##############################################################################
# </li><li class="L1018" rel="L1018"># Facilities for running tests from the command line
# </li><li class="L1019" rel="L1019">##############################################################################
# </li><li class="L1020" rel="L1020">
# </li><li class="L1021" rel="L1021"># Note: Reuse unittest.TestProgram to launch test. In the future we may
# </li><li class="L1022" rel="L1022"># build our own launcher to support more specific command line
# </li><li class="L1023" rel="L1023"># parameters like test title, CSS, etc.
# </li><li class="L1024" rel="L1024">class TestProgram(unittest.TestProgram):
# </li><li class="L1025" rel="L1025">    &#34;&#34;&#34;
# </li><li class="L1026" rel="L1026">    A variation of the unittest.TestProgram. Please refer to the base
# </li><li class="L1027" rel="L1027">    class for command line parameters.
# </li><li class="L1028" rel="L1028">    &#34;&#34;&#34;
# </li><li class="L1029" rel="L1029">    def runTests(self):
# </li><li class="L1030" rel="L1030">        # Pick HTMLTestReportCN as the default test runner.
# </li><li class="L1031" rel="L1031">        # base class&#39;s testRunner parameter is not useful because it means
# </li><li class="L1032" rel="L1032">        # we have to instantiate HTMLTestReportCN before we know self.verbosity.
# </li><li class="L1033" rel="L1033">        if self.testRunner is None:
# </li><li class="L1034" rel="L1034">            self.testRunner = HTMLTestReportCN(verbosity=self.verbosity)
# </li><li class="L1035" rel="L1035">        unittest.TestProgram.runTests(self)
# </li><li class="L1036" rel="L1036">
# </li><li class="L1037" rel="L1037">main = TestProgram
# </li><li class="L1038" rel="L1038">
# </li><li class="L1039" rel="L1039">##############################################################################
# </li><li class="L1040" rel="L1040"># Executing this module from the command line
# </li><li class="L1041" rel="L1041">##############################################################################
# </li><li class="L1042" rel="L1042">
# </li><li class="L1043" rel="L1043">if __name__ == &#34;__main__&#34;:
# </li><li class="L1044" rel="L1044">    main(module=None)</li></ol></code></pre></td>
#
# 						</tr>
# 					</tbody>
# 				</table>
#
# 		</div>
# 	</div>
# </div>
#
# <script>
# function submitDeleteForm() {
#     var message = prompt("delete_confirm_message\n\ndelete_commit_summary", "Delete ''");
#     if (message != null) {
#         $("#delete-message").val(message);
#         $("#delete-file-form").submit()
#     }
# }
# </script>
#
#
# 	</div>
# </div>
#
#
#
#
# 	</div>
#
#
#
# 	<footer>
# 	<div class="ui container">
# 		<div class="ui left">
# 			Powered by Gitea 当前版本: 1.11.4 页面: <strong>31ms</strong> 模板: <strong>3ms</strong>
# 		</div>
# 		<div class="ui right links">
#
# 			<div class="ui language bottom floating slide up dropdown link item">
# 				<i class="world icon"></i>
# 				<div class="text">简体中文</div>
# 				<div class="menu">
#
# 						<a lang="zh-CN" class="item active selected" href="#">简体中文</a>
#
# 						<a lang="en-US" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=en-US">English</a>
#
# 						<a lang="zh-HK" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=zh-HK">繁體中文（香港）</a>
#
# 						<a lang="zh-TW" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=zh-TW">繁體中文（台灣）</a>
#
# 						<a lang="de-DE" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=de-DE">Deutsch</a>
#
# 						<a lang="fr-FR" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=fr-FR">français</a>
#
# 						<a lang="nl-NL" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=nl-NL">Nederlands</a>
#
# 						<a lang="lv-LV" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=lv-LV">latviešu</a>
#
# 						<a lang="ru-RU" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=ru-RU">русский</a>
#
# 						<a lang="uk-UA" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=uk-UA">Українська</a>
#
# 						<a lang="ja-JP" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=ja-JP">日本語</a>
#
# 						<a lang="es-ES" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=es-ES">español</a>
#
# 						<a lang="pt-BR" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=pt-BR">português do Brasil</a>
#
# 						<a lang="pl-PL" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=pl-PL">polski</a>
#
# 						<a lang="bg-BG" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=bg-BG">български</a>
#
# 						<a lang="it-IT" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=it-IT">italiano</a>
#
# 						<a lang="fi-FI" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=fi-FI">suomi</a>
#
# 						<a lang="tr-TR" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=tr-TR">Türkçe</a>
#
# 						<a lang="cs-CZ" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=cs-CZ">čeština</a>
#
# 						<a lang="sr-SP" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=sr-SP">српски</a>
#
# 						<a lang="sv-SE" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=sv-SE">svenska</a>
#
# 						<a lang="ko-KR" class="item " href="/wulinhao/apitest/src/branch/local_test/report/HTMLTestRunnerCN.py?lang=ko-KR">한국어</a>
#
# 				</div>
# 			</div>
# 			<a href="/vendor/librejs.html" data-jslicense="1">JavaScript licenses</a>
# 			<a href="/api/swagger">API</a>
# 			<a target="_blank" rel="noopener noreferrer" href="https://gitea.io">官方网站</a>
#
# 			<span class="version">Go1.13.9</span>
# 		</div>
# 	</div>
# </footer>
#
#
# 	<script src="/vendor/plugins/jquery/jquery.min.js?v=3.4.1"></script>
# 	<script src="/vendor/plugins/jquery-migrate/jquery-migrate.min.js?v=3.0.1"></script>
# 	<script src="/vendor/plugins/jquery.areyousure/jquery.are-you-sure.js"></script>
#
#
#
#
# 	<script src="/vendor/plugins/highlight/highlight.pack.js"></script>
#
#
#
#
#
#
#
# 	<script src="/vendor/plugins/emojify/emojify.custom.js"></script>
# 	<script src="/vendor/plugins/clipboard/clipboard.min.js"></script>
# 	<script src="/vendor/plugins/vue/vue.min.js"></script>
#
#
# 	<script src="/vendor/plugins/fomantic/semantic.min.js?v=2150802f140babb659fb7f59b121e3e9"></script>
# 	<script src="/js/index.js?v=2150802f140babb659fb7f59b121e3e9"></script>
#
#
# </body>
# </html>
#
'''