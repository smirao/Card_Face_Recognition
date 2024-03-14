import face_alignment, datetime, torch, sys
from deepface import DeepFace

class faceIdIdentifier:
    def __init__(self, face_path, identification_path):
        self.time_start = datetime.datetime.now()
        self.face = face_path
        self.identification = identification_path
        self.backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']

    def compare(self) -> bool:
        result = DeepFace.verify(img1_path = self.face, img2_path = self.identification, detector_backend=self.backends[1])
        return result["verified"]
    
    def detect_blurry(self, image):
        fa = None
        if sys.platform == "darwin" or sys.platform == "linux":
            fa = face_alignment.FaceAlignment(face_alignment.LandmarksType.TWO_D, device='cpu', flip_input=False)
        else:
            fa = face_alignment.FaceAlignment(face_alignment.LandmarksType.TWO_D, dtype=torch.bfloat16, device='cuda', flip_input=False)
        landmarks = fa.get_landmarks_from_image(image)

        return landmarks is None
        
    def evaluate(self, BYPASS_CHECK = False) -> bool:
        face, id = False, False
        
        if not BYPASS_CHECK:
            ts1 = datetime.datetime.now()-self.time_start
            print(f"({round(ts1.total_seconds(),2)}s) Working on face...")
            face = self.detect_blurry(self.face)
            ts2 = datetime.datetime.now()-self.time_start
            print(f"({round(ts2.total_seconds(),2)}s) Working on ID...")
            id = self.detect_blurry(self.identification)

        if (face and id):
            print("Both images are too blurry.")
            return False
        elif (face):
            print("Face image is too blurry.")
            return False
        elif (id):
            print("ID image is too blurry.")
            return False
        else:
            ts3 = datetime.datetime.now()-self.time_start
            print(f"({round(ts3.total_seconds(),2)}s) Comparing...")
            compared = self.compare()
            string = "" if compared else "don't "
            ts4 = datetime.datetime.now()-self.time_start
            print(f"({round(ts4.total_seconds(),2)}s) The Face and ID {string}match.")
            return compared  

if __name__ == "__main__":
    identifier = faceIdIdentifier("current/mr_bean.jpg", "current/mr_bean_id.jpg")
    identifier.evaluate()
    
    print("\n\nNumber 2.")
    identifier = faceIdIdentifier("current/pee_wee.jpg", "current/mr_bean_id.jpg")
    identifier.evaluate()