# REGISTRATIONPAGE

import 'package:cloud_firestore/cloud_firestore.dart';import'package:edu_gov_schemes/common/widget.dart';import'package:edu_gov_schemes/utils/util.dart';
import'package:firebase_auth/firebase_auth.dart';import'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';classSignUpScreenextendsConsumerStatefulWidget{constSignUpScreen({super.key});
staticconstrouteName='/signup-screen';@override
ConsumerState<SignUpScreen>createState()=>
_SignUpScreenState();

}



class_SignUpScreenStateextends


ConsumerState<SignUpScreen>{

TextEditingControllernameController=TextEditingController();
TextEditingController emailController =TextEditingController();
TextEditingController passwordController =TextEditingController();
finalformKey=GlobalKey<FormState>();boolloader=false;
saveUserData(

{

requiredStringname,requiredStringemail,
requiredStringuserid})async{

varuserData=UserModel(name:name,email:email,userid)
awaitFirebaseFirestore.instance.collection('users')

.doc(userid)set(userData.toMap());


}

voidsignUpWithEmail()async{setState((){
loader=true;print(loader);
});

//ref.read(signupControllerProvider).signupWithEmail(

//	context:context,

//	userName:nameController.text,

//	email:emailController.text,

//	password: passwordController.text);try {
UserCredentialcredential=

awaitFirebaseAuth.instance.createUserWithEmailAndPassword(
email: emailController.text.trim(),password:passwordController.text.trim(),


);

awaitFirebaseAuth.instance.currentUser!

.updateDisplayName(nameController.text.trim());awaitFirebaseAuth.instance.currentUser!

.verifyBeforeUpdateEmail(emailController.text.trim());awaitsaveUserData(
name: nameController.text.trim(),email: emailController.text.trim(),userid:credential.user!.uid);
if(context.mounted){setState((){
loader = false;print(loader);nameController.clear();emailController.clear();passwordController.clear();
});


showSnackBar(context:context,text:"RegistrationSuccessful");
}

}onFirebaseAuthExceptioncatch(e){if(e.code=='weak-password'){
if(context.mounted){setState((){
loader=false;print(loader);
});

showSnackBar(

context:context,text:"Thepasswordprovidedistooweak.");
}

}elseif(e.code=='email-already-in-use'){if(context.mounted){
setState(() {loader=false;


print(loader);

});

showSnackBar(context:context,
text:"Theaccountalreadyexistsforthatemail.");

}

}

}catch(e){

if(context.mounted){

showSnackBar(context:context,text:e.toString());

}

}

//Future.delayed(constDuration(seconds:2),(){

//});

}



@override

Widgetbuild(BuildContextcontext){


return Scaffold(body: Form(key: formKey,child: Center(child: Card(elevation:5.1,
color: Colors.white,child: SizedBox(height:500,
width: 480,child:Padding(
padding: const EdgeInsets.symmetric(horizontal:20),child:Column(
crossAxisAlignment: CrossAxisAlignment.start,children:[constPadding(
padding:EdgeInsets.only(top:20),

child:HeadingText(text:"Register"),

),


constSizedBox(height:35,
),

ReUsableTextFormField(controller:nameController,
labelText: "Enter your name",validatorText:"Pleaseenteryourname",
),

constSizedBox(height:30,
),

ReUsableTextFormField(controller: emailController,labelText:"EnteryourEmail",
validatorText:"Pleaseenteryouremail",

),
constSizedBox(height:30,


),

ReUsableTextFormField(controller: passwordController,labelText:"EnteryourPassword",
validatorText:"Pleaseenteryourpassword",

),

constSizedBox(height:35,
),

Align(

alignment: Alignment.center,child:SizedBox(
width:double.infinity,

child:ReUsableElevatedButton(

//buttonText:"SignUp",child:loader==false
?constText(

"Register",


style: TextStyle(color:Colors.white,
fontWeight:FontWeight.bold),

)

: const CircularProgressIndicator(),onPressed:(){
if (formKey.currentState!.validate()) {signUpWithEmail();
}}),),),

constSizedBox(height:10,
),

Row(

mainAxisAlignment: MainAxisAlignment.end,children:[
const ParagraphText(text: "Already have an account?"),TextButton(
onPressed:(){


Navigator.pushNamed(

context,SignInScreen.routeName);

},

child:constText("Login",
style:TextStyle(

color: Color(0xff06737f),fontWeight:FontWeight.bold),
),],)],),),),)

[5:14 PM, 7/8/2025] Swetha🖤: LOGININPAGE

Import'package:edu_gov_schemes/auth/sign_up/screen/screen.dart';
import'package:edu_gov_schemes/common/widget.dart';

import'package:edu_gov_schemes/home/screen/home_screen.dart';
import 'package:edu_gov_schemes/utils/util.dart';import'package:firebase_auth/firebase_auth.dart';


import'package:flutter/material.dart';



classSignInScreenextendsStatefulWidget{constSignInScreen({super.key});
staticconstrouteName='/signin-screen';



@override

State<SignInScreen>createState()=>
_SignInScreenState();

}

class_SignInScreenStateextendsState<SignInScreen>{

TextEditingController emailController =TextEditingController();
TextEditingController passwordController =TextEditingController();



String? userName;boolloader=false;
voidsignInWithEmail()async{


try {setState(() {loader=true;print(loader);
});

final credential = awaitFirebaseAuth.instance.signInWithEmailAndPassword(
email: emailController.text.trim(),password: passwordController.text.trim());userName = credential.user!.displayName;setState((){
loader=false;print(loader);
});

Navigator.pushNamed(context, HomeScreen.routeName,arguments:userName);
}onFirebaseAuthExceptioncatch(e){if(e.code=='user-not-found'){


setState(() {loader=false;print(loader);
});

showSnackBar(context:context,text:"Nouserfoundforthatemail.");
//print('Nouserfoundforthatemail.');

}elseif(e.code=='wrong-password'){setState((){
loader=false;print(loader);
});

showSnackBar(

context:context,text:"Wrongpasswordprovidedforthatuser.");
//print('Wrongpasswordprovidedforthatuser.');

} else {setState((){


loader=false;print(loader);
showSnackBar(context:context,text:"Pleaseentercorrectinput");
});

}

}

}



@override

Widgetbuild(BuildContextcontext){returnScaffold(
body:Center(child: Card(elevation: 5.1,color: Colors.white,child: SizedBox(height:500,


width: 480,child:Padding(
padding:constEdgeInsets.symmetric(horizontal:20),child:Column(
crossAxisAlignment: CrossAxisAlignment.start,children:[
constPadding(

padding: EdgeInsets.only(top: 60),child:Align(
alignment:Alignment.center,child:HeadingText(text:"Login")),
),

constSizedBox(height:50,
),
ReUsableTextFormField(controller: emailController,labelText:"EnteryourEmail",


validatorText:"Pleaseenteryouremail",

),

constSizedBox(height:30,
),

ReUsableTextFormField(controller: passwordController,labelText:"EnteryourPassword",
validatorText:"Pleaseenteryourpassword",

),

constSizedBox(height:35,
),

Align(

alignment: Alignment.center,child:SizedBox(
width:double.infinity,

child:ReUsableElevatedButton(


//buttonText:"SignIn",child:loader==false
?constText("Login",
style: TextStyle(color:Colors.white,
fontWeight:FontWeight.bold),

)

: const CircularProgressIndicator(),onPressed: (){
signInWithEmail();

},

),

),

),

constSizedBox(height:20,
),


Row(

mainAxisAlignment: MainAxisAlignment.center,children:[
constParagraphText(text:"Don'thaveanaccount?"),TextButton(
onPressed:(){

Navigator.pushNamed(context,SignUpScreen.routeName);
},

child:constText("Register",
style:TextStyle(

color: Color(0xff06737f),fontWeight:FontWeight.bold),
),

)

],

)],),),),),),);}}
[5:16 PM, 7/8/2025] Swetha🖤: ALLOPTIONS

Import'package:edu_gov_schemes/chat_bot/screen/eligible
_check_chatbot_screen.dart';

import'package:edu_gov_schemes/common/egs_scaffold.dart';
import'package:edu_gov_schemes/common/widget.dart';

import'package:edu_gov_schemes/local_database/all_schemes_data.dart';
import'package:flutter/material.dart';

import'package:flutter_linkify/flutter_linkify.dart';import'package:url_launcher/url_launcher.dart';


classAllSChemesScreenextendsStatefulWidget{

constAllSChemesScreen({super.key,requiredthis.userName});
staticconstrouteName='/all-schemes-screen';finalStringuserName;
@override

State<AllSChemesScreen>createState()=>


_AllSChemesScreenState();

}

class_AllSChemesScreenStateextendsState<AllSChemesScreen>{
final GlobalKey<ScaffoldState> scaffoldKey =Future<void>onOpen(LinkableElementlink)async{if(!awaitlaunchUrl(Uri.parse(link.url))){
throwException('Couldnotlaunch${link.url}');

}

}



String_selectedCategory='Allschemes';

Map<String,List<Map<String,dynamic>>>data=allCategorySchemes;



List<Map<String, dynamic>> allSchemeData = [];List<Map<String,dynamic>>searchSchemeData=[];
//List<Map<String,dynamic>>


getFilteredData() {print(_selectedCategory);
if(_selectedCategory=='Allschemes'){

allSchemeData = data.values.expand((items) =>items).toList();
//returndata.values.expand((items)=>items).toList();

}else{

allSchemeData=data[_selectedCategory]!;

//returndata[_selectedCategory]??[];

}

}



//Map<String, List<String>> checkeligbleQuestion =checkEligbleQuestions;
ListcheckElibleQuestionSend=[];StringkeyName="";


finalsearchController=TextEditingController();





voidsearchMethod(Stringdata){

List<Map<String,dynamic>>suggestions=allSchemeData.where((element){
final schemeName =element["schemeName"].toString().toLowerCase();
finalinput=data.trim().toLowerCase();

//print(schemeName.contains(input).);returnschemeName.contains(input);
}).toList();



setState((){

searchSchemeData=suggestions;

});

if (searchController.text.isEmpty) {searchSchemeData=[];
}

}


@override

void initState() {getFilteredData();super.initState();
}



@override

Widgetbuild(BuildContextcontext){returnEGSSaffold(
userName: widget.userName,scaffoldKey:scaffoldKey,
endDrawer:ELigibleCheckChatBot(

keyName:keyName,questions:checkElibleQuestionSend),
floatButton:Container(),

//FloatingActionButton(

//	backgroundColor:Colors.white,

//	onPressed:(){


//	//scaffoldKey.currentState!.openEndDrawer();

//	},

//	child:constIcon(

//	Icons.chat_bubble,

//	color:Color(0xff06737f),

//	),

//),

text: Text(widget.userName,
style: const TextStyle(fontWeight:FontWeight.bold),
),

body:Container(

color: Color(0xffe8f3ff),child:Column(children:[
Padding(padding:


constEdgeInsets.symmetric(horizontal:20,vertical:20),child:TextField(
controller: searchController,decoration:InputDecoration(
prefixIcon: Icon(Icons.search),filled:true,
fillColor: Colors.white,hintText:"EnterSchemename",border:OutlineInputBorder(
borderRadius: BorderRadius.circular(20),borderSide:BorderSide(color:Colors.blue))),
onChanged:searchMethod,

),

),
Row(mainAxisAlignment:
MainAxisAlignment.spaceBetween,children:[


Padding(

padding:constEdgeInsets.only(left:10),child:Text(
"EducationGovernmentSchemes",style:
TextStyle(fontWeight:FontWeight.bold,
fontSize:20),

),

),

DropdownButton<String>(value:_selectedCategory,
items:['Allschemes',...data.keys].map((String
category){

return DropdownMenuItem<String>(value:category,
child:Text(category),

);

}).toList(),


onChanged:(String?newValue){setState((){
_selectedCategory=newValue!;getFilteredData();
});

},

),

],

),

Expanded(

child:searchSchemeData.isNotEmpty

?ListView.builder(

itemCount: searchSchemeData.length,itemBuilder:(context,index){
finalallScheme=searchSchemeData[index];



returnCard(

//color:Color(0xfff4fbff),


color: Colors.white,child:Theme(
data: Theme.of(context)copyWith(dividerColor:Colors.transparent),child:ExpansionTile(
expandedCrossAxisAlignment:CrossAxisAlignment.start,title: Text(allScheme["schemeName"]!,
style:TextStyle(fontWeight:FontWeight.bold),

),

subtitle: Align( alignment: Alignment.centerLeft,child: InkWell(onTap: () {checkElibleQuestionSend.clear();
//StringkeyName=allScheme["schemeName"];
var data = allScheme["checkEligbleQuestions"];checkElibleQuestionSend.addAll(data!);


scaffoldKey.currentState!

.openEndDrawer();

},

child:Text("Checkeligibility",style:
TextStyle(color:Color(0xff4c3885)

//color:Color(0xff06737f)

),

)),

),

children:[ListTile(
title:Text("SchemeDetails",style:TextStyle(
fontWeight:FontWeight.bold)),

),

ListTile(

leading:Text("eligibility"),


title:Text(allScheme["eligibility"]!),

),

ListTile(

leading:Text("benificiaries"),

title:Text(allScheme["benificiaries"]!),

),

ListTile( leading: Text("implementationStatus"),title:Text(allScheme["implementationStatus"]!),
),

ListTile(

leading: Text("sourceLink"),title:Linkify(
onOpen:onOpen,text:
allScheme['sourceLink'].toString()),

),

],

),),);})


:ListView.builder(

itemCount: allSchemeData.length,itemBuilder:(context,index){
finalallScheme=allSchemeData[index];returnCard(
//color: Color(0xfff4fbff),color:Colors.white,child:Theme(
data:Theme.of(context)

.copyWith(dividerColor: Colors.transparent),child: ExpansionTile(expandedCrossAxisAlignment:CrossAxisAlignment.start,
title: Text(allScheme["schemeName"]!,
style:TextStyle(fontWeight:FontWeight.bold),

),

subtitle:Align(


alignment: Alignment.centerLeft,child:InkWell(
onTap: () {checkElibleQuestionSend.clear();
//StringkeyName=allScheme["schemeName"];var data =allScheme["checkEligbleQuestions"checkElibleQuestionSend.addAll(data!);scaffoldKey.currentState!openEndDrawer();
},

child: Text("Check eligibility",style:
TextStyle(color:Color(0xff4c3885)

//color:Color(0xff06737f)

),

)),

),

children:[


ListTile(

title:Text("SchemeDetails",style:TextStyle(
fontWeight:FontWeight.bold)),

),

ListTile(

leading:Text("eligibility"),

title:Text(allScheme["eligibility"]!),

),

ListTile(

leading:Text("benificiaries"),

title: Text(allScheme["benificiaries"]!), ),ListTile( leading: Text("implementationStatus"),title:Text(allScheme["implementationStatus"]!),
),

ListTile(
leading: Text("sourceLink"),title:Linkify(


onOpen:onOpen,

text:	),],),),);}),),],),));

}}



MAIN.DART

import'package:edu_gov_schemes/auth/sign_in/screen/sign_inscreen.dart';
import'package:edu_gov_schemes/all_schemes/screen/all_schemes.dart';
import'package:edu_gov_schemes/chat_bot/forLearn.dart';
import'package:edu_gov_schemes/chat_bot/screen/egs_chatbot.dart';
import'package:edu_gov_schemes/home/screen/home_screen.dart';
import'package:edu_gov_schemes/route.dart';

import'package:edu_gov_schemes/scheme_chatbot/screens
/scheme_chatbot_screen.dart';

import'package:firebase_auth/firebase_auth.dart';


import'package:firebase_core/firebase_core.dart';import'package:flutter/material.dart';
import'package:flutter_riverpod/flutter_riverpod.dart';void main() async {WidgetsFlutterBinding.ensureInitialized();
awaitFirebase.initializeApp(
options:constFirebaseOptions(apiKey:
"AIzaSyAuEkizj9SNoTH_MXGsOjWm71wYAobjprojectId: "edu-gov-schemes",messagingSenderId:"717043768713",
appId:"1:717043768713:web:63571d26647e18e5655558",
));

runApp(const ProviderScope(child: MyApp()));}classMyAppextendsStatelessWidget{
const MyApp({super.key});@override


Widgetbuild(BuildContextcontext){returnMaterialApp(
title: 'Flutter Demo',debugShowCheckedModeBanner: false,theme:ThemeData(
colorScheme: ColorScheme.fromSeed(seedColor:Colors.deepPurple),
useMaterial3:true,

),

onGenerateRoute:(settings)=>generateRoute(settings),
home:StreamBuilder(

stream:FirebaseAuth.instance.authStateChanges(),builder:(context,snapshot){
if(snapshot.hasData){

String userName = snapshot.data!.displayName!;returnHomeScreen(userName:userName);}),);}
