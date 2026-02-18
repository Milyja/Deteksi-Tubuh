import cv2
import mediapipe as mp
mpose = mp.solutions.pose
pose = mpose.Pose()
mdraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    succes, img = cap.read()
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hasil = pose.process(imgrgb)

    if hasil.pose_landmarks:
        mdraw.draw_landmarks(img, hasil.pose_landmarks, mpose.POSE_CONNECTIONS)

        Im = hasil.pose_landmarks.landmark

        bahu_kiri= Im[11]
        tangan_kiri = Im[15]

        bahu_kanan = Im[12]
        tangan_kanan = Im[16]

        if tangan_kiri.y < bahu_kiri.y:
            cv2.putText(img,"Tangan Kiri Terangkat", (50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,240),4)

        if tangan_kanan.y < bahu_kanan.y:
            cv2.putText(img,"Tangan Kanan Terangkat", (50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,200),4)


    cv2.imshow("Deteksi Tangan Terangkat", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
