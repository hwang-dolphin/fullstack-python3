(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{22:function(e,t,n){},42:function(e,t,n){"use strict";n.r(t);var c=n(2),a=n.n(c),i=n(12),s=n.n(i),r=n(13),o=n(14),d=n(17),h=n(16),j=(n(22),n(15)),l=n.n(j),u=n(1),b=function(e){Object(d.a)(n,e);var t=Object(h.a)(n);function n(e){var c;return Object(r.a)(this,n),(c=t.call(this,e)).state={message:"hi",loading:!0},c}return Object(o.a)(n,[{key:"componentDidMount",value:function(){var e=this;l.a.get("/api/name",{headers:{"x-api-key":"secretkey"}}).then((function(t){e.setState({message:t.data,loading:!1})})).catch((function(e){console.log(e)}))}},{key:"render",value:function(){return Object(u.jsx)("div",{children:this.state.loading?Object(u.jsx)("div",{children:"loading..."}):Object(u.jsx)(u.Fragment,{children:Object(u.jsx)("div",{children:Object(u.jsxs)("div",{children:[Object(u.jsx)("h1",{children:"Number Value"})," ",this.state.message]})})})})}}]),n}(a.a.Component);s.a.render(Object(u.jsx)(a.a.StrictMode,{children:Object(u.jsx)(b,{})}),document.getElementById("root"))}},[[42,1,2]]]);
//# sourceMappingURL=main.ee8585e3.chunk.js.map