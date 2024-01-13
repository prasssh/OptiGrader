import 'package:flutter/material.dart';
import 'package:camera/camera.dart';

class CameraScreen extends StatefulWidget {
  const CameraScreen({Key? key}) : super(key: key);

  @override
  _CameraScreenState createState() => _CameraScreenState();
}

class _CameraScreenState extends State<CameraScreen> {
  late CameraController _controller;
  late Future<void> _initializeControllerFuture;

  @override
  void initState() {
    super.initState();

    // Get the list of available cameras.
    availableCameras().then((cameras) {
      if (cameras.isEmpty) {
        // No cameras are available
        return;
      }

      // Use the first camera from the list
      _controller = CameraController(
        cameras[0],
        ResolutionPreset.medium,
      );

      // Initialize the controller
      _initializeControllerFuture = _controller.initialize().then((_) {
        if (mounted) {
          setState(() {}); // Ensure the widget is marked as 'mounted'
        }
      }).catchError((error) {
        // Handle initialization errors
        print('Error initializing camera: $error');
      });
    });
  }

  @override
  void dispose() {
    // Dispose of the controller when the widget is disposed.
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Camera Screen'),
      ),
      body: FutureBuilder<void>(
        future: _initializeControllerFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.done) {
            // If the Future is complete, display the preview.
            return CameraPreview(_controller);
          } else if (snapshot.hasError) {
            // If an error occurs during initialization, display an error message.
            return Center(
              child: Text(
                'Error: ${snapshot.error}',
                style: TextStyle(color: Colors.red),
              ),
            );
          } else {
            // Otherwise, display a loading indicator.
            return Center(child: CircularProgressIndicator());
          }
        },
      ),
    );
  }
}
