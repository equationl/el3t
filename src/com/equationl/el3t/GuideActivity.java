package com.equationl.el3t;

import java.util.ArrayList;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.support.v4.view.ViewPager;
import android.support.v4.view.ViewPager.OnPageChangeListener;
import android.view.LayoutInflater;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;

/**
 * @author yangyu
 *	�������������activity��
 */
public class GuideActivity extends Activity implements OnPageChangeListener{
	// ����ViewPager����
	private ViewPager viewPager;

	// ����ViewPager������
	private ViewPagerAdapter vpAdapter;

	// ����һ��ArrayList����View
	private ArrayList<View> views;

	// ���������View����
	private View view1, view2, view3, view4;
	
	//���忪ʼ��ť����
	private Button startBt;
		
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_guide);
		
		initView();
		
		initData();
	}

	/**
	 * ��ʼ�����
	 */
	private void initView() {
		//ʵ�������Ĳ��ֶ��� 
		LayoutInflater mLi = LayoutInflater.from(this);
		view1 = mLi.inflate(R.layout.guide_view01, null);
		view2 = mLi.inflate(R.layout.guide_view02, null);
		view3 = mLi.inflate(R.layout.guide_view03, null);
		view4 = mLi.inflate(R.layout.guide_view04, null);
	
		// ʵ��ViewPager
		viewPager = (ViewPager) findViewById(R.id.viewpager);

		// ʵ��ArrayList����
		views = new ArrayList<View>();

		// ʵ��ViewPager������
		vpAdapter = new ViewPagerAdapter(views);
		
		//ʵ��ʼ��ť
		startBt = (Button) view4.findViewById(R.id.startBtn);
	}

	/**
	 * ��ʼ�����
	 */
	private void initData() {
		// ���ü���
		viewPager.setOnPageChangeListener(this);
		// �������������
		viewPager.setAdapter(vpAdapter);

		//��Ҫ��ҳ��ʾ��Viewװ��������		
		views.add(view1);
		views.add(view2);
		views.add(view3);
		views.add(view4);		
								
		// ��ʼ��ť���ü���
		startBt.setOnClickListener(new OnClickListener() {
			@Override
			public void onClick(View v) {
				 startbutton();
			}
		});
	}

	@Override
	public void onPageScrollStateChanged(int arg0) {
			
	}

	@Override
	public void onPageScrolled(int arg0, float arg1, int arg2) {
		
	}

	@Override
	public void onPageSelected(int arg0) {
		
	}
	
	/**
	 * ��Ӧ��ť����¼�
	 */
	private void startbutton() {  
      	Intent intent = new Intent();
		intent.setClass(GuideActivity.this,MainActivity.class);
		startActivity(intent);
		this.finish();
      }
}
