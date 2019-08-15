(function(e){function t(t){for(var s,l,i=t[0],u=t[1],o=t[2],c=0,d=[];c<i.length;c++)l=i[c],r[l]&&d.push(r[l][0]),r[l]=0;for(s in u)Object.prototype.hasOwnProperty.call(u,s)&&(e[s]=u[s]);m&&m(t);while(d.length)d.shift()();return n.push.apply(n,o||[]),a()}function a(){for(var e,t=0;t<n.length;t++){for(var a=n[t],s=!0,i=1;i<a.length;i++){var u=a[i];0!==r[u]&&(s=!1)}s&&(n.splice(t--,1),e=l(l.s=a[0]))}return e}var s={},r={app:0},n=[];function l(t){if(s[t])return s[t].exports;var a=s[t]={i:t,l:!1,exports:{}};return e[t].call(a.exports,a,a.exports,l),a.l=!0,a.exports}l.m=e,l.c=s,l.d=function(e,t,a){l.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:a})},l.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},l.t=function(e,t){if(1&t&&(e=l(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var a=Object.create(null);if(l.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var s in e)l.d(a,s,function(t){return e[t]}.bind(null,s));return a},l.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return l.d(t,"a",t),t},l.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},l.p="/static/";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],u=i.push.bind(i);i.push=t,i=i.slice();for(var o=0;o<i.length;o++)t(i[o]);var m=u;n.push([0,"chunk-vendors"]),a()})({0:function(e,t,a){e.exports=a("56d7")},"56d7":function(e,t,a){"use strict";a.r(t);var s=a("2b0e"),r=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-app",[a("v-app-bar",{attrs:{app:""}},[a("v-toolbar-title",{staticClass:"headline text-uppercase"},[a("span",[e._v("Guessing")]),a("span",{staticClass:"font-weight-light"},[e._v("Game")])]),a("v-spacer")],1),a("v-content",[a("Game")],1)],1)},n=[],l=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-container",{staticClass:"grey lighten-5"},[a("v-layout",{attrs:{"text-center":"",wrap:""}},[a("v-flex",{attrs:{"mb-12":""}},[a("h1",{staticClass:"display-2 font-weight-bold mb-3"},[e._v("Welcome to the Guessing Game")]),a("p",{staticClass:"subheading font-weight-regular"},[e._v("To start a game please selected a boundary for guessing a number")])])],1),a("v-form",{ref:"formStart",on:{submit:function(e){e.preventDefault()}},model:{value:e.formStartValid,callback:function(t){e.formStartValid=t},expression:"formStartValid"}},[a("v-layout",{attrs:{row:"","align-center":"","justify-space-between":""}},[a("v-flex",{attrs:{md2:"",xs12:"","offset-md3":""}},[a("v-text-field",{attrs:{type:"number",label:"Minimum",rules:e.minimumRules,"error-messages":e.validMinMax(),min:"1",max:"50",required:""},model:{value:e.minimumValue,callback:function(t){e.minimumValue=t},expression:"minimumValue"}})],1),a("v-flex",{attrs:{md2:"",xs12:""}},[a("v-text-field",{attrs:{type:"number",label:"Maximum",rules:e.maximumRules,"error-messages":e.validMinMax(),min:"1",max:"50",id:"maximumId",required:""},model:{value:e.maximumValue,callback:function(t){e.maximumValue=t},expression:"maximumValue"}})],1),a("v-flex",{attrs:{md2:"",xs12:""}},[a("v-btn",{attrs:{type:"sumit",disabled:!e.formStartValid},on:{click:e.startGame}},[e._v("Start the Game")])],1),a("v-flex",{attrs:{md2:""}})],1)],1),e.start?a("div",[a("v-layout",{attrs:{"text-center":"",wrap:""}},[a("v-flex",{attrs:{"mb-12":""}},[a("p",[e._v(" ")])])],1),a("v-layout",{attrs:{"text-center":"",wrap:""}},[a("v-flex",{attrs:{"mb-12":""}},[a("p",{staticClass:"subheading font-weight-regular"},[e._v("Choose one of the options below to guess the number")])])],1),a("v-form",{ref:"formLess",on:{submit:function(e){e.preventDefault()}},model:{value:e.formLessValid,callback:function(t){e.formLessValid=t},expression:"formLessValid"}},[a("v-layout",{attrs:{row:"","align-center":"","justify-space-around":""}},[a("v-flex",{attrs:{md3:"",xs12:"","offset-md2":""}},[a("v-text-field",{attrs:{rules:e.lessRules,type:"number",label:"Less",required:""},model:{value:e.lessThanValue,callback:function(t){e.lessThanValue=t},expression:"lessThanValue"}})],1),a("v-flex",{attrs:{md3:"",xs12:""}},[a("v-btn",{attrs:{type:"submit",disabled:!e.formLessValid,color:"primary"},on:{click:e.isLessThan}},[e._v("Less than")])],1),a("v-flex",{attrs:{md1:"",xs12:""}})],1)],1),a("v-form",{ref:"formGreater",on:{submit:function(e){e.preventDefault()}},model:{value:e.formGreaterValid,callback:function(t){e.formGreaterValid=t},expression:"formGreaterValid"}},[a("v-layout",{attrs:{row:"","align-center":"","justify-space-around":""}},[a("v-flex",{attrs:{md3:"",xs12:"","offset-md2":""}},[a("v-text-field",{attrs:{rules:e.maximumRules,type:"number",label:"Greater",required:""},model:{value:e.greaterThanValue,callback:function(t){e.greaterThanValue=t},expression:"greaterThanValue"}})],1),a("v-flex",{attrs:{md3:"",xs12:""}},[a("v-btn",{attrs:{type:"submit",disabled:!e.formGreaterValid,color:"primary"},on:{click:e.isGreaterThan}},[e._v("Greater than")])],1),a("v-flex",{attrs:{md1:"",xs12:""}})],1)],1),a("v-layout",{attrs:{row:"","align-center":"","justify-space-around":""}},[a("v-flex",{attrs:{md12:""}},[a("p",[e._v(" ")])]),a("v-flex",{attrs:{md1:"",xs12:"","offset-md4":""}},[a("v-btn",{on:{click:e.isOdd}},[e._v("Is Odd?")])],1),a("v-flex",{attrs:{md1:"",xs12:""}},[a("v-btn",{on:{click:e.isEven}},[e._v("Is Even?")])],1),a("v-flex",{attrs:{md3:"",xs12:""}})],1),a("v-form",{ref:"formGuess",on:{submit:function(e){e.preventDefault()}},model:{value:e.formGuessValid,callback:function(t){e.formGuessValid=t},expression:"formGuessValid"}},[a("v-layout",{attrs:{row:"","align-center":"","justify-space-around":""}},[a("v-flex",{attrs:{md12:""}},[a("p",[e._v(" ")])]),a("v-flex",{attrs:{md1:"",xs12:"","offset-md4":""}},[a("v-text-field",{attrs:{rules:e.guessRules,type:"number",label:"Guess?",required:""},model:{value:e.guessValue,callback:function(t){e.guessValue=t},expression:"guessValue"}})],1),a("v-flex",{attrs:{md1:"",xs12:""}},[a("v-btn",{attrs:{type:"submit",disabled:!e.formGuessValid,color:"warning"},on:{click:e.guess}},[e._v("Guess it?")])],1),a("v-flex",{attrs:{md3:"",xs12:""}})],1)],1)],1):e._e(),a("v-layout",{attrs:{"text-center":"",wrap:""}},[a("v-flex",{attrs:{md12:""}},[a("p",[e._v(" ")])]),a("v-flex",{attrs:{"mb-12":""}},[a("h2",[e._v(e._s(e.message))])])],1),a("div",{staticClass:"text-center"},[a("v-dialog",{attrs:{width:"500"},model:{value:e.dialog,callback:function(t){e.dialog=t},expression:"dialog"}},[a("v-card",[a("v-card-title",{staticClass:"headline grey lighten-2",attrs:{"primary-title":""}},[e._v("Congratulations!!!")]),a("v-card-text",[a("br"),e._v("\n          You guessed the number: "+e._s(e.guessValue)+". Now you can play another game!\n        ")]),a("v-divider"),a("v-card-actions",[a("v-spacer"),a("v-btn",{attrs:{color:"primary",text:""},on:{keyup:function(t){if(!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter"))return null;e.dialog=!1},click:function(t){e.dialog=!1}}},[e._v("OK")])],1)],1)],1)],1)],1)},i=[],u={data:()=>({minimumValue:1,maximumValue:50,minimumRules:[e=>!!e||"Minimum is required"],maximumRules:[e=>!!e||"Maximum is required"],formStartValid:!0,start:!1,greaterThanValue:null,greaterRules:[e=>!!e||"Greater than value is required"],formGreaterValid:!0,lessThanValue:null,lessRules:[e=>!!e||"Less than value is required"],formLessValid:!0,guessValue:null,guessRules:[e=>!!e||"Guess value is required"],formGuessValid:!0,dialog:!1,message:""}),methods:{validMinMax:function(){return this.minimumValue<this.maximumValue?"":"Minimum must be inferior to Maximum"},startGame:function(){s["a"].axios.get(`/api/start/${this.minimumValue}/${this.maximumValue}`).then(e=>{null==e.data["success"]||0==e.data["success"]?this.message="Something wrong!":(this.start=!0,this.message=`Start: Guessing a number from ${this.minimumValue} to ${this.maximumValue}.`)}).catch(e=>{console.log(e)})},isEven:function(){s["a"].axios.get("/api/even").then(e=>{null==e.data["success"]||0==e.data["success"]?this.message="Something wrong!":this.message=`Is even? ${e.data["even"]}!`}).catch(e=>{console.log(e)})},isOdd:function(){s["a"].axios.get("/api/odd").then(e=>{null==e.data["success"]||0==e.data["success"]?this.message="Something wrong!":this.message=`Is odd? ${e.data["odd"]}!`}).catch(e=>{console.log(e)})},isLessThan:function(){s["a"].axios.get(`/api/less/${this.lessThanValue}`).then(e=>{null==e.data["success"]||0==e.data["success"]?this.message="Something wrong!":this.message=`Is less than ${this.lessThanValue}? ${e.data["less"]}!`}).catch(e=>{console.log(e)})},isGreaterThan:function(){s["a"].axios.get(`/api/greater/${this.greaterThanValue}`).then(e=>{null==e.data["success"]||0==e.data["success"]?this.message="Something wrong!":this.message=`Is greater than ${this.greaterThanValue}? ${e.data["greater"]}!`}).catch(e=>{console.log(e)})},guess:function(){s["a"].axios.get(`/api/guess/${this.guessValue}`).then(e=>{null==e.data["success"]||0==e.data["success"]?this.message="Something wrong!":e.data["guess"]?(this.dialog=!0,this.start=!1,this.message=""):this.message="You did not guess it :("}).catch(e=>{console.log(e)})}}},o=u,m=a("2877"),c=a("6544"),d=a.n(c),f=a("8336"),v=a("b0af"),p=a("99d9"),g=a("a523"),h=a("169a"),x=a("ce7e"),b=a("0e8f"),V=a("4bd4"),y=a("a722"),w=a("2fa4"),_=a("8654"),G=Object(m["a"])(o,l,i,!1,null,null,null),k=G.exports;d()(G,{VBtn:f["a"],VCard:v["a"],VCardActions:p["a"],VCardText:p["b"],VCardTitle:p["c"],VContainer:g["a"],VDialog:h["a"],VDivider:x["a"],VFlex:b["a"],VForm:V["a"],VLayout:y["a"],VSpacer:w["a"],VTextField:_["a"]});var T={name:"App",components:{Game:k},data:()=>({})},S=T,C=a("7496"),M=a("40dc"),O=a("a75b"),$=a("2a7f"),j=Object(m["a"])(S,r,n,!1,null,null,null),L=j.exports;d()(j,{VApp:C["a"],VAppBar:M["a"],VContent:O["a"],VSpacer:w["a"],VToolbarTitle:$["a"]});var q=a("f309");s["a"].use(q["a"]);var R=new q["a"]({icons:{iconfont:"mdi"}}),I=a("bc3a"),D=a.n(I),E=a("a7fe"),P=a.n(E);s["a"].config.productionTip=!1,s["a"].use(P.a,D.a),new s["a"]({vuetify:R,render:e=>e(L)}).$mount("#app")}});
//# sourceMappingURL=app.5d748cac.js.map