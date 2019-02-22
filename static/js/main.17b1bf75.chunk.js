(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{19:function(e,n,t){e.exports=t(32)},25:function(e,n,t){},26:function(e,n,t){},27:function(e,n,t){},28:function(e,n,t){},31:function(e,n,t){},32:function(e,n,t){"use strict";t.r(n);var a=t(0),r=t.n(a),o=t(12),l=t.n(o),c=(t(25),t(8)),i=t(7),s=t(11),u=t(9),m=t(10);t(26);function d(e){var n=e.selected===e.alt;return r.a.createElement("li",{className:n?"selected":""},r.a.createElement("img",{src:e.link,alt:e.alt,onClick:function(n){return e.onClick(n)}}),r.a.createElement("span",null,e.alt))}t(27);var h=function(e){function n(){return Object(c.a)(this,n),Object(s.a)(this,Object(u.a)(n).apply(this,arguments))}return Object(m.a)(n,e),Object(i.a)(n,[{key:"renderFoodItem",value:function(e,n,t){return r.a.createElement(d,{key:e.key,link:e.image,alt:e.key,onClick:n,selected:t})}},{key:"render",value:function(e){var n=this,t=this.props.foods.map(function(e){return n.renderFoodItem(e,n.props.onClick,n.props.selected)});return r.a.createElement(r.a.Fragment,null,r.a.createElement("p",null,r.a.createElement("strong",null,"Selected food:")," ",this.props.selected),r.a.createElement("section",{className:"FoodsContainer"},r.a.createElement("ul",null,t)))}}]),n}(a.Component),f=t(3),p=t.n(f),g=t(34),y=t(37),k=t(35),v=t(36),b=(t(28),function(e){function n(e){var t;return Object(c.a)(this,n),(t=Object(s.a)(this,Object(u.a)(n).call(this,e))).colors=["green","red","blue","orange"],t.markers={green:p.a.icon({iconUrl:"iconGreen.png",iconSize:[20,20]}),red:p.a.icon({iconUrl:"iconRed.png",iconSize:[20,20]}),blue:p.a.icon({iconUrl:"iconBlue.png",iconSize:[20,20]}),orange:p.a.icon({iconUrl:"iconOrange.png",iconSize:[20,20]})},t}return Object(m.a)(n,e),Object(i.a)(n,[{key:"renderMarker",value:function(e,n){var t=[e.lat,e.lng];return r.a.createElement(g.a,{key:t[0]+t[1],position:t,icon:this.markers[n]},r.a.createElement(y.a,null,e.name," ",r.a.createElement("br",null)," ",e.synonyms))}},{key:"render",value:function(e){var n=this,t={},a=0,o=this.props.places.map(function(e){var r,o=!0,l=!1,c=void 0;try{for(var i,s=e.synonyms[Symbol.iterator]();!(o=(i=s.next()).done);o=!0){var u=i.value;t.hasOwnProperty(u)?r=t[u]:(t[u]=n.colors[a],r=t[u],a+=1)}}catch(m){l=!0,c=m}finally{try{o||null==s.return||s.return()}finally{if(l)throw c}}return n.renderMarker(e,r)}),l=[40.73061,-73.935242];return r.a.createElement(k.a,{center:l,zoom:3},r.a.createElement(v.a,{attribution:'\xa9 <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',url:"http://{s}.tile.osm.org/{z}/{x}/{y}.png"}),o)}}]),n}(a.Component)),E=(t(31),function(e){function n(e){var t;return Object(c.a)(this,n),(t=Object(s.a)(this,Object(u.a)(n).call(this,e))).componentDidMount=function(){t.setState({loading:!0}),t.data.all=t.readJson(t.jsonPath).then(function(e){t.data.all=e,console.log("original data",t.data.all),t.data.all.sort(t.comparePlaceFrequency),console.log("after sort",t.data.all),t.data.images=e.map(function(e){return{key:e.key,image:e.image}}),console.log("The data was loaded",t.data.all,t.data.images),t.setState({loading:!1})})},t.handleClick=function(e){t.setState({selectedFood:e.currentTarget.alt,places:t.data.all.find(function(n){return n.key===e.currentTarget.alt}).places})},t.data={images:[],all:{}},t.state={selectedFood:"almond",places:[],loading:!0},t.jsonPath="/distribution.json",t}return Object(m.a)(n,e),Object(i.a)(n,[{key:"comparePlaceFrequency",value:function(e,n){return e.places.length>n.places.length?-1:1}},{key:"compareSynonymFrequency",value:function(e,n){var t=[],a=[];t.concat(e.places.map(function(e){return e.synonyms})),a.concat(n.places.map(function(e){return e.synonyms}));var r=t.filter(function(e,n,t){return t.indexOf(e)===n}),o=a.filter(function(e,n,t){return t.indexOf(e)===n});return console.log(r),console.log(o),r.length>o.length?1:-1}},{key:"readJson",value:function(e){return fetch(e).then(function(e){if(!e.ok)throw new Error("HTTP error "+e.status);return e.json()}).catch(function(){throw new Error("File not available")})}},{key:"render",value:function(){return!0===this.state.loading?r.a.createElement("h2",null,"Loading..."):r.a.createElement(r.a.Fragment,null,r.a.createElement("header",null,r.a.createElement("h1",null,"Food language variety visualization")),r.a.createElement("main",null,r.a.createElement("aside",null,r.a.createElement(h,{foods:this.data.images,onClick:this.handleClick,selected:this.state.selectedFood})),r.a.createElement(b,{places:this.state.places})),r.a.createElement("footer",null,"Made with love by ",r.a.createElement("a",{href:"https://github.com/nmicht/"},"@nmicht")," and ",r.a.createElement("a",{href:"https://github.com/jbrew/"},"@jbrew")))}}]),n}(a.Component));Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));l.a.render(r.a.createElement(E,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}},[[19,1,2]]]);
//# sourceMappingURL=main.17b1bf75.chunk.js.map