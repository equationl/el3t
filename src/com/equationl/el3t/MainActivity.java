package com.equationl.el3t;

import android.app.*;
import android.app.AlertDialog.*;
import android.content.*;
import android.os.*;
import android.util.*;
import android.view.*;
import android.view.View.*;
import android.widget.*;
import com.equationl.ad.manager.*;
import java.io.*;
import java.lang.reflect.*;
import android.content.SharedPreferences.Editor;

import android.view.View.OnClickListener;


public class MainActivity extends Activity implements PointListen
{

	Button boot = null; 
	Button code = null;
	Button get = null;
	Button information = null;
	TextView wellcometext = null;
	Context context;
//	SharedPreferences sp=this.getSharedPreferences("sharePre", Context.MODE_PRIVAT


	@Override
    public void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
		
		this.context=this;
		JFQManager.init(context);
		JFQManager.setPointListen(this);

        boot = (Button)super.findViewById(R.id.boot);
		get = (Button)super.findViewById(R.id.get);
		code = (Button)super.findViewById(R.id.code);
		information = (Button)super.findViewById(R.id.information);
		wellcometext = (TextView)super.findViewById(R.id.wellcometext);
		
		//检测是否第一次启动，如果第一次启动则将积分调整为105
		SharedPreferences preferences = getSharedPreferences("isFirstUseAPP",MODE_WORLD_READABLE);
		boolean isFirstUse = preferences.getBoolean("isFirstUseAPP", true);
		if (isFirstUse) {
			//第一次使用
			boolean issuccess =JFQManager.updatePoint(105);
			if (issuccess) {
				wellcometext.setText("第一次使用，赠送105积分");
				Editor editor = preferences.edit();
				editor.putBoolean("isFirstUseAPP", false);
				editor.commit();
			}
		}
		

		
		boot.setOnClickListener(new OnClickListener() {
				public void onClick(View v){
					//启动程序
					SharedPreferences preferences = getSharedPreferences("isGetCode",MODE_WORLD_READABLE);
					boolean isGetCode = preferences.getBoolean("isGetCode", false);
					if (isGetCode) {
						Intent intent = new Intent();
						intent.setClass(MainActivity.this, ScriptActivity.class);
						startActivity(intent);
						MainActivity.this.finish();
					}
					int local_gold = JFQManager.selectPoint();
					if (local_gold < 100) {
						wellcometext.setText("积分不足！需要100，已有"+local_gold);
					}
					else {
						boolean issuccess = JFQManager.reducePoint(1);
						if (issuccess) {
							Intent intent = new Intent();
							intent.setClass(MainActivity.this, ScriptActivity.class);
							startActivity(intent);
							MainActivity.this.finish();
						}						
						else{
							wellcometext.setText("扣减积分失败！");
						}
					}
					
				}
			});
		get.setOnClickListener(new OnClickListener() {
				public void onClick(View v){
					//获取积分
					JFQManager.showXiaomaiOffer(context);
				}
			});
		code.setOnClickListener(new OnClickListener() {
				public void onClick(View v){
					//获取源码
					if (JFQManager.selectPoint() > 499) {
						boolean iscopy =  copyFileToSdCard("/sdcard/");
						if (iscopy) {
							boolean issuccess = JFQManager.reducePoint(500);
							if (issuccess) {
								SharedPreferences preferences = getSharedPreferences("isGetCode",MODE_WORLD_READABLE);
								Editor editor = preferences.edit();
								editor.putBoolean("isGetCode", true);
								editor.commit();
								wellcometext.setText("源码已导出至sdcard");
							}
							else {
								wellcometext.setText("积分扣减失败！");
							}
							
						}
						else {
							wellcometext.setText("导出错误！");
						}
					/**	SharedPreferences.Editor editor=sp.edit();
						editor.putString("clearad", "true");
						editor.commit();**/
					}
					else {
						int local_gold = JFQManager.selectPoint();
						wellcometext.setText("积分不足！需要500，已有" + local_gold);
					}
				}
			});
		information.setOnClickListener(new OnClickListener() {
				public void onClick(View v){
					//查看帮助
					final Builder builder = new AlertDialog.Builder(MainActivity.this);
					LayoutInflater myinflater = LayoutInflater.from(MainActivity.this);
					final View mydialogview = myinflater.inflate(R.layout.dialog_information, null);
					builder.setTitle("关于");
					builder.setView(mydialogview);//在这一步实现了和资源文件中的mylogindialog的关联
					builder.create().show();
				}
			});
			
			
   }
   
   	protected void onDestroy() {
		JFQManager.release();
		super.onDestroy();
	}
		
		@Override
		public boolean doActionAddPoint(int arg0) {
			Log.i("JFQ", "�����"+arg0+"���");
			return false;
		}

		@Override
		public boolean doActionReducePoint(int arg0) {
			Log.i("JFQ", "�����"+arg0+"���");
			return false;
		}

		@Override
		public boolean doActionUpdatePoint(int arg0) {
			Log.i("JFQ", "�����"+arg0+"���");
			return false;
		}
		
	private boolean copyFileToSdCard(String path) {
		Field[] raw = R.raw.class.getDeclaredFields();

		for(Field r : raw) {
			int id=getResources().getIdentifier(r.getName(), "raw", getPackageName());
			//Log.i(TAG, r.getName() + ": " + Integer.toHexString(id));
			String filename = path +  File.separator + r.getName().replace('_', ' ') + ".py";
			File file = new File(filename);

			if(file.exists()) continue;
			try {
				BufferedOutputStream outputStream = new BufferedOutputStream(new FileOutputStream(file));
				BufferedInputStream inputStream = new BufferedInputStream(getResources().openRawResource(id));
				byte[] buff = new byte[20*1024];
				int len;
				try {
					while((len = inputStream.read(buff)) > 0) {
						outputStream.write(buff, 0, len);
					}
					outputStream.flush();
					inputStream.close();
					outputStream.close();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
					return false;
				}

			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				return false;
			}
		}
		return true;
    }
		
	private long exitTime = 0;
	@Override
	public boolean onKeyDown(int keyCode, KeyEvent event) {
		if (keyCode == KeyEvent.KEYCODE_BACK
			&& event.getAction() == KeyEvent.ACTION_DOWN) {
			if ((System.currentTimeMillis() - exitTime) > 2000) {
				Toast.makeText(getApplicationContext(), "再按一次退出程序",
							   Toast.LENGTH_SHORT).show();
				exitTime = System.currentTimeMillis();
			} else {
				finish();
				System.exit(0);
			}
			return true;
		}
		return super.onKeyDown(keyCode, event);
	}
	
}
