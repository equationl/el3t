import android
#coding=utf-8
droid = android.Android()

#..............
#layoutdata.py.
#EL3T布局数据...
#author:equationl(独孤方程)
#..............

XML_GAME = '''<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
	xmlns:android="http://schemas.android.com/apk/res/android"
	android:layout_width="fill_parent"
	android:layout_height="fill_parent"
	android:orientation="vertical"
	android:background="file:///sdcard/equationl/EL3T/data/image/game_chessboard.jpg" >

	<TextView
		android:layout_width="fill_parent"
		android:layout_height="wrap_content"
		android:text="EL3T"
		android:textColor="#ff0000"
		android:textSize="18sp"
		android:gravity="center"
		android:id="@+id/toptext"/>

	<TableLayout
		android:layout_width="fill_parent"
		android:layout_height="wrap_content">

		<TextView
			android:layout_width="156dp"
			android:layout_height="2dp"
			android:background="#000000"/>

		<TableRow
			android:layout_width="fill_parent"
			android:layout_height="wrap_content">

			<TextView
				android:layout_width="2dp"
				android:layout_height="50dip"
				android:background="#000000"/>

			<ImageButton
				android:layout_height="50dp"
				style="?android:attr/buttonBarButtonStyle"
				android:layout_width="50dp"
				android:background="file:///sdcard/equationl/EL3T/data/image/game_chessboard_1.jpg"
				android:id="@+id/btn_303" />

			<TextView
				android:layout_width="2dp"
				android:layout_height="50dip"
				android:background="#000000"/>

			<ImageButton
				android:layout_height="50dp"
				style="?android:attr/buttonBarButtonStyle"
				android:layout_width="50dp"
				android:background="file:///sdcard/equationl/EL3T/data/image/game_chessboard_1.jpg"
				android:id="@+id/btn_203" />

			<TextView
				android:layout_width="2dp"
				android:layout_height="50dip"
				android:background="#000000"/>

			<ImageButton
				android:layout_height="50dp"
				style="?android:attr/buttonBarButtonStyle"
				android:layout_width="50dp"
				android:background="file:///sdcard/equationl/EL3T/data/image/game_chessboard_1.jpg"
			 android:id="@+id/btn_103" />

			<TextView
				android:layout_width="2dp"
				android:layout_height="50dip"
				android:background="#000000"/>

		</TableRow>

		<TextView
			android:layout_width="156dp"
			android:layout_height="2dp"
			android:background="#000000"/>

		<TableRow
			android:layout_width="fill_parent"
			android:layout_height="wrap_content">

			<TextView
				android:layout_width="2dp"
				android:layout_height="50dip"
				android:background="#000000"/>

			<ImageButton
				android:layout_height="50dp"
				style="?android:attr/buttonBarButtonStyle"
				android:layout_width="50dp"
				android:background="file:///sdcard/equationl/EL3T/data/image/game_chessboard_1.jpg"
				 android:id="@+id/btn_302" />

			<TextView
				android:layout_width="2dp"
				android:layout_height="50dip"
				android:background="#000000"/>

			<ImageButton
				android:layout_height="50dp"
				style="?android:attr/buttonBarButtonStyle"
				android:layout_width="50dp"
				android:background="file:///sdcard/equationl/EL3T/data/image/game_chessboard_1.jpg"
				 android:id="@+id/btn_202" />

			<TextView
				android:layout_width="2dp"
				android:layout_height="50dip"
				android:background="#000000"/>

			<ImageButton
				android:layout_height="50dp"
				style="?android:attr/buttonBarButtonStyle"
				android:layout_width="50dp"
				android:background="file:///sdcard/equationl/EL3T/data/image/game_chessboard_1.jpg"
				 android:id="@+id/btn_102" />

			<TextView
				android:layout_width="2dp"
				android:layout_height="50dip"
				android:background="#000000"/>

		</TableRow>

		<TextView
			android:layout_width="156dp"
			android:layout_height="2dp"
			android:background="#000000"/>

		<TableRow
			android:layout_width="fill_parent"
			android:layout_height="wrap_content">

			<TextView
				android:layout_width="2dp"
				android:layout_height="50dip"
				android:background="#000000"/>

			<ImageButton
				android:layout_height="50dp"
				style="?android:attr/buttonBarButtonStyle"
				android:layout_width="50dp"
				android:background="file:///sdcard/equationl/EL3T/data/image/game_chessboard_1.jpg"
				 android:id="@+id/btn_301" />

			<TextView
				android:layout_width="2dp"
				android:layout_height="50dip"
				android:background="#000000"/>

			<ImageButton
				android:layout_height="50dp"
				style="?android:attr/buttonBarButtonStyle"
				android:layout_width="50dp"
				android:background="file:///sdcard/equationl/EL3T/data/image/game_chessboard_1.jpg"
				 android:id="@+id/btn_201" />

			<TextView
				android:layout_width="2dp"
				android:layout_height="50dip"
				android:background="#000000"/>

			<ImageButton
				android:layout_height="50dp"
				style="?android:attr/buttonBarButtonStyle"
				android:layout_width="50dp"
				android:background="file:///sdcard/equationl/EL3T/data/image/game_chessboard_1.jpg"
				 android:id="@+id/btn_101" />

			<TextView
				android:layout_width="2dp"
				android:layout_height="50dip"
				android:background="#000000"/>

		</TableRow>

		<TextView
			android:layout_width="156dp"
			android:layout_height="2dp"
			android:background="#000000"/>

	</TableLayout>
	
	 		<ListView
			android:layout_height="wrap_content"
			android:layout_width="wrap_content"
			android:id="@+id/list"/>

</LinearLayout>
'''