import 'package:flutter/material.dart';
import 'camera.dart'; // Import the CameraScreen

class Dashboard extends StatelessWidget {
  var height, width;

  List imgData = [
    "assets/image/mcqs.png",
    "assets/image/quiz.png",
    "assets/image/pdf.png",
    "assets/image/about.png",
  ];
  List titles = ["MCQS", "QUIZ", "PDF", "ABOUT"];

  Dashboard({super.key});
  @override
  Widget build(BuildContext context) {
    height = MediaQuery.of(context).size.height;
    width = MediaQuery.of(context).size.width;
    return Scaffold(
      body: SingleChildScrollView(
        child: Container(
          color: Colors.indigo,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                decoration: BoxDecoration(),
                height: height * 0.35,
                width: width,
                child: Column(
                  children: [
                    Padding(
                      padding: EdgeInsets.only(
                        top: 35,
                        left: 20,
                        right: 20,
                      ),
                      child: Row(
                        children: [
                          InkWell(
                            onTap: () {},
                            child: Icon(
                              Icons.sort,
                              color: Colors.white,
                              size: 40,
                            ),
                          ),
                          Container(
                            height: 50,
                            width: 50,
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(15),
                              color: Colors.white,
                              image: DecorationImage(
                                image: AssetImage(
                                  "image/woman.png",
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                    Padding(
                      padding: EdgeInsets.only(
                        top: 20,
                        left: 30,
                      ),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            "Dashboard",
                            style: TextStyle(
                              fontSize: 30,
                              color: Colors.white,
                              fontWeight: FontWeight.w500,
                              letterSpacing: 1,
                            ),
                          ),
                          SizedBox(height: 10),
                          Text(
                            "Last Update: 12 Jan 2024",
                            style: TextStyle(
                              fontSize: 16,
                              color: Colors.white54,
                              letterSpacing: 1,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
              Container(
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.only(
                    topLeft: Radius.circular(30),
                    topRight: Radius.circular(30),
                  ),
                ),
                height: height * 0.75,
                width: width,
                child: GridView.builder(
                  gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 2,
                    childAspectRatio: 1.1,
                    mainAxisSpacing: 25,
                  ),
                  shrinkWrap: true,
                  physics: NeverScrollableScrollPhysics(),
                  itemCount: imgData.length,
                  itemBuilder: (context, index) {
                    return InkWell(
                      onTap: () {},
                      child: Container(
                        margin:
                            EdgeInsets.symmetric(vertical: 8, horizontal: 20),
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(20),
                          color: Colors.white,
                          boxShadow: [
                            BoxShadow(
                              color: Colors.black26,
                              spreadRadius: 1,
                              blurRadius: 6,
                            ),
                          ],
                        ),
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                          children: [
                            Image.asset(
                              imgData[index],
                              width: 100,
                            ),
                          ],
                        ),
                      ),
                    );
                  },
                ),
              ),
              // Add Scanner Button
              Container(
                width: double.infinity,
                height: 70, // Increased footer size
                color: Colors.indigo,
                child: TextButton(
                  onPressed: () {
                    // Navigate to the Camera Screen (Scanner)
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => CameraScreen(),
                      ),
                    );
                  },
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Image.asset(
                        "assets/image/camera.png", // Add scan.png
                        height: 30,
                        width: 30,
                      ),
                      SizedBox(width: 10),
                      Text(
                        'Scanner',
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 18,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
